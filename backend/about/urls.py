from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InstitutionInfoView,
    InstitutionInfoUpdateView,
    StaffMemberViewSet,
    ClubViewSet,
    AchievementViewSet,
    DocumentViewSet,
)

router = DefaultRouter()
router.register("staff", StaffMemberViewSet, basename="staff")
router.register("clubs", ClubViewSet, basename="clubs")
router.register("achievements", AchievementViewSet, basename="achievements")
router.register("documents", DocumentViewSet, basename="documents")

urlpatterns = [
    path("info/", InstitutionInfoView.as_view(), name="institution_info"),
    path(
        "info/update/",
        InstitutionInfoUpdateView.as_view(),
        name="institution_info_update",
    ),
    path("", include(router.urls)),
]
