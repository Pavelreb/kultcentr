from django.db import models
from django.conf import settings
from django.utils import timezone


class InstitutionInfo(models.Model):
    """Общая информация об учреждении (одиночная запись, как баннер)"""

    name = models.CharField(
        max_length=255, default="Центр Культуры", verbose_name="Название учреждения"
    )
    description = models.TextField(
        default="", blank=True, verbose_name="Описание учреждения"
    )
    logo = models.ImageField(
        upload_to="about/", blank=True, null=True, verbose_name="Логотип (файл)"
    )
    logo_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на логотип"
    )
    background_image = models.ImageField(
        upload_to="about/", blank=True, null=True, verbose_name="Фон баннера (файл)"
    )
    background_image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на фон баннера"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return "Общая информация об учреждении"

    class Meta:
        verbose_name = "Информация об учреждении"
        verbose_name_plural = "Информация об учреждении"


class StaffMember(models.Model):
    """Сотрудник учреждения"""

    CATEGORY_CHOICES = [
        ("aup", "Административно-управленческий персонал"),
        ("main", "Основной персонал"),
        ("technical", "Технический персонал"),
        ("auxiliary", "Вспомогательный персонал"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="staff_profiles",
        verbose_name="Пользователь сайта",
    )
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="main",
        verbose_name="Категория персонала",
    )
    photo = models.ImageField(
        upload_to="about/staff/", blank=True, null=True, verbose_name="Фото (файл)"
    )
    photo_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на фото")
    bio = models.TextField(blank=True, null=True, verbose_name="О сотруднике")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} — {self.position}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["category", "order", "full_name"]


class Club(models.Model):
    """Клубное формирование"""

    title = models.CharField(max_length=255, verbose_name="Название")
    excerpt = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    content = models.TextField(blank=True, null=True, verbose_name="Полное описание")
    image = models.ImageField(
        upload_to="about/clubs/", blank=True, null=True, verbose_name="Изображение (файл)"
    )
    image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на изображение"
    )
    leader_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Руководитель"
    )
    schedule = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Расписание"
    )
    age = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Возраст участников"
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Клубное формирование"
        verbose_name_plural = "Клубные формирования"
        ordering = ["title"]


class Achievement(models.Model):
    """Достижение / награда учреждения"""

    title = models.CharField(max_length=255, verbose_name="Название")
    excerpt = models.TextField(blank=True, null=True, verbose_name="Краткое описание")
    content = models.TextField(blank=True, null=True, verbose_name="Полное описание")
    image = models.ImageField(
        upload_to="about/achievements/",
        blank=True,
        null=True,
        verbose_name="Изображение (файл)",
    )
    image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на изображение"
    )
    date = models.DateField(blank=True, null=True, verbose_name="Дата получения")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"
        ordering = ["-date", "-created_at"]
