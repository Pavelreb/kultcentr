from django.urls import path

from .views import (
    AssessmentListCreateView,
    AssessmentQuestionsView,
    FeedbackListCreateView,
)

urlpatterns = [
    path("feedback/", FeedbackListCreateView.as_view(), name="feedback"),
    path(
        "assessment/questions/",
        AssessmentQuestionsView.as_view(),
        name="assessment-questions",
    ),
    path("assessment/", AssessmentListCreateView.as_view(), name="assessment"),
]
