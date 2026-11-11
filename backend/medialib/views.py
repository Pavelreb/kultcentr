# backend/medialib/views.py

from rest_framework import filters, permissions, viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Audio, Video
from .serializers import AudioSerializer, VideoSerializer


class IsEditorOrReadOnly(permissions.BasePermission):
    """Чтение — всем, изменение — только редакторам"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == "editor"


class PublishedFilterMixin:
    """Не-редакторам показываем только опубликованные записи"""

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated and user.role == "editor":
            return queryset
        if self.action in ("list", "retrieve"):
            return queryset.filter(is_published=True)
        return queryset


class VideoViewSet(PublishedFilterMixin, viewsets.ModelViewSet):
    queryset = Video.objects.select_related("uploaded_by").all()
    serializer_class = VideoSerializer
    permission_classes = [IsEditorOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]


class AudioViewSet(PublishedFilterMixin, viewsets.ModelViewSet):
    queryset = Audio.objects.select_related("uploaded_by").all()
    serializer_class = AudioSerializer
    permission_classes = [IsEditorOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]
