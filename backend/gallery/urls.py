from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, PhotoReorderView
from .comment_views import PhotoCommentViewSet

# Используем другое имя для комментариев к фото, чтобы не конфликтовать
router = DefaultRouter()
router.register(r"photo-comments", PhotoCommentViewSet, basename="photo-comment")
router.register(r"albums", AlbumViewSet, basename="album")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "albums/<int:album_id>/reorder/",
        PhotoReorderView.as_view(),
        name="photo-reorder",
    ),
]
