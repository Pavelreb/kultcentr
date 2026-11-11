from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    ASSESSMENT_QUESTIONS,
    AssessmentResponse,
    FeedbackMessage,
)
from .serializers import AssessmentResponseSerializer, FeedbackMessageSerializer


def is_editor(user):
    return user.is_authenticated and user.role == "editor"


class FeedbackListCreateView(APIView):
    """POST — любой посетитель; GET — только редакторы"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = FeedbackMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Сообщение отправлено"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if not is_editor(request.user):
            return Response({"detail": "Доступ запрещён"}, status=403)
        messages = FeedbackMessage.objects.all()
        return Response(FeedbackMessageSerializer(messages, many=True).data)


class AssessmentQuestionsView(APIView):
    """Список вопросов опроса (публичный)"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(ASSESSMENT_QUESTIONS)


class AssessmentListCreateView(APIView):
    """POST — любой посетитель; GET — только редакторы (сводка + ответы)"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = AssessmentResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Спасибо за участие в опросе!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if not is_editor(request.user):
            return Response({"detail": "Доступ запрещён"}, status=403)
        responses = AssessmentResponse.objects.all()
        data = AssessmentResponseSerializer(responses, many=True).data

        # Средние оценки по каждому вопросу
        averages = []
        for q in ASSESSMENT_QUESTIONS:
            scores = [r["ratings"][q["key"]] for r in data]
            averages.append(
                {
                    "key": q["key"],
                    "text": q["text"],
                    "average": round(sum(scores) / len(scores), 2) if scores else None,
                    "distribution": {
                        str(n): scores.count(n) for n in range(1, 6)
                    },
                }
            )

        overall = None
        scored = [a for a in averages if a["average"] is not None]
        if scored:
            overall = round(sum(a["average"] for a in scored) / len(scored), 2)

        return Response(
            {
                "total": len(data),
                "overall_average": overall,
                "averages": averages,
                "responses": data,
            }
        )
