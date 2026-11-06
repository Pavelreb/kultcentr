from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение:
    - Читать могут все
    - Редактировать может только автор комментария
    - Удалять может автор комментария, автор поста или редактор
    """

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user

        # Редактирование (PUT/PATCH) — только автор комментария
        if request.method in ["PUT", "PATCH"]:
            return obj.author == user

        # Удаление (DELETE) — автор комментария, автор поста или редактор
        if request.method == "DELETE":
            # Автор комментария
            if obj.author == user:
                return True
            # Автор поста
            if obj.post.author == user:
                return True
            # Главный редактор
            if user.role == "editor":
                return True
            return False

        return False


class CanCommentPermission(permissions.BasePermission):
    """
    Разрешение: только авторизованные пользователи могут комментировать
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated
        return True
