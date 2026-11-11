# backend/medialib/models.py

from django.conf import settings
from django.db import models
from django.utils import timezone


class Video(models.Model):
    """Видеоролик медиатеки (загружают только редакторы)"""

    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    file = models.FileField(
        upload_to="medialib/videos/", blank=True, null=True, verbose_name="Файл видео"
    )
    video_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на видео (вместо файла)"
    )
    thumbnail = models.ImageField(
        upload_to="medialib/videos/thumbs/",
        blank=True,
        null=True,
        verbose_name="Обложка",
    )
    thumbnail_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на обложку"
    )
    duration = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Длительность (сек)"
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_videos",
        verbose_name="Загрузил",
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видеоролик"
        verbose_name_plural = "Видеоролики"
        ordering = ["-created_at"]


class Audio(models.Model):
    """Аудиозапись медиатеки (загружают только редакторы, конвертируется в MP3)"""

    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    file = models.FileField(
        upload_to="medialib/audio/", blank=True, null=True, verbose_name="Файл аудио"
    )
    audio_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на аудио (вместо файла)"
    )
    cover = models.ImageField(
        upload_to="medialib/audio/covers/",
        blank=True,
        null=True,
        verbose_name="Обложка",
    )
    cover_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на обложку"
    )
    duration = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Длительность (сек)"
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_audio",
        verbose_name="Загрузил",
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи"
        ordering = ["-created_at"]
