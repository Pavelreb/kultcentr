from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_active", "has_background", "updated_at"]
    list_filter = ["is_active", "updated_at"]
    fieldsets = (
        ("Основное", {"fields": ("title", "subtitle", "is_active")}),
        ("Изображение", {"fields": ("background_image", "background_image_url")}),
        ("Кнопка", {"fields": ("button_text", "button_link")}),
        ("Дата обновления", {"fields": ("updated_at",), "classes": ("collapse",)}),
    )
    readonly_fields = ["updated_at"]

    def has_background(self, obj):
        return bool(obj.background_image or obj.background_image_url)

    has_background.boolean = True
    has_background.short_description = "Есть изображение"
