# backend/gallery/admin.py

from django.contrib import admin
from .models import Album, Photo, PhotoLike, PhotoComment


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ["image", "caption", "order"]
    ordering = ["order"]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "photos_count", "is_published", "created_at"]
    list_filter = ["is_published", "date"]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at", "updated_at"]
    inlines = [PhotoInline]
    fieldsets = (
        ("Основное", {"fields": ("title", "description", "date", "is_published")}),
        ("Обложка", {"fields": ("cover_image", "cover_image_url")}),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    def photos_count(self, obj):
        return obj.photos.count()

    photos_count.short_description = "Количество фото"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "album",
        "caption",
        "order",
        "views",
        "likes_count",
        "uploaded_at",
    ]
    list_filter = ["album", "uploaded_at"]
    search_fields = ["caption"]


@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    list_display = ["id", "photo", "user", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["user__username", "photo__id"]


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ["id", "photo", "user", "content", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["user__username", "content"]
