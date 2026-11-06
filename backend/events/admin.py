from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "event_date", "location", "is_published"]
    list_filter = ["is_published", "event_date", "location"]
    search_fields = ["title", "content", "location"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = (
        (
            "Основное",
            {"fields": ("title", "content", "excerpt", "author", "is_published")},
        ),
        (
            "Детали события",
            {"fields": ("event_date", "location", "price", "image_url")},
        ),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
