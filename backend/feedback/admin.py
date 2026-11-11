from django.contrib import admin

from .models import AssessmentResponse, FeedbackMessage


@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "created_at"]
    search_fields = ["email", "full_name", "text"]


@admin.register(AssessmentResponse)
class AssessmentResponseAdmin(admin.ModelAdmin):
    list_display = ["email", "full_name", "created_at"]
    search_fields = ["email", "full_name", "text"]
