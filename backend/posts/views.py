from rest_framework import viewsets, permissions, status, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from urllib.parse import unquote
import os
from django.db import models
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrEditorOrReadOnly, IsAuthorUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrEditorOrReadOnly,
        IsAuthorUser,
    ]
    # Поиск: /api/posts/?search=текст
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content", "excerpt"]

    def get_queryset(self):
        user = self.request.user

        queryset = Post.objects.all()
        author_name = self.request.query_params.get("author_name")

        if author_name:
            queryset = queryset.filter(author__username=author_name)
            if user.is_authenticated:
                if user.username == author_name or user.role == "editor":
                    return queryset
            return queryset.filter(is_published=True)

        if self.action == "list":
            return queryset.filter(is_published=True)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])

        if post.is_published:
            post.views += 1
            post.save(update_fields=["views"])
            serializer = self.get_serializer(post)
            return Response(serializer.data)

        user = request.user
        if user.is_authenticated and (post.author == user or user.role == "editor"):
            post.views += 1
            post.save(update_fields=["views"])
            serializer = self.get_serializer(post)
            return Response(serializer.data)

        return Response({"detail": "Пост не найден"}, status=404)

    def update(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        user = request.user

        if post.is_published:
            if post.author != user and user.role != "editor":
                return Response({"detail": "Недостаточно прав"}, status=403)
        else:
            if post.author != user and user.role != "editor":
                return Response({"detail": "Недостаточно прав"}, status=403)

        old_post = Post.objects.get(pk=kwargs["pk"])
        old_image_url = old_post.image_url
        old_image = old_post.image

        print("=" * 60)
        print(f"🔍 Обновляем пост: {post.title}")
        print(f"🔍 Старое изображение URL: {old_image_url}")
        print(f"🔍 Старое изображение файл: {old_image}")

        response = super().update(request, *args, **kwargs)

        post.refresh_from_db()

        new_image_url = post.image_url
        new_image = post.image

        print(f"🔍 Новое изображение URL: {new_image_url}")
        print(f"🔍 Новое изображение файл: {new_image}")

        if old_image_url and old_image_url != new_image_url:
            print(f"🔍 Изображение изменилось, удаляем старое: {old_image_url}")

            if "/media/" in old_image_url:
                filename = old_image_url.split("/media/")[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f"🔍 Путь к старому файлу: {file_path}")

                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f"✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}")
                    except Exception as e:
                        print(f"❌ Ошибка удаления: {e}")
                else:
                    print(f"⚠️ Старый файл не найден: {file_path}")

        if old_image and old_image != new_image:
            file_path = old_image.path
            print(f"🔍 Удаляем старый файл image: {file_path}")
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")

        print("=" * 60)

        return response

    def perform_destroy(self, instance):
        print("=" * 60)
        print(f"🔍 Удаляем пост: {instance.title}")
        print(f"🔍 ID поста: {instance.id}")

        if instance.image:
            print(f"🔍 Поле image: {instance.image.name}")
            file_path = instance.image.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"✅ Изображение УСПЕШНО УДАЛЕНО: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")
        else:
            print("🔍 У поста нет image (загружено через ссылку)")

        if instance.image_url:
            print(f"🔍 image_url: {instance.image_url}")

            if "/media/" in instance.image_url:
                filename = instance.image_url.split("/media/")[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f"🔍 Декодированное имя: {filename}")
                print(f"🔍 Полный путь: {file_path}")

                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f"✅ Изображение по URL УСПЕШНО УДАЛЕНО: {file_path}")
                    except Exception as e:
                        print(f"❌ Ошибка удаления: {e}")
                else:
                    print(f"⚠️ Файл не найден: {file_path}")

        print("=" * 60)
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["post"], url_path="feature")
    def feature(self, request, pk=None):
        """Назначить пост главной публикацией (только редактор)"""
        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        post = get_object_or_404(Post, pk=pk)
        if not post.is_published:
            return Response(
                {"detail": "Главной может быть только опубликованная публикация"},
                status=400,
            )

        Post.objects.filter(is_featured=True).exclude(pk=post.pk).update(
            is_featured=False
        )
        post.is_featured = True
        post.save(update_fields=["is_featured"])
        return Response(self.get_serializer(post).data)

    @action(detail=False, methods=["post"], url_path="unfeature")
    def unfeature(self, request):
        """Сбросить главную публикацию — выбор станет автоматическим"""
        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        Post.objects.filter(is_featured=True).update(is_featured=False)
        return Response({"detail": "Главная публикация сброшена"})

    @action(detail=False, methods=["get"], url_path="my_posts")
    def my_posts(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Не авторизован"}, status=401)

        posts = Post.objects.filter(author=user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["post"],
        url_path="upload-image",
        parser_classes=[MultiPartParser, FormParser],
    )
    def upload_image(self, request):
        user = request.user

        if not user.is_authenticated or (user.role not in ["author", "editor"]):
            return Response(
                {"detail": "Недостаточно прав"}, status=status.HTTP_403_FORBIDDEN
            )

        if "image" not in request.FILES:
            return Response(
                {"detail": "Файл не передан"}, status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES["image"]

        if file.size > 5 * 1024 * 1024:
            return Response(
                {"detail": "Файл слишком большой (макс 5MB)"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
        if file.content_type not in allowed_types:
            return Response(
                {
                    "detail": "Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        filename = f"posts/{user.id}_{file.name}"
        file_path = default_storage.save(filename, ContentFile(file.read()))
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)

        print(f"📁 Загружено изображение для поста: {file_path}")
        print(f"📁 URL: {file_url}")

        return Response(
            {"image_url": file_url, "detail": "Изображение загружено"},
            status=status.HTTP_200_OK,
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["post"], url_path="poll/vote")
    def poll_vote(self, request, pk=None):
        """Проголосовать (один пользователь — один голос)"""
        from .models import Poll, PollOption, PollVote
        from .serializers import build_poll_data

        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "Не авторизован"}, status=401)

        post = get_object_or_404(Post, pk=pk)
        poll = Poll.objects.filter(post=post).first()
        if not poll:
            return Response({"detail": "У поста нет голосования"}, status=404)

        option_id = request.data.get("option_id")
        option = poll.options.filter(pk=option_id).first()
        if not option:
            return Response({"detail": "Вариант не найден"}, status=400)

        if poll.votes.filter(user=user).exists():
            return Response({"detail": "Вы уже голосовали"}, status=400)

        PollVote.objects.create(poll=poll, option=option, user=user)
        return Response(build_poll_data(post, request))

    @action(detail=True, methods=["post"], url_path="quiz/submit")
    def quiz_submit(self, request, pk=None):
        """Отправить прохождение теста (один раз на пользователя)"""
        from .models import Quiz, QuizAttempt
        from .serializers import build_quiz_data

        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "Не авторизован"}, status=401)

        post = get_object_or_404(Post, pk=pk)
        quiz = Quiz.objects.filter(post=post).first()
        if not quiz:
            return Response({"detail": "У поста нет теста"}, status=404)

        if quiz.attempts.filter(user=user).exists():
            return Response(
                {"detail": "Вы уже проходили этот тест"}, status=400
            )

        answers = request.data.get("answers", {})
        if not isinstance(answers, dict):
            return Response({"detail": "Неверный формат ответов"}, status=400)

        questions = list(quiz.questions.prefetch_related("answers"))
        if not questions:
            return Response({"detail": "В тесте нет вопросов"}, status=400)

        score = 0
        saved_answers = {}
        for q in questions:
            answer_id = answers.get(str(q.id)) or answers.get(q.id)
            try:
                answer_id = int(answer_id)
            except (TypeError, ValueError):
                return Response(
                    {"detail": "Ответьте на все вопросы"}, status=400
                )
            answer = q.answers.filter(pk=answer_id).first()
            if not answer:
                return Response(
                    {"detail": "Ответ не найден"}, status=400
                )
            saved_answers[str(q.id)] = answer_id
            if answer.is_correct:
                score += 1

        QuizAttempt.objects.create(
            quiz=quiz,
            user=user,
            score=score,
            total=len(questions),
            answers=saved_answers,
        )
        return Response(build_quiz_data(post, request))

    @action(detail=False, methods=["get"], url_path="stats")
    def stats(self, request):
        """Статистика голосований и тестов (только для редакторов)"""
        from .models import Poll, Quiz

        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Доступ запрещён"}, status=403)

        def user_label(u):
            parts = [u.last_name, u.first_name]
            name = " ".join(p for p in parts if p)
            return name or u.username

        polls_data = []
        for poll in (
            Poll.objects.select_related("post")
            .prefetch_related("options__votes__user")
            .order_by("-created_at")
        ):
            options = []
            total_votes = 0
            for o in poll.options.all():
                votes = o.votes.count()
                total_votes += votes
                options.append(
                    {
                        "id": o.id,
                        "text": o.text,
                        "votes": votes,
                        "voters": [
                            {"name": user_label(v.user), "voted_at": v.created_at}
                            for v in o.votes.all()
                        ],
                    }
                )
            polls_data.append(
                {
                    "id": poll.id,
                    "post_id": poll.post_id,
                    "post_title": poll.post.title,
                    "question": poll.question,
                    "total_votes": total_votes,
                    "options": options,
                    "created_at": poll.created_at,
                }
            )

        quizzes_data = []
        for quiz in (
            Quiz.objects.select_related("post")
            .prefetch_related("attempts__user", "questions")
            .order_by("-created_at")
        ):
            attempts = [
                {
                    "name": user_label(a.user),
                    "score": a.score,
                    "total": a.total,
                    "created_at": a.created_at,
                }
                for a in quiz.attempts.all()
            ]
            avg_percent = (
                round(
                    sum(a["score"] / a["total"] for a in attempts if a["total"])
                    / len(attempts)
                    * 100
                )
                if attempts
                else None
            )
            quizzes_data.append(
                {
                    "id": quiz.id,
                    "post_id": quiz.post_id,
                    "post_title": quiz.post.title,
                    "title": quiz.title,
                    "questions_count": quiz.questions.count(),
                    "attempts_count": len(attempts),
                    "avg_percent": avg_percent,
                    "attempts": attempts,
                    "created_at": quiz.created_at,
                }
            )

        return Response({"polls": polls_data, "quizzes": quizzes_data})
