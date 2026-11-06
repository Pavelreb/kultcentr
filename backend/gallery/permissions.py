from rest_framework import permissions


class IsEditorOrReadOnly(permissions.BasePermission):
    """Разрешение: только чтение для всех, запись только для редакторов"""

    def has_permission(self, request, view):
        # GET запросы разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # POST, PUT, DELETE только для редакторов
        return request.user.is_authenticated and request.user.role == "editor"

    def has_object_permission(self, request, view, obj):
        # GET запросы разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # PUT, DELETE только для редакторов
        return request.user.is_authenticated and request.user.role == "editor"
