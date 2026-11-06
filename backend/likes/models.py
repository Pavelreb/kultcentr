from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from posts.models import Post
from comments.models import Comment


class Like(models.Model):
    """
    Модель для лайков на посты и комментарии
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name="Пользователь",
    )

    # Связь с постом (может быть NULL, если лайк на комментарий)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="likes",
        verbose_name="Пост",
    )

    # Связь с комментарием (может быть NULL, если лайк на пост)
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="likes",
        verbose_name="Комментарий",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        # Один пользователь может поставить лайк только один раз на один пост
        unique_together = [
            ["user", "post"],
            ["user", "comment"],
        ]
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
        ordering = ["-created_at"]

    def clean(self):
        """Проверяем, что лайк привязан либо к посту, либо к комментарию"""
        if not self.post and not self.comment:
            raise ValidationError("Лайк должен быть привязан к посту или комментарию")
        if self.post and self.comment:
            raise ValidationError(
                "Лайк не может быть привязан одновременно к посту и комментарию"
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.post:
            return f"{self.user.username} → {self.post.title}"
        return f"{self.user.username} → комментарий {self.comment.id}"
