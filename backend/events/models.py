import os
from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название события")
    content = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор"
    )

    event_date = models.DateTimeField(
        verbose_name="Дата и время проведения", null=True, blank=True
    )
    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Место проведения"
    )
    price = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Стоимость"
    )

    image = models.ImageField(
        upload_to="events/", blank=True, null=True, verbose_name="Изображение (файл)"
    )
    image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на изображение"
    )

    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    excerpt = models.TextField(blank=True, null=True, verbose_name="Краткое описание")

    def delete_image_file(self):
        """Удаляет файл изображения с диска"""
        if self.image:
            file_path = self.image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"🗑️ Изображение события удалено: {file_path}")
                return True
            else:
                print(f"⚠️ Файл не найден: {file_path}")
        return False

    def delete(self, *args, **kwargs):
        """При удалении события удаляем изображение с диска"""
        self.delete_image_file()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ["-event_date", "-created_at"]
