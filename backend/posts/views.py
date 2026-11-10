from rest_framework import viewsets, permissions, status, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from urllib.parse import unquote
import os
from django.db import models
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrEditorOrReadOnly, IsAuthorUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrEditorOrReadOnly,
        IsAuthorUser,
    ]
    # Поиск: /api/posts/?search=текст
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content", "excerpt"]

    def get_queryset(self):
        user = self.request.user

        queryset = Post.objects.all()
        author_name = self.request.query_params.get("author_name")

        if author_name:
            queryset = queryset.filter(author__username=author_name)
            if user.is_authenticated:
                if user.username == author_name or user.role == "editor":
                    return queryset
            return queryset.filter(is_published=True)

        if self.action == "list":
            return queryset.filter(is_published=True)

        return queryset

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])

        if post.is_published:
            post.views += 1
            post.save(update_fields=["views"])
            serializer = self.get_serializer(post)
            return Response(serializer.data)

        user = request.user
        if user.is_authenticated and (post.author == user or user.role == "editor"):
            post.views += 1
            post.save(update_fields=["views"])
            serializer = self.get_serializer(post)
            return Response(serializer.data)

        return Response({"detail": "Пост не найден"}, status=404)

    def update(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        user = request.user

        if post.is_published:
            if post.author != user and user.role != "editor":
                return Response({"detail": "Недостаточно прав"}, status=403)
        else:
            if post.author != user and user.role != "editor":
                return Response({"detail": "Недостаточно прав"}, status=403)

        old_post = Post.objects.get(pk=kwargs["pk"])
        old_image_url = old_post.image_url
        old_image = old_post.image

        print("=" * 60)
        print(f"🔍 Обновляем пост: {post.title}")
        print(f"🔍 Старое изображение URL: {old_image_url}")
        print(f"🔍 Старое изображение файл: {old_image}")

        response = super().update(request, *args, **kwargs)

        post.refresh_from_db()

        new_image_url = post.image_url
        new_image = post.image

        print(f"🔍 Новое изображение URL: {new_image_url}")
        print(f"🔍 Новое изображение файл: {new_image}")

        if old_image_url and old_image_url != new_image_url:
            print(f"🔍 Изображение изменилось, удаляем старое: {old_image_url}")

            if "/media/" in old_image_url:
                filename = old_image_url.split("/media/")[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f"🔍 Путь к старому файлу: {file_path}")

                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f"✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}")
                    except Exception as e:
                        print(f"❌ Ошибка удаления: {e}")
                else:
                    print(f"⚠️ Старый файл не найден: {file_path}")

        if old_image and old_image != new_image:
            file_path = old_image.path
            print(f"🔍 Удаляем старый файл image: {file_path}")
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")

        print("=" * 60)

        return response

    def perform_destroy(self, instance):
        print("=" * 60)
        print(f"🔍 Удаляем пост: {instance.title}")
        print(f"🔍 ID поста: {instance.id}")

        if instance.image:
            print(f"🔍 Поле image: {instance.image.name}")
            file_path = instance.image.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"✅ Изображение УСПЕШНО УДАЛЕНО: {file_path}")
                except Exception as e:
                    print(f"❌ Ошибка удаления: {e}")
        else:
            print("🔍 У поста нет image (загружено через ссылку)")

        if instance.image_url:
            print(f"🔍 image_url: {instance.image_url}")

            if "/media/" in instance.image_url:
                filename = instance.image_url.split("/media/")[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f"🔍 Декодированное имя: {filename}")
                print(f"🔍 Полный путь: {file_path}")

                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f"✅ Изображение по URL УСПЕШНО УДАЛЕНО: {file_path}")
                    except Exception as e:
                        print(f"❌ Ошибка удаления: {e}")
                else:
                    print(f"⚠️ Файл не найден: {file_path}")

        print("=" * 60)
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["post"], url_path="feature")
    def feature(self, request, pk=None):
        """Назначить пост главной публикацией (только редактор)"""
        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        post = get_object_or_404(Post, pk=pk)
        if not post.is_published:
            return Response(
                {"detail": "Главной может быть только опубликованная публикация"},
                status=400,
            )

        Post.objects.filter(is_featured=True).exclude(pk=post.pk).update(
            is_featured=False
        )
        post.is_featured = True
        post.save(update_fields=["is_featured"])
        return Response(self.get_serializer(post).data)

    @action(detail=False, methods=["post"], url_path="unfeature")
    def unfeature(self, request):
        """Сбросить главную публикацию — выбор станет автоматическим"""
        user = request.user
        if not user.is_authenticated or user.role != "editor":
            return Response({"detail": "Недостаточно прав"}, status=403)

        Post.objects.filter(is_featured=True).update(is_featured=False)
        return Response({"detail": "Главная публикация сброшена"})

    @action(detail=False, methods=["get"], url_path="my_posts")
    def my_posts(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Не авторизован"}, status=401)

        posts = Post.objects.filter(author=user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["post"],
        url_path="upload-image",
        parser_classes=[MultiPartParser, FormParser],
    )
    def upload_image(self, request):
        user = request.user

        if not user.is_authenticated or (user.role not in ["author", "editor"]):
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

        filename = f"posts/{user.id}_{file.name}"
        file_path = default_storage.save(filename, ContentFile(file.read()))
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)

        print(f"📁 Загружено изображение для поста: {file_path}")
        print(f"📁 URL: {file_url}")

        return Response(
            {"image_url": file_url, "detail": "Изображение загружено"},
            status=status.HTTP_200_OK,
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
