from django.conf import settings
from django.db import models
from django.utils import timezone


class Notification(models.Model):
    """Уведомление пользователя"""

    TYPE_CHOICES = [
        ("subscription", "Новый подписчик"),
        ("comment", "Комментарий к публикации"),
        ("like", "Лайк"),
        ("new_post", "Новая публикация автора"),
        ("reply", "Ответ на комментарий"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Получатель",
    )
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, verbose_name="Тип"
    )
    text = models.CharField(max_length=500, verbose_name="Текст")
    link = models.CharField(
        max_length=300, blank=True, default="", verbose_name="Ссылка"
    )
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Создано")

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} ← {self.text[:50]}"


def notify(user, type_, text, link=""):
    """Создать уведомление (с защитой от ошибок — уведомление не должно ломать основное действие)"""
    if not user or not user.is_authenticated:
        return
    try:
        Notification.objects.create(user=user, type=type_, text=text, link=link)
    except Exception:
        pass
