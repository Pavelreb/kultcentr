from django.db import models
from django.conf import settings
from django.utils import timezone
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Пост"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор"
    )
    content = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(  # НОВОЕ ПОЛЕ
        auto_now=True, verbose_name="Дата обновления"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="Родительский комментарий",
    )

    def clean(self):
        if self.parent and self.parent.post_id != self.post_id:
            from django.core.exceptions import ValidationError

            raise ValidationError(
                {
                    "parent": "Родительский комментарий должен принадлежать тому же посту!"
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["created_at"]
