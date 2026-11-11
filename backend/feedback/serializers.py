from rest_framework import serializers

from .models import (
    ASSESSMENT_KEYS,
    AssessmentResponse,
    FeedbackMessage,
)


class FeedbackMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackMessage
        fields = ["id", "email", "full_name", "text", "created_at"]

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Введите текст сообщения")
        return value.strip()


class AssessmentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResponse
        fields = ["id", "email", "full_name", "text", "ratings", "created_at"]

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Введите комментарий")
        return value.strip()

    def validate_ratings(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Неверный формат оценок")
        for key in ASSESSMENT_KEYS:
            score = value.get(key)
            if not isinstance(score, int) or not (1 <= score <= 5):
                raise serializers.ValidationError(
                    "Поставьте оценку от 1 до 5 на каждый вопрос"
                )
        # Отбрасываем лишние ключи
        return {key: value[key] for key in ASSESSMENT_KEYS}
