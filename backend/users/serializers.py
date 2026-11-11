# backend/users/serializers.py

import os
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.db.models import Sum
from posts.models import Post  # ✅ Добавляем импорт для подсчёта постов
from likes.models import Like
from comments.models import Comment

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        label="Подтверждение пароля",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {"email": {"required": False, "allow_blank": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password2": "Пароли не совпадают!"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        if "email" not in validated_data or not validated_data.get("email"):
            validated_data["email"] = ""
        user = User.objects.create_user(**validated_data)
        user.role = "subscriber"
        user.is_active = True
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()
    subscribers_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    is_online = serializers.SerializerMethodField()
    total_views = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "birth_date",
            "bio",
            "date_joined",
            "role",
            "role_display",
            "full_name",
            "is_active",
            "avatar",
            "avatar_url",
            "posts_count",
            "subscribers_count",
            "is_subscribed",
            "is_online",
            "phone",
            "vk",
            "max",
            "ok",
            "rutube",
            "show_phone",
            "show_email",
            "show_socials",
            "total_views",
            "total_likes",
            "total_comments",
        ]
        read_only_fields = ["id", "username", "date_joined", "role", "role_display"]

    def to_representation(self, instance):
        """Приватность: для чужих пользователей скрываем данные по настройкам"""
        data = super().to_representation(instance)

        request = self.context.get("request")
        is_self_or_editor = (
            request
            and request.user.is_authenticated
            and (request.user.id == instance.id or request.user.role == "editor")
        )

        if not is_self_or_editor:
            # Email показываем публично только с разрешения пользователя
            if not instance.show_email:
                data["email"] = None
            if not instance.show_phone:
                data["phone"] = None
            if not instance.show_socials:
                data["vk"] = None
                data["max"] = None
                data["ok"] = None
                data["rutube"] = None

        return data

    def get_role_display(self, obj):
        return obj.get_role_display()

    def get_full_name(self, obj):
        parts = []
        if obj.last_name:
            parts.append(obj.last_name)
        if obj.first_name:
            parts.append(obj.first_name)
        if obj.patronymic:
            parts.append(obj.patronymic)
        return " ".join(parts) if parts else obj.username

    def get_avatar_url(self, obj):
        if obj.avatar:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None

    def get_posts_count(self, obj):
        """Количество опубликованных постов автора"""
        return Post.objects.filter(author=obj, is_published=True).count()

    def get_subscribers_count(self, obj):
        """Количество подписчиков"""
        return obj.subscribers.count()

    def get_is_subscribed(self, obj):
        """Подписан ли текущий пользователь на этого автора"""
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.subscribers.filter(subscriber=request.user).exists()

    def get_is_online(self, obj):
        """Пользователь в сети (активен в последние 5 минут)"""
        return obj.is_online

    def get_total_views(self, obj):
        """Суммарные просмотры опубликованных постов пользователя"""
        return (
            Post.objects.filter(author=obj, is_published=True).aggregate(
                total=Sum("views")
            )["total"]
            or 0
        )

    def get_total_likes(self, obj):
        """Лайки на опубликованных постах пользователя"""
        return Like.objects.filter(post__author=obj, post__is_published=True).count()

    def get_total_comments(self, obj):
        """Комментарии к опубликованным постам пользователя"""
        return Comment.objects.filter(
            post__author=obj, post__is_published=True
        ).count()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "patronymic",
            "birth_date",
            "bio",
            "avatar",
            "phone",
            "vk",
            "max",
            "ok",
            "rutube",
            "show_phone",
            "show_email",
            "show_socials",
        ]

    def update(self, instance, validated_data):
        new_avatar = validated_data.get("avatar", None)

        if new_avatar and instance.avatar:
            old_avatar_path = instance.avatar.path
            if os.path.isfile(old_avatar_path):
                os.remove(old_avatar_path)
                print(f"🗑️ Старый аватар удалён: {old_avatar_path}")

        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.patronymic = validated_data.get("patronymic", instance.patronymic)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.bio = validated_data.get("bio", instance.bio)
        instance.avatar = validated_data.get("avatar", instance.avatar)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.vk = validated_data.get("vk", instance.vk)
        instance.max = validated_data.get("max", instance.max)
        instance.ok = validated_data.get("ok", instance.ok)
        instance.rutube = validated_data.get("rutube", instance.rutube)
        instance.show_phone = validated_data.get("show_phone", instance.show_phone)
        instance.show_email = validated_data.get("show_email", instance.show_email)
        instance.show_socials = validated_data.get(
            "show_socials", instance.show_socials
        )
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        required=True, write_only=True, validators=[validate_password]
    )
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError({"new_password2": "Пароли не совпадают!"})
        return attrs


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)

    def validate(self, attrs):
        email = attrs.get("email")
        username = attrs.get("username")

        if not email and not username:
            raise serializers.ValidationError("Укажите email или имя пользователя")

        user = None
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass

        if not user and username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                pass

        if not user:
            raise serializers.ValidationError("Пользователь с такими данными не найден")

        attrs["user"] = user
        return attrs


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        required=True, write_only=True, validators=[validate_password]
    )
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError({"new_password2": "Пароли не совпадают!"})
        return attrs
