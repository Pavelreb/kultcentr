# backend/medialib/serializers.py

import os

from rest_framework import serializers

from .models import Audio, Video
from .utils import compress_video, convert_to_mp3, probe_duration, replace_file_field


class VideoSerializer(serializers.ModelSerializer):
    file_display = serializers.SerializerMethodField()
    thumbnail_display = serializers.SerializerMethodField()
    uploaded_by_username = serializers.ReadOnlyField(source="uploaded_by.username")

    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "description",
            "file",
            "video_url",
            "file_display",
            "thumbnail",
            "thumbnail_url",
            "thumbnail_display",
            "duration",
            "uploaded_by",
            "uploaded_by_username",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "duration", "uploaded_by", "created_at"]

    def _abs(self, field):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(field.url)
        return field.url

    def get_file_display(self, obj):
        if obj.file:
            return self._abs(obj.file)
        return obj.video_url

    def get_thumbnail_display(self, obj):
        if obj.thumbnail:
            return self._abs(obj.thumbnail)
        return obj.thumbnail_url

    def _process(self, instance):
        """Компрессия видео и извлечение длительности после загрузки файла."""
        if not instance.file:
            return
        path = instance.file.path
        instance.duration = probe_duration(path)
        compressed = compress_video(path)
        if compressed:
            replace_file_field(instance, compressed)
        instance.save(update_fields=["file", "duration"])

    def create(self, validated_data):
        validated_data["uploaded_by"] = self.context["request"].user
        instance = super().create(validated_data)
        self._process(instance)
        return instance

    def update(self, instance, validated_data):
        file_changed = "file" in validated_data and validated_data["file"]
        instance = super().update(instance, validated_data)
        if file_changed:
            self._process(instance)
        return instance


class AudioSerializer(serializers.ModelSerializer):
    file_display = serializers.SerializerMethodField()
    cover_display = serializers.SerializerMethodField()
    uploaded_by_username = serializers.ReadOnlyField(source="uploaded_by.username")

    class Meta:
        model = Audio
        fields = [
            "id",
            "title",
            "description",
            "file",
            "audio_url",
            "file_display",
            "cover",
            "cover_url",
            "cover_display",
            "duration",
            "uploaded_by",
            "uploaded_by_username",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "duration", "uploaded_by", "created_at"]

    def _abs(self, field):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(field.url)
        return field.url

    def get_file_display(self, obj):
        if obj.file:
            return self._abs(obj.file)
        return obj.audio_url

    def get_cover_display(self, obj):
        if obj.cover:
            return self._abs(obj.cover)
        return obj.cover_url

    def _process(self, instance):
        """Конвертация в MP3 и извлечение длительности после загрузки файла."""
        if not instance.file:
            return
        path = instance.file.path
        instance.duration = probe_duration(path)
        converted = convert_to_mp3(path)
        if converted:
            replace_file_field(instance, converted)
        instance.save(update_fields=["file", "duration"])

    def create(self, validated_data):
        validated_data["uploaded_by"] = self.context["request"].user
        instance = super().create(validated_data)
        self._process(instance)
        return instance

    def update(self, instance, validated_data):
        file_changed = "file" in validated_data and validated_data["file"]
        instance = super().update(instance, validated_data)
        if file_changed:
            self._process(instance)
        return instance
