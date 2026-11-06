from django.db import models


class ContactInfo(models.Model):
    """
    Модель для хранения контактной информации учреждения
    """

    address = models.CharField(
        max_length=255, default="г. Москва, ул. Культурная, д. 1", verbose_name="Адрес"
    )
    phone = models.CharField(
        max_length=50, default="+7 (495) 123-45-67", verbose_name="Телефон"
    )
    email = models.EmailField(default="info@kultcentr.ru", verbose_name="Email")
    work_hours = models.CharField(
        max_length=100, default="Пн–Пт: 10:00 – 20:00", verbose_name="Часы работы"
    )
    description = models.TextField(
        default="Место, где искусство, традиции и творчество объединяются.\nМы создаём пространство для культурного развития и вдохновения.",
        verbose_name="Описание",
    )
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    vk = models.URLField(blank=True, null=True, verbose_name="ВКонтакте")
    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return (
            f'Контактная информация (обновлено: {self.updated_at.strftime("%d.%m.%Y")})'
        )

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"
