from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import PhotoComment, Photo
from .serializers import PhotoCommentSerializer


class PhotoCommentViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев к фотографиям"""

    queryset = PhotoComment.objects.all().select_related("user", "photo")
    serializer_class = PhotoCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "pk"

    def get_queryset(self):
        queryset = PhotoComment.objects.all().select_related("user", "photo")
        photo_id = self.request.query_params.get("photo_id")
        if photo_id:
            queryset = queryset.filter(photo_id=photo_id)
        return queryset

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer):
        photo_id = self.request.data.get("photo")
        if not photo_id:
            from rest_framework.exceptions import ValidationError

            raise ValidationError({"photo": "Это поле обязательно"})
        photo = get_object_or_404(Photo, id=photo_id)
        serializer.save(user=self.request.user, photo=photo)
        print(f"💬 Создан комментарий к фото: {serializer.instance.content[:30]}...")

    @action(detail=False, methods=["get"], url_path="my_comments")
    def my_comments(self, request):
        """Получить комментарии текущего пользователя"""
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Не авторизован"}, status=status.HTTP_401_UNAUTHORIZED
            )

        comments = PhotoComment.objects.filter(user=request.user).order_by(
            "-created_at"
        )
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """Получить конкретный комментарий"""
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            print(f"🔍 Получен комментарий к фото {instance.id}")
            return Response(serializer.data)
        except Exception as e:
            print(f"❌ Ошибка получения комментария: {e}")
            return Response(
                {"detail": "Комментарий не найден"}, status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        """Обновить комментарий (PUT)"""
        try:
            instance = self.get_object()

            print(
                f"🔍 Обновление комментария к фото {instance.id} пользователем {request.user.username}"
            )
            print(f"🔍 Автор комментария: {instance.user.username}")

            if instance.user != request.user:
                return Response(
                    {"detail": "Вы можете редактировать только свои комментарии"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            partial = kwargs.pop("partial", False)
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            print(f"✅ Комментарий к фото {instance.id} обновлён")
            return Response(serializer.data)

        except Exception as e:
            print(f"❌ Ошибка обновления комментария: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        """Обновить комментарий (PATCH)"""
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        """Удалить комментарий"""
        try:
            instance = self.get_object()

            print(
                f"🔍 Удаление комментария к фото {instance.id} пользователем {request.user.username}"
            )

            if instance.user != request.user and request.user.role != "editor":
                return Response(
                    {"detail": "Вы можете удалять только свои комментарии"},
                    status=status.HTTP_403_FORBIDDEN,
                )

            self.perform_destroy(instance)
            print(f"✅ Комментарий к фото {instance.id} удалён")
            return Response({"detail": "Комментарий удалён"}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"❌ Ошибка удаления комментария: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
