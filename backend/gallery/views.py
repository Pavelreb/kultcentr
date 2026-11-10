from rest_framework import viewsets, permissions, status, generics, filters
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
from .models import Album, Photo, PhotoLike
from .serializers import (
    AlbumListSerializer,
    AlbumDetailSerializer,
    AlbumCreateUpdateSerializer,
    PhotoSerializer,
)
from .permissions import IsEditorOrReadOnly


class AlbumViewSet(viewsets.ModelViewSet):
    """ViewSet для альбомов"""

    queryset = Album.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsEditorOrReadOnly]
    # Поиск: /api/albums/?search=текст
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]

    def get_serializer_class(self):
        if self.action == "list":
            return AlbumListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return AlbumCreateUpdateSerializer
        return AlbumDetailSerializer

    def get_queryset(self):
        queryset = Album.objects.all()

        if not self.request.user.is_authenticated:
            return queryset.filter(is_published=True)

        return queryset

    def perform_create(self, serializer):
        serializer.save()
        print(f"📸 Создан альбом: {serializer.instance.title}")

    def perform_update(self, serializer):
        instance = serializer.instance
        old_cover = instance.cover_image

        serializer.save()

        if old_cover and old_cover != instance.cover_image:
            file_path = old_cover.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"🗑️ Старая обложка альбома удалена: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")

        print(f"📸 Обновлён альбом: {serializer.instance.title}")

    def perform_destroy(self, instance):
        print(f"🗑️ Удаляем альбом: {instance.title}")
        instance.delete()

    @action(detail=True, methods=["post"], url_path="upload-photos")
    def upload_photos(self, request, pk=None):
        """Загрузка нескольких фотографий в альбом"""
        album = self.get_object()

        if request.user.role != "editor":
            return Response(
                {"detail": "Только редакторы могут загружать фотографии"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if "photos" not in request.FILES:
            return Response(
                {"detail": "Файлы не переданы"}, status=status.HTTP_400_BAD_REQUEST
            )

        files = request.FILES.getlist("photos")
        uploaded_photos = []

        print(f"📸 Получено {len(files)} файлов для загрузки")

        for file in files:
            print(f"  - {file.name} ({file.size} байт, {file.content_type})")

            # Проверка размера
            if file.size > 10 * 1024 * 1024:
                print(f"  ⚠️ Файл {file.name} слишком большой, пропускаем")
                continue

            # Проверка типа
            allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
            if file.content_type not in allowed_types:
                print(
                    f"  ⚠️ Файл {file.name} имеет неподдерживаемый тип {file.content_type}, пропускаем"
                )
                continue

            photo = Photo.objects.create(
                album=album, image=file, caption=request.data.get("caption", "")
            )
            uploaded_photos.append(photo)
            print(f"  ✅ Загружено фото: {file.name}")

        print(f"📸 Успешно загружено {len(uploaded_photos)} фотографий")

        serializer = PhotoSerializer(
            uploaded_photos, many=True, context={"request": request}
        )

        return Response(
            {
                "detail": f"Загружено {len(uploaded_photos)} фотографий",
                "photos": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="photos/(?P<photo_id>[^/.]+)/view",
        permission_classes=[AllowAny],
    )
    def view_photo(self, request, pk=None, photo_id=None):
        """Увеличить количество просмотров фотографии"""
        album = self.get_object()
        photo = get_object_or_404(Photo, id=photo_id, album=album)

        photo.views += 1
        photo.save(update_fields=["views"])

        return Response(
            {"detail": "Просмотр засчитан", "views": photo.views},
            status=status.HTTP_200_OK,
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="photos/(?P<photo_id>[^/.]+)/like",
        permission_classes=[IsAuthenticated],
    )
    def like_photo(self, request, pk=None, photo_id=None):
        """Поставить/убрать лайк на фотографии"""
        album = self.get_object()
        photo = get_object_or_404(Photo, id=photo_id, album=album)

        existing_like = PhotoLike.objects.filter(photo=photo, user=request.user).first()

        if existing_like:
            existing_like.delete()
            photo.likes_count -= 1
            photo.save(update_fields=["likes_count"])
            return Response(
                {
                    "detail": "Лайк убран",
                    "action": "unliked",
                    "likes_count": photo.likes_count,
                    "photo_id": photo.id,
                },
                status=status.HTTP_200_OK,
            )
        else:
            PhotoLike.objects.create(photo=photo, user=request.user)
            photo.likes_count += 1
            photo.save(update_fields=["likes_count"])
            return Response(
                {
                    "detail": "Лайк поставлен",
                    "action": "liked",
                    "likes_count": photo.likes_count,
                    "photo_id": photo.id,
                },
                status=status.HTTP_201_CREATED,
            )

    @action(
        detail=True,
        methods=["delete"],
        url_path="photos/(?P<photo_id>[^/.]+)",
        permission_classes=[IsAuthenticated],
    )
    def delete_photo(self, request, pk=None, photo_id=None):
        """Удаление фотографии из альбома"""
        album = self.get_object()

        if request.user.role != "editor":
            return Response(
                {"detail": "Только редакторы могут удалять фотографии"},
                status=status.HTTP_403_FORBIDDEN,
            )

        photo = get_object_or_404(Photo, id=photo_id, album=album)
        photo.delete()

        return Response({"detail": "Фотография удалена"}, status=status.HTTP_200_OK)


class PhotoReorderView(generics.UpdateAPIView):
    """Обновление порядка фотографий"""

    permission_classes = [IsAuthenticated]

    def post(self, request, album_id):
        if request.user.role != "editor":
            return Response(
                {"detail": "Только редакторы могут изменять порядок"},
                status=status.HTTP_403_FORBIDDEN,
            )

        album = get_object_or_404(Album, id=album_id)
        photo_ids = request.data.get("photo_ids", [])

        for index, photo_id in enumerate(photo_ids):
            Photo.objects.filter(id=photo_id, album=album).update(order=index)

        return Response(
            {"detail": "Порядок фотографий обновлён"}, status=status.HTTP_200_OK
        )
