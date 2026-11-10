from django.contrib import admin
from .models import InstitutionInfo, StaffMember, Club, Achievement


@admin.register(InstitutionInfo)
class InstitutionInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "updated_at")


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "category", "order", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("full_name", "position")


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("title", "leader_name", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title",)
