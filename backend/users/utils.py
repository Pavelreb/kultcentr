from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings


def send_password_reset_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    frontend_url = "http://localhost:3000"
    reset_url = f"{frontend_url}/reset-password/{uid}/{token}/"

    subject = "Сброс пароля на сайте Центр Культуры"
    message = f"""
Здравствуйте, {user.username}!

Вы запросили сброс пароля на сайте "Центр Культуры".

Для создания нового пароля, пожалуйста, перейдите по ссылке:
{reset_url}

Если вы не запрашивали сброс пароля, просто проигнорируйте это письмо.

С уважением,
Команда Центр Культуры
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )

    print("=" * 60)
    print("📧 ПИСЬМО ДЛЯ СБРОСА ПАРОЛЯ ОТПРАВЛЕНО")
    print(f"📤 Кому: {user.email}")
    print(f"🔗 Ссылка: {reset_url}")
    print("=" * 60)
