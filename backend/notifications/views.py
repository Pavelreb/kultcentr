from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(APIView):
    """Список уведомлений текущего пользователя (последние 50)"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()[:50]
        unread = request.user.notifications.filter(is_read=False).count()
        return Response(
            {
                "unread_count": unread,
                "results": NotificationSerializer(notifications, many=True).data,
            }
        )


class NotificationUnreadCountView(APIView):
    """Лёгкий эндпоинт для бейджа в шапке"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        count = request.user.notifications.filter(is_read=False).count()
        return Response({"unread_count": count})


class NotificationReadAllView(APIView):
    """Отметить все уведомления прочитанными"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.notifications.filter(is_read=False).update(is_read=True)
        return Response({"detail": "Все уведомления прочитаны"})


class NotificationReadView(APIView):
    """Отметить одно уведомление прочитанным"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        updated = request.user.notifications.filter(pk=pk, is_read=False).update(
            is_read=True
        )
        return Response({"detail": "ok", "updated": updated})
