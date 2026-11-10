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

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
