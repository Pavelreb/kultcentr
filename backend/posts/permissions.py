from rest_framework import permissions


class IsAuthorOrEditorOrReadOnly(permissions.BasePermission):
    """
    Разрешение:
    - Читать могут все
    - Редактировать/удалять может автор или главный редактор
    """

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Голосование и прохождение теста — любому авторизованному пользователю
        if getattr(view, "action", None) in ("poll_vote", "quiz_submit"):
            return request.user.is_authenticated

        # Редактирование/удаление разрешено автору или редактору
        return obj.author == request.user or request.user.role == "editor"


class IsAuthorUser(permissions.BasePermission):
    """
    Разрешение: только пользователи с ролью 'author' или 'editor' могут создавать посты.
    Остальные POST-действия (голосование, прохождение теста, лайк) доступны
    любому авторизованному пользователю.
    """

    def has_permission(self, request, view):
        # Ограничиваем только создание поста
        if getattr(view, "action", None) == "create":
            return request.user.is_authenticated and request.user.role in [
                "author",
                "editor",
            ]
        return True
