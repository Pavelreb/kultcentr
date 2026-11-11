from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication


class LastActivityMiddleware:
    """Обновляет last_activity авторизованного пользователя (не чаще раза в минуту).
    JWT-аутентификацию DRF делает во view, поэтому токен проверяем здесь вручную."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        user = getattr(request, "user", None)

        # Для API-запросов request.user здесь ещё анонимный — пробуем JWT
        if not (user and user.is_authenticated):
            try:
                result = self.jwt_auth.authenticate(request)
                if result:
                    user = result[0]
            except Exception:
                pass

        if user and user.is_authenticated:
            now = timezone.now()
            if (
                not user.last_activity
                or (now - user.last_activity).total_seconds() > 60
            ):
                # update() без сигналов, чтобы не дёргать лишнее
                type(user).objects.filter(pk=user.pk).update(last_activity=now)
                user.last_activity = now

        return self.get_response(request)
