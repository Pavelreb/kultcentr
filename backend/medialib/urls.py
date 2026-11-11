from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AudioViewSet, VideoViewSet

router = DefaultRouter()
router.register("videos", VideoViewSet, basename="medialib-videos")
router.register("audio", AudioViewSet, basename="medialib-audio")

urlpatterns = [
    path("", include(router.urls)),
]
