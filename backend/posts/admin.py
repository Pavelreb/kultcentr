from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "is_published"]
    list_filter = ["is_published", "created_at"]
    search_fields = ["title", "content"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (
            "Основное",
            {"fields": ("title", "content", "excerpt", "author", "is_published")},
        ),
        ("Изображение", {"fields": ("image_url",), "classes": ("collapse",)}),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
