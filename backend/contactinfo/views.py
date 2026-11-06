from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import ContactInfo
from .serializers import ContactInfoSerializer


class ContactInfoView(generics.RetrieveAPIView):
    """
    Получение контактной информации (доступно всем)
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.first()


class ContactInfoUpdateView(generics.UpdateAPIView):
    """
    Обновление контактной информации (только для редакторов)
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.first()

    def update(self, request, *args, **kwargs):
        user = request.user

        if user.role != "editor":
            return Response(
                {"detail": "Только главные редакторы могут редактировать контакты"},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().update(request, *args, **kwargs)
