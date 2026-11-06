# backend/users/serializers.py

import os
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from posts.models import Post  # ✅ Добавляем импорт для подсчёта постов

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
    posts_count = serializers.SerializerMethodField()  # ✅ НОВОЕ ПОЛЕ
    subscribers_count = serializers.SerializerMethodField()  # ✅ НОВОЕ ПОЛЕ (заглушка)

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
            "subscribers_count",  # ✅ ДОБАВЛЯЕМ
        ]
        read_only_fields = ["id", "username", "date_joined", "role", "role_display"]

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
        """Количество подписчиков (заглушка, можно реализовать позже)"""
        # TODO: Добавить модель подписок
        return 0


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
