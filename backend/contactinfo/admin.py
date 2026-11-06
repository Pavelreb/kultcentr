from django.contrib import admin
from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ["address", "phone", "email", "updated_at"]
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("address", "phone", "email", "work_hours", "description")},
        ),
        ("Социальные сети", {"fields": ("instagram", "vk", "telegram")}),
        ("Дата обновления", {"fields": ("updated_at",), "classes": ("collapse",)}),
    )
    readonly_fields = ["updated_at"]
