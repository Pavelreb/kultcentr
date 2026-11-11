from django.conf import settings
from django.db import models
from django.utils import timezone


class FeedbackMessage(models.Model):
    """Сообщение обратной связи (может отправить любой посетитель)"""

    email = models.EmailField(verbose_name="Электронная почта")
    full_name = models.CharField(
        max_length=255, blank=True, default="", verbose_name="Ф.И.О."
    )
    text = models.TextField(verbose_name="Текст сообщения")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Отправлено")

    def __str__(self):
        return f"{self.email}: {self.text[:50]}"

    class Meta:
        verbose_name = "Сообщение обратной связи"
        verbose_name_plural = "Обратная связь"
        ordering = ["-created_at"]


# Вопросы независимой оценки качества услуг учреждения
ASSESSMENT_QUESTIONS = [
    {"key": "availability", "text": "Доступность учреждения (удобство расположения, режим работы)"},
    {"key": "comfort", "text": "Комфортность помещений и территории"},
    {"key": "staff", "text": "Доброжелательность и компетентность сотрудников"},
    {"key": "quality", "text": "Качество мероприятий и услуг"},
    {"key": "information", "text": "Информированность о мероприятиях (афиши, сайт, соцсети)"},
    {"key": "overall", "text": "Общая удовлетворённость учреждением"},
]

ASSESSMENT_KEYS = [q["key"] for q in ASSESSMENT_QUESTIONS]


class AssessmentResponse(models.Model):
    """Ответ на опрос независимой оценки (оценки 1–5 по каждому вопросу)"""

    email = models.EmailField(verbose_name="Электронная почта")
    full_name = models.CharField(
        max_length=255, blank=True, default="", verbose_name="Ф.И.О."
    )
    text = models.TextField(verbose_name="Комментарий")
    ratings = models.JSONField(
        default=dict, verbose_name="Оценки по вопросам"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Отправлено")

    def __str__(self):
        return f"{self.email} — {self.created_at:%d.%m.%Y}"

    class Meta:
        verbose_name = "Ответ опроса оценки"
        verbose_name_plural = "Ответы опроса оценки"
        ordering = ["-created_at"]
