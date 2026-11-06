from rest_framework import permissions


class IsEditorOrReadOnly(permissions.BasePermission):
    """
    Разрешение:
    - Читать могут все
    - Создавать, редактировать, удалять может только Главный редактор (role='editor')
    """

    def has_permission(self, request, view):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Создание (POST) — только редактор
        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == "editor"

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редактирование/удаление — только редактор
        return request.user.is_authenticated and request.user.role == "editor"
