# backend/about/serializers.py

from rest_framework import serializers
from .models import InstitutionInfo, StaffMember, Club, Achievement


class InstitutionInfoSerializer(serializers.ModelSerializer):
    logo_display = serializers.SerializerMethodField()
    background_display = serializers.SerializerMethodField()

    class Meta:
        model = InstitutionInfo
        fields = [
            "id",
            "name",
            "description",
            "logo",
            "logo_url",
            "logo_display",
            "background_image",
            "background_image_url",
            "background_display",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]

    def _abs(self, field):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(field.url)
        return field.url

    def get_logo_display(self, obj):
        if obj.logo:
            return self._abs(obj.logo)
        return obj.logo_url

    def get_background_display(self, obj):
        if obj.background_image:
            return self._abs(obj.background_image)
        return obj.background_image_url


class StaffMemberSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True
    )
    display_photo = serializers.SerializerMethodField()
    user_id = serializers.ReadOnlyField(source="user.id")
    user_username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = StaffMember
        fields = [
            "id",
            "user",
            "user_id",
            "user_username",
            "full_name",
            "position",
            "category",
            "category_display",
            "photo",
            "photo_url",
            "display_photo",
            "bio",
            "order",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def get_display_photo(self, obj):
        """Фото сотрудника: своё фото → аватар привязанного пользователя"""
        request = self.context.get("request")
        if obj.photo:
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        if obj.photo_url:
            return obj.photo_url
        if obj.user and obj.user.avatar:
            if request:
                return request.build_absolute_uri(obj.user.avatar.url)
            return obj.user.avatar.url
        return None


class ClubSerializer(serializers.ModelSerializer):
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = [
            "id",
            "title",
            "excerpt",
            "content",
            "image",
            "image_url",
            "display_image",
            "leader_name",
            "schedule",
            "age",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url


class AchievementSerializer(serializers.ModelSerializer):
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = [
            "id",
            "title",
            "excerpt",
            "content",
            "image",
            "image_url",
            "display_image",
            "date",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url
