# backend/posts/serializers.py

from rest_framework import serializers
from .models import (
    Post,
    Poll,
    PollOption,
    PollVote,
    Quiz,
    QuizQuestion,
    QuizAnswer,
    QuizAttempt,
)
from comments.serializers import CommentForPostSerializer


def _notify_subscribers_new_post(post):
    """Уведомить подписчиков автора о новой публикации"""
    from notifications.models import notify

    author_name = (
        f"{post.author.last_name} {post.author.first_name}".strip()
        or post.author.username
    )
    for sub in post.author.subscribers.select_related("subscriber"):
        notify(
            sub.subscriber,
            "new_post",
            f"{author_name} опубликовал новую публикацию «{post.title[:60]}»",
            f"/posts/{post.id}",
        )


def build_poll_data(post, request):
    """Собирает данные голосования для ответа API"""
    try:
        poll = post.poll
    except Poll.DoesNotExist:
        return None

    options = [
        {"id": o.id, "text": o.text, "votes": o.votes.count()}
        for o in poll.options.all()
    ]
    total_votes = sum(o["votes"] for o in options)

    user_vote = None
    can_manage = False
    if request and request.user.is_authenticated:
        vote = poll.votes.filter(user=request.user).first()
        user_vote = vote.option_id if vote else None
        can_manage = (
            request.user == post.author or request.user.role == "editor"
        )

    return {
        "id": poll.id,
        "question": poll.question,
        "options": options,
        "total_votes": total_votes,
        "user_vote": user_vote,
        "can_manage": can_manage,
    }


def build_quiz_data(post, request):
    """Собирает данные теста для ответа API"""
    try:
        quiz = post.quiz
    except Quiz.DoesNotExist:
        return None

    user = request.user if request else None
    is_authenticated = bool(user and user.is_authenticated)
    can_manage = is_authenticated and (
        user == post.author or user.role == "editor"
    )

    attempt = None
    if is_authenticated:
        attempt = quiz.attempts.filter(user=user).first()

    show_correct = can_manage or attempt is not None

    questions = []
    for q in quiz.questions.prefetch_related("answers"):
        answers = []
        for a in q.answers.all():
            answer = {"id": a.id, "text": a.text}
            if show_correct:
                answer["is_correct"] = a.is_correct
            answers.append(answer)
        questions.append({"id": q.id, "text": q.text, "answers": answers})

    return {
        "id": quiz.id,
        "title": quiz.title,
        "description": quiz.description,
        "questions": questions,
        "questions_count": len(questions),
        "attempted": attempt is not None,
        "score": attempt.score if attempt else None,
        "total": attempt.total if attempt else None,
        "my_answers": attempt.answers if attempt else None,
        "can_manage": can_manage,
    }


def _save_poll(post, poll_data):
    """Создать/заменить/удалить голосование поста"""
    if poll_data is None:
        Poll.objects.filter(post=post).delete()
        return

    question = (poll_data.get("question") or "").strip()
    options = [
        (o or "").strip()
        for o in poll_data.get("options", [])
        if (o or "").strip()
    ]

    if not question:
        raise serializers.ValidationError(
            {"poll": "Укажите вопрос голосования"}
        )
    if len(options) < 2:
        raise serializers.ValidationError(
            {"poll": "Голосованию нужно минимум 2 варианта ответа"}
        )

    Poll.objects.filter(post=post).delete()
    poll = Poll.objects.create(post=post, question=question)
    for i, text in enumerate(options):
        PollOption.objects.create(poll=poll, text=text, order=i)


def _save_quiz(post, quiz_data):
    """Создать/заменить/удалить тест поста"""
    if quiz_data is None:
        Quiz.objects.filter(post=post).delete()
        return

    title = (quiz_data.get("title") or "").strip()
    description = (quiz_data.get("description") or "").strip()
    questions = quiz_data.get("questions", [])

    if not title:
        raise serializers.ValidationError({"quiz": "Укажите название теста"})
    if not questions:
        raise serializers.ValidationError(
            {"quiz": "В тесте должен быть хотя бы 1 вопрос"}
        )

    for q in questions:
        text = (q.get("text") or "").strip()
        answers = [
            a for a in q.get("answers", []) if (a.get("text") or "").strip()
        ]
        if not text:
            raise serializers.ValidationError(
                {"quiz": "У каждого вопроса должен быть текст"}
            )
        if len(answers) < 2:
            raise serializers.ValidationError(
                {"quiz": f"У вопроса «{text[:50]}» должно быть минимум 2 ответа"}
            )
        if not any(a.get("is_correct") for a in answers):
            raise serializers.ValidationError(
                {"quiz": f"У вопроса «{text[:50]}» не отмечен правильный ответ"}
            )

    Quiz.objects.filter(post=post).delete()
    quiz = Quiz.objects.create(
        post=post, title=title, description=description or None
    )
    for qi, q in enumerate(questions):
        question = QuizQuestion.objects.create(
            quiz=quiz, text=q["text"].strip(), order=qi
        )
        for ai, a in enumerate(q["answers"]):
            if not (a.get("text") or "").strip():
                continue
            QuizAnswer.objects.create(
                question=question,
                text=a["text"].strip(),
                is_correct=bool(a.get("is_correct")),
                order=ai,
            )



class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_name = serializers.CharField(source="author.username", read_only=True)
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_role = serializers.CharField(source="author.role", read_only=True)
    author_avatar = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    user_has_liked = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()
    poll = serializers.JSONField(required=False, allow_null=True, write_only=True)
    quiz = serializers.JSONField(required=False, allow_null=True, write_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "image",
            "image_url",
            "display_image",
            "author_id",
            "author_name",
            "author_first_name",  # ✅ НОВОЕ ПОЛЕ
            "author_last_name",  # ✅ НОВОЕ ПОЛЕ
            "author_full_name",  # ✅ НОВОЕ ПОЛЕ
            "author_role",
            "author_avatar",
            "created_at",
            "updated_at",
            "is_published",
            "excerpt",
            "is_featured",
            "comments",
            "likes_count",
            "user_has_liked",
            "views",
            "poll",
            "quiz",
        ]
        read_only_fields = [
            "author",
            "author_name",
            "author_first_name",
            "author_last_name",
            "author_full_name",
            "author_role",
            "author_avatar",
            "created_at",
            "updated_at",
            "views",
            "is_featured",
        ]

    def get_comments(self, obj):
        top_level_comments = obj.comments.filter(parent__isnull=True)
        context = {"request": self.context.get("request")}
        return CommentForPostSerializer(
            top_level_comments, many=True, context=context
        ).data

    def get_user_has_liked(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()

    def get_author_avatar(self, obj):
        if obj.author.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.author.avatar.url)
            return obj.author.avatar.url
        return None

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url

    def get_author_full_name(self, obj):
        """Возвращает полное имя автора (Фамилия Имя Отчество)"""
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        if obj.author.patronymic:
            parts.append(obj.author.patronymic)
        return " ".join(parts) if parts else obj.author.username

    def create(self, validated_data):
        request = self.context.get("request")
        poll_data = validated_data.pop("poll", None)
        quiz_data = validated_data.pop("quiz", None)
        if (poll_data is not None or quiz_data is not None) and (
            not request or request.user.role != "editor"
        ):
            raise serializers.ValidationError(
                {"detail": "Голосования и тесты могут создавать только редакторы"}
            )
        validated_data["author"] = request.user
        post = super().create(validated_data)
        if poll_data is not None:
            _save_poll(post, poll_data)
        if quiz_data is not None:
            _save_quiz(post, quiz_data)
        if post.is_published:
            _notify_subscribers_new_post(post)
        return post

    def update(self, instance, validated_data):
        poll_data = validated_data.pop("poll", "__keep__")
        quiz_data = validated_data.pop("quiz", "__keep__")
        if (poll_data != "__keep__" or quiz_data != "__keep__"):
            request = self.context.get("request")
            if not request or request.user.role != "editor":
                raise serializers.ValidationError(
                    {"detail": "Голосования и тесты могут изменять только редакторы"}
                )
        was_published = instance.is_published
        post = super().update(instance, validated_data)
        if poll_data != "__keep__":
            _save_poll(post, poll_data)
        if quiz_data != "__keep__":
            _save_quiz(post, quiz_data)
        if post.is_published and not was_published:
            _notify_subscribers_new_post(post)
        return post

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        data["poll"] = build_poll_data(instance, request)
        data["quiz"] = build_quiz_data(instance, request)
        return data
