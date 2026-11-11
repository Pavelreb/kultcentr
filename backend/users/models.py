from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("subscriber", "Подписчик"),
        ("author", "Автор"),
        ("editor", "Главный редактор"),
    ]

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="subscriber", verbose_name="Роль"
    )

    bio = models.TextField(blank=True, null=True, verbose_name="О себе")

    patronymic = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Отчество"
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")

    # НОВОЕ ПОЛЕ ДЛЯ АВАТАРКИ
    avatar = models.ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="Аватар"
    )

    # Контакты и соцсети пользователя
    phone = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телефон"
    )
    vk = models.URLField(blank=True, null=True, verbose_name="ВКонтакте")
    max = models.URLField(blank=True, null=True, verbose_name="MAX")
    ok = models.URLField(blank=True, null=True, verbose_name="Одноклассники")
    rutube = models.URLField(blank=True, null=True, verbose_name="RuTube")

    # Настройки приватности
    show_phone = models.BooleanField(
        default=False, verbose_name="Показывать телефон публично"
    )
    show_email = models.BooleanField(
        default=False, verbose_name="Показывать email публично"
    )
    show_socials = models.BooleanField(
        default=True, verbose_name="Показывать соцсети публично"
    )

    # Последняя активность (для статуса «в сети»)
    last_activity = models.DateTimeField(
        blank=True, null=True, verbose_name="Последняя активность"
    )

    ONLINE_WINDOW_MINUTES = 5

    @property
    def is_online(self):
        """Пользователь в сети, если был активен в последние 5 минут"""
        if not self.last_activity:
            return False
        from django.utils import timezone

        return (
            timezone.now() - self.last_activity
        ).total_seconds() < self.ONLINE_WINDOW_MINUTES * 60

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Subscription(models.Model):
    """Подписка пользователя на автора/редактора"""

    subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="Подписчик",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscribers",
        verbose_name="Автор",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["subscriber", "author"], name="unique_subscription"
            )
        ]

    def __str__(self):
        return f"{self.subscriber} → {self.author}"
