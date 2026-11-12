from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
from .models import Banner
from .serializers import BannerSerializer


class BannerView(generics.RetrieveAPIView):
    """Публичный просмотр баннера"""

    permission_classes = [permissions.AllowAny]
    serializer_class = BannerSerializer

    def get_object(self):
        banner = Banner.objects.first()
        if not banner:
            banner = Banner.objects.create()
        return banner


class BannerUpdateView(generics.UpdateAPIView):
    """Обновление баннера (только для редакторов)"""

    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = BannerSerializer

    def get_object(self):
        banner = Banner.objects.first()
        if not banner:
            banner = Banner.objects.create()
        return banner

    def update(self, request, *args, **kwargs):
        user = request.user

        if user.role != "editor":
            return Response(
                {"detail": "Только главные редакторы могут редактировать баннер"},
                status=status.HTTP_403_FORBIDDEN,
            )

        instance = self.get_object()

        old_background = instance.background_image
        should_remove_image = False

        if "background_image_url" in request.data:
            if (
                request.data["background_image_url"] == ""
                or request.data["background_image_url"] == "null"
            ):
                should_remove_image = True
                if instance.background_image:
                    file_path = instance.background_image.path
                    if os.path.isfile(file_path):
                        try:
                            os.remove(file_path)
                            print(
                                f"🗑️ Фоновое изображение баннера удалено: {file_path}"
                            )
                        except Exception as e:
                            print(f"❌ Ошибка удаления: {e}")
                    instance.background_image = None
                instance.background_image_url = None

        # QueryDict.copy() делает deepcopy и падает на больших файлах
        # (TemporaryUploadedFile: cannot pickle 'BufferedRandom'),
        # поэтому берём обычный dict — файлы передаются по ссылке
        data = request.data.dict()

        if should_remove_image:
            if "background_image_url" in data:
                data["background_image_url"] = None
            if "background_image" in data:
                data.pop("background_image", None)

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        instance.refresh_from_db()

        if "background_image" in request.FILES and old_background:
            if old_background != instance.background_image:
                file_path = old_background.path
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(
                            f"🗑️ Старое фоновое изображение баннера удалено: {file_path}"
                        )
                    except Exception as e:
                        print(f"❌ Ошибка удаления: {e}")

        response_data = serializer.data
        response_data["background_image_url_display"] = (
            serializer.get_background_image_url_display(instance)
        )
        response_data["has_background"] = serializer.get_has_background(instance)

        return Response(response_data)

    def perform_update(self, serializer):
        print("=" * 60)
        print("🎨 ОБНОВЛЕНИЕ БАННЕРА")
        print(f"👤 Редактор: {self.request.user.username}")
        print(f'📝 Заголовок: {serializer.validated_data.get("title", "не изменён")}')
        print(
            f'📝 Подзаголовок: {serializer.validated_data.get("subtitle", "не изменён")}'
        )
        print(
            f'🔘 Кнопка активна: {serializer.validated_data.get("button_enabled", "не изменён")}'
        )
        print(
            f'📊 Баннер активен: {serializer.validated_data.get("is_active", "не изменён")}'
        )
        print("=" * 60)
        serializer.save()
