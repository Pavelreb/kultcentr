from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор"
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    excerpt = models.TextField(blank=True, null=True, verbose_name="Краткое описание")

    # Два поля для изображений
    image = models.ImageField(
        upload_to="posts/", blank=True, null=True, verbose_name="Изображение (файл)"
    )
    image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на изображение"
    )

    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    is_featured = models.BooleanField(
        default=False, verbose_name="Главная публикация"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]


class Poll(models.Model):
    """Голосование, прикреплённое к посту"""

    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name="poll", verbose_name="Пост"
    )
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Голосование: {self.question}"

    class Meta:
        verbose_name = "Голосование"
        verbose_name_plural = "Голосования"


class PollOption(models.Model):
    """Вариант ответа голосования"""

    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="options", verbose_name="Голосование"
    )
    text = models.CharField(max_length=255, verbose_name="Вариант ответа")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"
        ordering = ["order", "id"]


class PollVote(models.Model):
    """Голос пользователя (один пользователь — один голос)"""

    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name="votes", verbose_name="Голосование"
    )
    option = models.ForeignKey(
        PollOption, on_delete=models.CASCADE, related_name="votes", verbose_name="Вариант"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} → {self.option}"

    class Meta:
        verbose_name = "Голос"
        verbose_name_plural = "Голоса"
        constraints = [
            models.UniqueConstraint(
                fields=["poll", "user"], name="unique_poll_vote_per_user"
            )
        ]


class Quiz(models.Model):
    """Тест, прикреплённый к посту"""

    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name="quiz", verbose_name="Пост"
    )
    title = models.CharField(max_length=255, verbose_name="Название теста")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Тест: {self.title}"

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class QuizQuestion(models.Model):
    """Вопрос теста"""

    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="questions", verbose_name="Тест"
    )
    text = models.CharField(max_length=500, verbose_name="Вопрос")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос теста"
        verbose_name_plural = "Вопросы теста"
        ordering = ["order", "id"]


class QuizAnswer(models.Model):
    """Вариант ответа на вопрос теста"""

    question = models.ForeignKey(
        QuizQuestion, on_delete=models.CASCADE, related_name="answers", verbose_name="Вопрос"
    )
    text = models.CharField(max_length=255, verbose_name="Ответ")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ответ теста"
        verbose_name_plural = "Ответы теста"
        ordering = ["order", "id"]


class QuizAttempt(models.Model):
    """Прохождение теста (один пользователь — одно прохождение)"""

    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="attempts", verbose_name="Тест"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    score = models.PositiveIntegerField(default=0, verbose_name="Верных ответов")
    total = models.PositiveIntegerField(default=0, verbose_name="Всего вопросов")
    answers = models.JSONField(
        default=dict, blank=True, verbose_name="Выбранные ответы"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} — {self.score}/{self.total}"

    class Meta:
        verbose_name = "Прохождение теста"
        verbose_name_plural = "Прохождения тестов"
        constraints = [
            models.UniqueConstraint(
                fields=["quiz", "user"], name="unique_quiz_attempt_per_user"
            )
        ]
