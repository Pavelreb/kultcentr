# backend/comments/serializers.py

from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_name = serializers.ReadOnlyField(source="author.username")
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author_id",
            "author_name",
            "author_first_name",  # ✅ НОВОЕ ПОЛЕ
            "author_last_name",  # ✅ НОВОЕ ПОЛЕ
            "author_full_name",  # ✅ НОВОЕ ПОЛЕ
            "author_avatar",
            "content",
            "created_at",
            "updated_at",
            "parent",
            "replies",
            "can_edit",
            "can_delete",
            "likes_count",
            "user_has_liked",
        ]
        read_only_fields = ["author", "post"]

    def validate(self, data):
        parent = data.get("parent")
        post = data.get("post")
        if parent and post:
            if parent.post_id != post.id:
                raise serializers.ValidationError(
                    "Родительский комментарий должен принадлежать тому же посту"
                )
        return data

    def update(self, instance, validated_data):
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance

    def get_replies(self, obj):
        if obj.replies.exists():
            context = {"request": self.context.get("request")}
            return CommentSerializer(obj.replies.all(), many=True, context=context).data
        return []

    def get_can_edit(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.author == request.user

    def get_can_delete(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False

        user = request.user

        if obj.author == user:
            return True

        if obj.post.author == user:
            return True

        if user.role == "editor":
            return True

        return False

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

    def get_author_full_name(self, obj):
        """Возвращает полное имя автора комментария"""
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        return " ".join(parts) if parts else obj.author.username


class CommentForPostSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.id")
    author_name = serializers.ReadOnlyField(source="author.username")
    author_first_name = serializers.CharField(
        source="author.first_name", read_only=True
    )
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "author_id",
            "author_name",
            "author_first_name",  # ✅ НОВОЕ ПОЛЕ
            "author_last_name",  # ✅ НОВОЕ ПОЛЕ
            "author_full_name",  # ✅ НОВОЕ ПОЛЕ
            "author_avatar",
            "content",
            "created_at",
            "updated_at",
            "parent",
            "replies",
            "can_edit",
            "can_delete",
            "likes_count",
            "user_has_liked",
        ]

    def get_replies(self, obj):
        if obj.replies.exists():
            context = {"request": self.context.get("request")}
            return CommentForPostSerializer(
                obj.replies.all(), many=True, context=context
            ).data
        return []

    def get_can_edit(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.author == request.user

    def get_can_delete(self, obj):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False

        user = request.user

        if obj.author == user:
            return True

        if obj.post.author == user:
            return True

        if user.role == "editor":
            return True

        return False

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

    def get_author_full_name(self, obj):
        """Возвращает полное имя автора комментария"""
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        return " ".join(parts) if parts else obj.author.username
