# backend/gallery/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
import os


class Album(models.Model):
    """Модель альбома"""

    title = models.CharField(max_length=200, verbose_name="Название альбома")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    date = models.DateField(
        verbose_name="Дата события",
        help_text="Укажите дату, к которой относится альбом",
    )
    cover_image = models.ImageField(
        upload_to="albums/covers/",
        blank=True,
        null=True,
        verbose_name="Обложка альбома (файл)",
    )
    cover_image_url = models.URLField(
        blank=True, null=True, verbose_name="Обложка альбома (ссылка)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_cover_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        return self.cover_image_url

    def delete(self, *args, **kwargs):
        if self.cover_image:
            file_path = self.cover_image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"🗑️ Обложка альбома удалена: {file_path}")
        super().delete(*args, **kwargs)


class Photo(models.Model):
    """Модель фотографии"""

    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="photos", verbose_name="Альбом"
    )
    image = models.ImageField(upload_to="albums/photos/", verbose_name="Фотография")
    caption = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Подпись"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    likes_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество лайков"
    )

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ["order", "uploaded_at"]

    def __str__(self):
        return f"{self.album.title} - {self.id}"

    def increment_views(self):
        self.views += 1
        self.save(update_fields=["views"])

    def delete(self, *args, **kwargs):
        if self.image:
            file_path = self.image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"🗑️ Фотография удалена: {file_path}")
        super().delete(*args, **kwargs)


class PhotoLike(models.Model):
    """Модель лайка для фотографии"""

    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="likes", verbose_name="Фотография"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="photo_likes",
        verbose_name="Пользователь",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        unique_together = ["photo", "user"]
        verbose_name = "Лайк фотографии"
        verbose_name_plural = "Лайки фотографий"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} → {self.photo.id}"


class PhotoComment(models.Model):
    """Модель комментария к фотографии"""

    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Фотография",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="photo_comments",
        verbose_name="Пользователь",
    )
    content = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
        verbose_name="Родительский комментарий",
    )

    class Meta:
        verbose_name = "Комментарий к фото"
        verbose_name_plural = "Комментарии к фото"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"
