from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from urllib.parse import unquote
import os
from .models import Event
from .serializers import EventSerializer
from .permissions import IsEditorOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEditorOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    # Поиск: /api/events/?search=текст
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content", "location", "excerpt"]

    def get_queryset(self):
        queryset = Event.objects.all()

        if self.action == "list":
            return queryset.filter(is_published=True).order_by("event_date")

        return queryset

    def retrieve(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs["pk"])

        if event.is_published:
            serializer = self.get_serializer(event)
            return Response(serializer.data)

        user = request.user
        if user.is_authenticated and user.role == "editor":
            serializer = self.get_serializer(event)
            return Response(serializer.data)

        return Response({"detail": "Событие не найдено"}, status=404)

    def create(self, request, *args, **kwargs):
        print("=" * 60)
        print("📸 СОЗДАНИЕ СОБЫТИЯ")
        print(f"📥 request.FILES: {request.FILES}")
        print(f"📥 request.data: {request.data}")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        print(f"✅ Создано событие: {serializer.instance.title}")
        if serializer.instance.image:
            print(f"🖼️ Изображение сохранено: {serializer.instance.image.url}")
        else:
            print("🖼️ Изображение НЕ сохранено")
        print("=" * 60)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        print("=" * 60)
        print("📸 ОБНОВЛЕНИЕ СОБЫТИЯ")

        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        print(f"📝 Название: {instance.title}")
        print(f"🆔 ID: {instance.id}")
        print(f"🖼️ Старое изображение в БД: {instance.image}")
        print(f"🖼️ Старое image_url: {instance.image_url}")

        user = request.user
        if instance.is_published:
            if user.role != "editor":
                return Response({"detail": "Недостаточно прав"}, status=403)
        else:
            if user.role != "editor":
                return Response({"detail": "Недостаточно прав"}, status=403)

        old_image = instance.image

        print(f"📥 request.FILES: {request.FILES}")
        print(f"📥 request.data: {request.data}")

        if "image" in request.FILES:
            print(f'📎 Файл найден в FILES: {request.FILES["image"].name}')
            print(f'📎 Размер: {request.FILES["image"].size} байт')
            print(f'📎 Тип: {request.FILES["image"].content_type}')
        else:
            print("📎 Файл НЕ найден в request.FILES")

        data = request.data.copy()

        if "image" in request.FILES:
            data["image"] = request.FILES["image"]

        if "image_url" in data and data["image_url"] == "":
            print("🖼️ Получен запрос на удаление изображения")
            if instance.image:
                file_path = instance.image.path
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f"🗑️ Изображение события удалено: {file_path}")
                    except Exception as e:
                        print(f"❌ Ошибка удаления: {e}")
                instance.image = None
                instance.save()

        serializer = self.get_serializer(instance, data=data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            print("✅ Сериализатор валиден")
        except Exception as e:
            print(f"❌ Ошибка валидации: {e}")
            raise

        self.perform_update(serializer)
        print("💾 Сериализатор сохранён")

        instance.refresh_from_db()
        print(f"🖼️ Новое изображение в БД: {instance.image}")
        print(f"🖼️ Новый image_url: {instance.image_url}")
        if instance.image:
            print(f"🖼️ URL: {instance.image.url}")

        if "image" in request.FILES and old_image:
            instance.refresh_from_db()
            if old_image != instance.image and instance.image:
                try:
                    file_path = old_image.path
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"🗑️ Старое изображение события удалено: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")

        print("=" * 60)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        print(f"🗑️ Удаляем событие: {instance.title}")
        if instance.image:
            file_path = instance.image.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"🗑️ Изображение события удалено: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")
        instance.delete()

    @action(detail=True, methods=["post"], url_path="feature")
    def feature(self, request, pk=None):
        """Назначить событие главной афишей (только редактор)"""
        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        event = get_object_or_404(Event, pk=pk)
        if not event.is_published:
            return Response(
                {"detail": "Главной может быть только опубликованная афиша"},
                status=400,
            )

        Event.objects.filter(is_featured=True).exclude(pk=event.pk).update(
            is_featured=False
        )
        event.is_featured = True
        event.save(update_fields=["is_featured"])
        return Response(self.get_serializer(event).data)

    @action(detail=False, methods=["post"], url_path="unfeature")
    def unfeature(self, request):
        """Сбросить главную афишу — выбор станет автоматическим"""
        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        Event.objects.filter(is_featured=True).update(is_featured=False)
        return Response({"detail": "Главная афиша сброшена"})

    @action(detail=False, methods=["get"], url_path="my_events")
    def my_events(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Не авторизован"}, status=401)

        if user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        events = Event.objects.filter(author=user).order_by("event_date")
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["post"],
        url_path="upload-image",
        parser_classes=[MultiPartParser, FormParser],
    )
    def upload_image(self, request):
        user = request.user

        if not user.is_authenticated or user.role != "editor":
            return Response(
                {"detail": "Недостаточно прав"}, status=status.HTTP_403_FORBIDDEN
            )

        if "image" not in request.FILES:
            return Response(
                {"detail": "Файл не передан"}, status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES["image"]

        if file.size > 5 * 1024 * 1024:
            return Response(
                {"detail": "Файл слишком большой (макс 5MB)"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
        if file.content_type not in allowed_types:
            return Response(
                {
                    "detail": "Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        filename = f"events/temp_{user.id}_{file.name}"
        file_path = default_storage.save(filename, ContentFile(file.read()))
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)

        print(f"📁 Загружено изображение: {file_path}")
        print(f"📁 URL: {file_url}")

        return Response(
            {"image_url": file_url, "detail": "Изображение загружено"},
            status=status.HTTP_200_OK,
        )
