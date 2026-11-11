from django.contrib import admin

from .models import Audio, Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "duration", "uploaded_by", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title", "description")


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "duration", "uploaded_by", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title", "description")
