# backend/posts/serializers.py

from rest_framework import serializers
from .models import Post
from comments.serializers import CommentForPostSerializer


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.username", read_only=True)
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_role = serializers.CharField(source="author.role", read_only=True)
    author_avatar = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    user_has_liked = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "image",
            "image_url",
            "display_image",
            "author_name",
            "author_first_name",  # ✅ НОВОЕ ПОЛЕ
            "author_last_name",  # ✅ НОВОЕ ПОЛЕ
            "author_full_name",  # ✅ НОВОЕ ПОЛЕ
            "author_role",
            "author_avatar",
            "created_at",
            "updated_at",
            "is_published",
            "excerpt",
            "is_featured",
            "comments",
            "likes_count",
            "user_has_liked",
            "views",
        ]
        read_only_fields = [
            "author",
            "author_name",
            "author_first_name",
            "author_last_name",
            "author_full_name",
            "author_role",
            "author_avatar",
            "created_at",
            "updated_at",
            "views",
            "is_featured",
        ]

    def get_comments(self, obj):
        top_level_comments = obj.comments.filter(parent__isnull=True)
        context = {"request": self.context.get("request")}
        return CommentForPostSerializer(
            top_level_comments, many=True, context=context
        ).data

    def get_user_has_liked(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()

    def get_author_avatar(self, obj):
        if obj.author.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.author.avatar.url)
            return obj.author.avatar.url
        return None

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url

    def get_author_full_name(self, obj):
        """Возвращает полное имя автора (Фамилия Имя Отчество)"""
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        if obj.author.patronymic:
            parts.append(obj.author.patronymic)
        return " ".join(parts) if parts else obj.author.username

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)
