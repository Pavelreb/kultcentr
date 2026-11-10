# backend/about/views.py

from rest_framework import viewsets, generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import InstitutionInfo, StaffMember, Club, Achievement
from .serializers import (
    InstitutionInfoSerializer,
    StaffMemberSerializer,
    ClubSerializer,
    AchievementSerializer,
)


class IsEditorOrReadOnly(permissions.BasePermission):
    """Чтение — всем, изменение — только редакторам"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated and request.user.role == "editor"
        )


class InstitutionInfoView(generics.RetrieveAPIView):
    """Получение общей информации (всем)"""

    permission_classes = [permissions.AllowAny]
    serializer_class = InstitutionInfoSerializer

    def get_object(self):
        obj = InstitutionInfo.objects.first()
        if obj is None:
            obj = InstitutionInfo.objects.create()
        return obj


class InstitutionInfoUpdateView(generics.UpdateAPIView):
    """Обновление общей информации (только редакторы)"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InstitutionInfoSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        obj = InstitutionInfo.objects.first()
        if obj is None:
            obj = InstitutionInfo.objects.create()
        return obj

    def update(self, request, *args, **kwargs):
        if request.user.role != "editor":
            return Response(
                {"detail": "Только главные редакторы могут редактировать информацию"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)


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


class StaffMemberViewSet(PublishedFilterMixin, viewsets.ModelViewSet):
    queryset = StaffMember.objects.select_related("user").all()
    serializer_class = StaffMemberSerializer
    permission_classes = [IsEditorOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["full_name", "position", "bio"]


class ClubViewSet(PublishedFilterMixin, viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsEditorOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "excerpt", "content", "leader_name"]


class AchievementViewSet(PublishedFilterMixin, viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsEditorOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "excerpt", "content"]
