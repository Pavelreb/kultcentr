from django.db import models
from django.conf import settings
import os


class Banner(models.Model):
    """Модель для управления Hero-баннером на главной странице"""

    title = models.CharField(
        max_length=200,
        default="🏛️ Добро пожаловать в Центр Культуры",
        verbose_name="Заголовок баннера",
    )
    subtitle = models.TextField(
        default="Место, где искусство, традиции и творчество объединяются",
        verbose_name="Подзаголовок",
    )

    background_image = models.ImageField(
        upload_to="banner/", blank=True, null=True, verbose_name="Фоновое изображение"
    )
    background_image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на фоновое изображение"
    )

    button_text = models.CharField(
        max_length=100,
        default="Смотреть афишу",
        blank=True,
        null=True,
        verbose_name="Текст кнопки",
    )
    button_link = models.CharField(
        max_length=200,
        default="/events",
        blank=True,
        null=True,
        verbose_name="Ссылка кнопки",
    )
    button_enabled = models.BooleanField(default=True, verbose_name="Кнопка активна")

    is_active = models.BooleanField(default=True, verbose_name="Баннер активен")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"

    def __str__(self):
        return f'Баннер (обновлен: {self.updated_at.strftime("%d.%m.%Y %H:%M")})'

    def delete(self, *args, **kwargs):
        if self.background_image:
            file_path = self.background_image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"🗑️ Фоновое изображение баннера удалено: {file_path}")
        super().delete(*args, **kwargs)
