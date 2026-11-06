# ПОЛНЫЙ ПРОМТ ПРОЕКТА "ЦЕНТР КУЛЬТУРЫ"

## ОПИСАНИЕ ПРОЕКТА

Сайт "Центр Культуры" — полноценное веб-приложение для публикации статей, новостей, анонсов мероприятий и культурных событий. Платформа с системой ролей, где авторы могут делиться публикациями, пользователи — комментировать, а редакторы — управлять контентом.

---

## СТЕК ТЕХНОЛОГИЙ

### Бэкенд:
- Python 3.13
- Django 6.0.7
- Django REST Framework
- djangorestframework-simplejwt (JWT)
- django-cors-headers
- Pillow
- SQLite

### Фронтенд:
- Nuxt 4.4.8 (Vue 3)
- Tailwind CSS
- Pinia

---

## СТРУКТУРА ПРОЕКТА

```
kultcentr/
├── backend/
│   ├── config/
│   │   ├── settings.py
│   │   └── urls.py
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── utils.py
│   ├── posts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── comments/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── events/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── likes/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── contactinfo/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── manage.py
│   └── db.sqlite3
├── frontend/
│   ├── pages/
│   │   ├── index.vue
│   │   ├── profile.vue
│   │   ├── contacts/
│   │   │   ├── index.vue
│   │   │   └── edit.vue
│   │   ├── auth/
│   │   │   ├── login.vue
│   │   │   └── register.vue
│   │   ├── posts/
│   │   │   ├── index.vue
│   │   │   ├── create.vue
│   │   │   ├── [id].vue
│   │   │   └── edit-[id].vue
│   │   ├── events/
│   │   │   ├── index.vue
│   │   │   ├── create.vue
│   │   │   ├── [id].vue
│   │   │   └── edit-[id].vue
│   │   └── authors/
│   │       ├── index.vue
│   │       └── [id].vue
│   ├── components/
│   │   ├── CommentItem.vue
│   │   └── LikeButton.vue
│   ├── store/
│   │   ├── auth.js
│   │   └── theme.js
│   ├── middleware/
│   │   └── auth.js
│   ├── assets/
│   │   └── css/
│   │       └── main.css
│   ├── app.vue
│   ├── nuxt.config.ts
│   └── tailwind.config.js
└── venv/
```

---

## ПОЛНЫЙ ФУНКЦИОНАЛ

### 👤 Пользователи и роли

| Роль | Что может |
|------|-----------|
| **Гость** | Смотреть посты, события, авторов, контакты |
| **Подписчик** | Смотреть + комментировать + редактировать профиль |
| **Автор** | Всё, что подписчик + создавать/редактировать/удалять свои посты + удалять комментарии под своими постами |
| **Главный редактор** | Всё, что автор + редактировать/удалять любые посты и события + создавать события + удалять любые комментарии + редактировать контакты |
| **Админ** | Всё (доступ в админку) |

---

### 📝 Посты
- CRUD
- Изображения (файл или ссылка)
- Черновики
- Лайки
- Комментарии
- Просмотры
- Автоудаление файлов

### 🎭 Афиша (События)
- CRUD (только редакторы)
- Изображения (файл или ссылка)
- Черновики
- Сортировка по дате (ближайшие первыми)
- Автоудаление файлов

### 💬 Комментарии
- Создание (только авторизованные)
- Редактирование (только свои)
- Удаление (свои, автор поста, редактор)
- Вложенность
- Лайки
- Аватарки авторов

### ❤️ Лайки
- На посты и комментарии
- Только авторизованные

### 👤 Профиль
- ФИО, дата рождения, аватарка
- Смена пароля
- Мои посты, Мои афиши, Мои комментарии

### 📞 Контакты
- Страница `/contacts` (доступна всем)
- Редактирование `/contacts/edit` (только редакторы)
- Данные в footer

### ✍️ Авторы
- Блок на главной
- Страница всех авторов
- Страница автора с публикациями

### 🎨 Дизайн
- Адаптив
- Тёмная тема
- Hero-баннер
- Семантические теги (header, main, footer)

### 📧 Восстановление пароля
- Через email (локально — вывод в терминал)

---

## ПОЛЬЗОВАТЕЛИ ДЛЯ ТЕСТИРОВАНИЯ

| Имя | Пароль | Роль |
|-----|--------|------|
| `admin` | `Admin123!` | Суперпользователь |
| `editor_user` | `EditorPass123!` | Главный редактор |
| `editor1` | `Editor123!` | Главный редактор |
| `author_user` | `AuthorPass123!` | Автор |
| `author1`-`author6` | `Author123!` | Автор |
| `user_user` | `UserPass123!` | Подписчик |
| `subscriber1`-`subscriber7` | `Sub123!` | Подписчик |

---

## ПОЛНЫЕ ФАЙЛЫ БЭКЕНДА

### `backend/config/settings.py`

```python
from pathlib import Path
from datetime import timedelta
import os

AUTH_USER_MODEL = 'users.User'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-btk8jqm6*+31(3i&h9u10fckd-39pw1*$h00le(wbktk^=k=4y"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "users",
    "posts",
    "comments",
    "events",
    "likes",
    "contactinfo",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@kultcentr.local'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

### `backend/config/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('events.urls')),
    path('api/', include('likes.urls')),
    path('api/auth/', include('users.urls')),
    path('api/contact-info/', include('contactinfo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### `backend/users/models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('subscriber', 'Подписчик'),
        ('author', 'Автор'),
        ('editor', 'Главный редактор'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='subscriber',
        verbose_name='Роль'
    )
    
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    
    patronymic = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Отчество'
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
```

---

### `backend/users/views.py`

```python
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegisterSerializer, UserSerializer, UserUpdateSerializer,
    ChangePasswordSerializer, PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)
from .utils import send_password_reset_email

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True, role='subscriber')
        print(f'✅ Пользователь {user.username} зарегистрирован')


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class CurrentUserView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CurrentUserUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        context = {'request': request}
        user_serializer = UserSerializer(instance, context=context)
        return Response(user_serializer.data)


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        old_password = serializer.validated_data.get('old_password')
        new_password = serializer.validated_data.get('new_password')
        
        if not user.check_password(old_password):
            return Response(
                {'old_password': 'Неверный текущий пароль'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(new_password)
        user.save()
        
        return Response(
            {'detail': 'Пароль успешно изменён!'},
            status=status.HTTP_200_OK
        )


class PasswordResetRequestView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        send_password_reset_email(user, request)
        
        return Response(
            {'detail': 'Ссылка для сброса пароля отправлена на email'},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, uidb64, token):
        from django.utils.http import urlsafe_base64_decode
        from django.contrib.auth.tokens import default_token_generator
        
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            return Response(
                {'detail': 'Неверная ссылка для сброса пароля'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not default_token_generator.check_token(user, token):
            return Response(
                {'detail': 'Неверный или просроченный токен'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        new_password = serializer.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        
        return Response(
            {'detail': 'Пароль успешно изменён!'},
            status=status.HTTP_200_OK
        )
```

---

### `backend/users/serializers.py`

```python
import os
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        label="Подтверждение пароля"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'email': {'required': False, 'allow_blank': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password2": "Пароли не совпадают!"}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        if 'email' not in validated_data or not validated_data.get('email'):
            validated_data['email'] = ''
        user = User.objects.create_user(**validated_data)
        user.role = 'subscriber'
        user.is_active = True
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'patronymic', 'birth_date', 'bio', 'date_joined', 
            'role', 'role_display', 'full_name', 'is_active',
            'avatar', 'avatar_url'
        ]
        read_only_fields = ['id', 'username', 'date_joined', 'role', 'role_display']

    def get_role_display(self, obj):
        return obj.get_role_display()

    def get_full_name(self, obj):
        parts = []
        if obj.last_name:
            parts.append(obj.last_name)
        if obj.first_name:
            parts.append(obj.first_name)
        if obj.patronymic:
            parts.append(obj.patronymic)
        return ' '.join(parts) if parts else obj.username

    def get_avatar_url(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'patronymic', 'birth_date', 'bio', 'avatar']

    def update(self, instance, validated_data):
        new_avatar = validated_data.get('avatar', None)
        
        if new_avatar and instance.avatar:
            old_avatar_path = instance.avatar.path
            if os.path.isfile(old_avatar_path):
                os.remove(old_avatar_path)
                print(f'🗑️ Старый аватар удалён: {old_avatar_path}')
        
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError(
                {"new_password2": "Пароли не совпадают!"}
            )
        return attrs


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)

    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')
        
        if not email and not username:
            raise serializers.ValidationError(
                "Укажите email или имя пользователя"
            )
        
        user = None
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
        
        if not user and username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                pass
        
        if not user:
            raise serializers.ValidationError(
                "Пользователь с такими данными не найден"
            )
        
        attrs['user'] = user
        return attrs


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    new_password2 = serializers.CharField(
        required=True,
        write_only=True
    )

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError(
                {"new_password2": "Пароли не совпадают!"}
            )
        return attrs
```

---

### `backend/users/urls.py`

```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterView, UserDetailView, UserListView, 
    CurrentUserView, CurrentUserUpdateView, ChangePasswordView,
    PasswordResetRequestView, PasswordResetConfirmView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/me/', CurrentUserView.as_view(), name='current_user'),
    path('users/me/update/', CurrentUserUpdateView.as_view(), name='current_user_update'),
    path('users/me/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('password-reset/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
```

---

### `backend/users/admin.py`

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Личная информация', {
            'fields': ('patronymic', 'birth_date', 'bio', 'avatar')
        }),
        ('Роль', {
            'fields': ('role',)
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Личная информация', {
            'fields': ('patronymic', 'birth_date', 'bio', 'avatar')
        }),
        ('Роль', {
            'fields': ('role',)
        }),
    )
```

---

### `backend/users/utils.py`

```python
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings


def send_password_reset_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    
    frontend_url = 'http://localhost:3000'
    reset_url = f'{frontend_url}/reset-password/{uid}/{token}/'
    
    subject = 'Сброс пароля на сайте Центр Культуры'
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
    
    print('=' * 60)
    print('📧 ПИСЬМО ДЛЯ СБРОСА ПАРОЛЯ ОТПРАВЛЕНО')
    print(f'📤 Кому: {user.email}')
    print(f'🔗 Ссылка: {reset_url}')
    print('=' * 60)
```

---

### `backend/posts/models.py`

```python
from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )
    excerpt = models.TextField(
        blank=True,
        null=True,
        verbose_name="Краткое описание"
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name="Изображение (файл)"
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на изображение"
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Просмотры"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']
```

---

### `backend/posts/views.py`

```python
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from urllib.parse import unquote
import os
from django.db import models
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrEditorOrReadOnly, IsAuthorUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrEditorOrReadOnly, IsAuthorUser]

    def get_queryset(self):
        user = self.request.user
        
        queryset = Post.objects.all()
        author_name = self.request.query_params.get('author_name')
        
        if author_name:
            queryset = queryset.filter(author__username=author_name)
            if user.is_authenticated:
                if user.username == author_name or user.role == 'editor':
                    return queryset
            return queryset.filter(is_published=True)
        
        if self.action == 'list':
            return queryset.filter(is_published=True)
        
        return queryset

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        
        if post.is_published:
            post.views += 1
            post.save(update_fields=['views'])
            serializer = self.get_serializer(post)
            return Response(serializer.data)
        
        user = request.user
        if user.is_authenticated and (post.author == user or user.role == 'editor'):
            post.views += 1
            post.save(update_fields=['views'])
            serializer = self.get_serializer(post)
            return Response(serializer.data)
        
        return Response({'detail': 'Пост не найден'}, status=404)

    def update(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        user = request.user
        
        if post.is_published:
            if post.author != user and user.role != 'editor':
                return Response({'detail': 'Недостаточно прав'}, status=403)
        else:
            if post.author != user and user.role != 'editor':
                return Response({'detail': 'Недостаточно прав'}, status=403)
        
        old_post = Post.objects.get(pk=kwargs['pk'])
        old_image_url = old_post.image_url
        old_image = old_post.image
        
        print('=' * 60)
        print(f'🔍 Обновляем пост: {post.title}')
        print(f'🔍 Старое изображение URL: {old_image_url}')
        print(f'🔍 Старое изображение файл: {old_image}')
        
        response = super().update(request, *args, **kwargs)
        
        post.refresh_from_db()
        
        new_image_url = post.image_url
        new_image = post.image
        
        print(f'🔍 Новое изображение URL: {new_image_url}')
        print(f'🔍 Новое изображение файл: {new_image}')
        
        if old_image_url and old_image_url != new_image_url:
            print(f'🔍 Изображение изменилось, удаляем старое: {old_image_url}')
            
            if '/media/' in old_image_url:
                filename = old_image_url.split('/media/')[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f'🔍 Путь к старому файлу: {file_path}')
                
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f'✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}')
                    except Exception as e:
                        print(f'❌ Ошибка удаления: {e}')
                else:
                    print(f'⚠️ Старый файл не найден: {file_path}')
        
        if old_image and old_image != new_image:
            file_path = old_image.path
            print(f'🔍 Удаляем старый файл image: {file_path}')
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        
        print('=' * 60)
        
        return response

    def perform_destroy(self, instance):
        print('=' * 60)
        print(f'🔍 Удаляем пост: {instance.title}')
        print(f'🔍 ID поста: {instance.id}')
        
        if instance.image:
            print(f'🔍 Поле image: {instance.image.name}')
            file_path = instance.image.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'✅ Изображение УСПЕШНО УДАЛЕНО: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        else:
            print('🔍 У поста нет image (загружено через ссылку)')
        
        if instance.image_url:
            print(f'🔍 image_url: {instance.image_url}')
            
            if '/media/' in instance.image_url:
                filename = instance.image_url.split('/media/')[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f'🔍 Декодированное имя: {filename}')
                print(f'🔍 Полный путь: {file_path}')
                
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f'✅ Изображение по URL УСПЕШНО УДАЛЕНО: {file_path}')
                    except Exception as e:
                        print(f'❌ Ошибка удаления: {e}')
                else:
                    print(f'⚠️ Файл не найден: {file_path}')
        
        print('=' * 60)
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='my_posts')
    def my_posts(self, request):
        user = request.user
        
        if not user.is_authenticated:
            return Response(
                {'detail': 'Не авторизован'},
                status=401
            )
        
        posts = Post.objects.filter(author=user)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(
        detail=False, 
        methods=['post'], 
        url_path='upload-image',
        parser_classes=[MultiPartParser, FormParser]
    )
    def upload_image(self, request):
        user = request.user
        
        if not user.is_authenticated or (user.role not in ['author', 'editor']):
            return Response(
                {'detail': 'Недостаточно прав'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        if 'image' not in request.FILES:
            return Response(
                {'detail': 'Файл не передан'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        file = request.FILES['image']
        
        if file.size > 5 * 1024 * 1024:
            return Response(
                {'detail': 'Файл слишком большой (макс 5MB)'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        if file.content_type not in allowed_types:
            return Response(
                {'detail': 'Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        filename = f"posts/{user.id}_{file.name}"
        file_path = default_storage.save(filename, ContentFile(file.read()))
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
        
        print(f'📁 Загружено изображение для поста: {file_path}')
        print(f'📁 URL: {file_url}')
        
        return Response({
            'image_url': file_url,
            'detail': 'Изображение загружено'
        }, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

---

### `backend/posts/serializers.py`

```python
from rest_framework import serializers
from .models import Post
from comments.serializers import CommentForPostSerializer


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    author_role = serializers.CharField(source='author.role', read_only=True)
    author_avatar = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user_has_liked = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'image',
            'image_url',
            'display_image',
            'author_name',
            'author_role',
            'author_avatar',
            'created_at',
            'updated_at',
            'is_published',
            'excerpt',
            'comments',
            'likes_count',
            'user_has_liked',
            'views',
        ]
        read_only_fields = ['author', 'author_name', 'author_role', 'author_avatar', 'created_at', 'updated_at', 'views']

    def get_comments(self, obj):
        top_level_comments = obj.comments.filter(parent__isnull=True)
        context = {'request': self.context.get('request')}
        return CommentForPostSerializer(top_level_comments, many=True, context=context).data

    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()

    def get_author_avatar(self, obj):
        if obj.author.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.author.avatar.url)
            return obj.author.avatar.url
        return None

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)
```

---

### `backend/posts/permissions.py`

```python
from rest_framework import permissions


class IsAuthorOrEditorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.role == 'editor'


class IsAuthorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.role in ['author', 'editor']
        return True
```

---

### `backend/posts/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
```

---

### `backend/posts/admin.py`

```python
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'is_published']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content', 'excerpt', 'author', 'is_published')
        }),
        ('Изображение', {
            'fields': ('image', 'image_url'),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
```

---

### `backend/comments/models.py`

```python
from django.db import models
from django.conf import settings
from django.utils import timezone
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Пост"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    content = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name="Родительский комментарий"
    )

    def clean(self):
        if self.parent and self.parent.post_id != self.post_id:
            from django.core.exceptions import ValidationError
            raise ValidationError({
                'parent': 'Родительский комментарий должен принадлежать тому же посту!'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_at']
```

---

### `backend/comments/views.py`

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post
from .permissions import IsOwnerOrReadOnly, CanCommentPermission


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, CanCommentPermission]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        queryset = super().get_queryset()
        post_id = self.request.query_params.get('post_id')
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], url_path='my_comments')
    def my_comments(self, request):
        user = request.user
        
        if not user.is_authenticated:
            return Response(
                {'detail': 'Не авторизован'},
                status=401
            )
        
        comments = Comment.objects.filter(author=user).order_by('-created_at')
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
```

---

### `backend/comments/serializers.py`

```python
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_avatar = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'author_name',
            'author_avatar',
            'content',
            'created_at',
            'updated_at',
            'parent',
            'replies',
            'can_edit',
            'can_delete',
            'likes_count',
            'user_has_liked',
        ]
        read_only_fields = ['author', 'post']

    def validate(self, data):
        parent = data.get('parent')
        post = data.get('post')
        if parent and post:
            if parent.post_id != post.id:
                raise serializers.ValidationError(
                    "Родительский комментарий должен принадлежать тому же посту"
                )
        return data

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

    def get_replies(self, obj):
        if obj.replies.exists():
            context = {'request': self.context.get('request')}
            return CommentSerializer(obj.replies.all(), many=True, context=context).data
        return []

    def get_can_edit(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.author == request.user

    def get_can_delete(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        
        user = request.user
        
        if obj.author == user:
            return True
        
        if obj.post.author == user:
            return True
        
        if user.role == 'editor':
            return True
        
        return False

    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()

    def get_author_avatar(self, obj):
        if obj.author.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.author.avatar.url)
            return obj.author.avatar.url
        return None


class CommentForPostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_avatar = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'author_name',
            'author_avatar',
            'content',
            'created_at',
            'updated_at',
            'parent',
            'replies',
            'can_edit',
            'can_delete',
            'likes_count',
            'user_has_liked',
        ]

    def get_replies(self, obj):
        if obj.replies.exists():
            context = {'request': self.context.get('request')}
            return CommentForPostSerializer(obj.replies.all(), many=True, context=context).data
        return []

    def get_can_edit(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.author == request.user

    def get_can_delete(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        
        user = request.user
        
        if obj.author == user:
            return True
        
        if obj.post.author == user:
            return True
        
        if user.role == 'editor':
            return True
        
        return False

    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()

    def get_author_avatar(self, obj):
        if obj.author.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.author.avatar.url)
            return obj.author.avatar.url
        return None
```

---

### `backend/comments/permissions.py`

```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        user = request.user
        
        if request.method in ['PUT', 'PATCH']:
            return obj.author == user
        
        if request.method == 'DELETE':
            if obj.author == user:
                return True
            if obj.post.author == user:
                return True
            if user.role == 'editor':
                return True
            return False
        
        return False


class CanCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True
```

---

### `backend/comments/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
```

---

### `backend/comments/admin.py`

```python
from django.contrib import admin
from django import forms
from .models import Comment


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent')
        post = cleaned_data.get('post')
        if parent and post:
            if parent.post_id != post.id:
                raise forms.ValidationError(
                    "Родительский комментарий должен принадлежать тому же посту!"
                )
        return cleaned_data


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['id', 'content', 'author', 'post', 'created_at', 'parent']
    list_filter = ['created_at', 'post']
    search_fields = ['content', 'author__username']
```

---

### `backend/events/models.py`

```python
import os
from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название события")
    content = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    
    event_date = models.DateTimeField(
        verbose_name="Дата и время проведения",
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Место проведения"
    )
    price = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Стоимость"
    )
    
    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True,
        verbose_name="Изображение (файл)"
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка на изображение"
    )
    
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )
    excerpt = models.TextField(
        blank=True,
        null=True,
        verbose_name="Краткое описание"
    )

    def delete(self, *args, **kwargs):
        if self.image:
            file_path = self.image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f'🗑️ Изображение события удалено: {file_path}')
        
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['-event_date', '-created_at']
```

---

### `backend/events/views.py`

```python
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from urllib.parse import unquote
import os
from .models import Event
from .serializers import EventSerializer
from .permissions import IsEditorOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsEditorOrReadOnly]

    def get_queryset(self):
        queryset = Event.objects.all()
        
        if self.action == 'list':
            return queryset.filter(is_published=True).order_by('event_date')
        
        return queryset

    def retrieve(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['pk'])
        
        if event.is_published:
            serializer = self.get_serializer(event)
            return Response(serializer.data)
        
        user = request.user
        if user.is_authenticated and user.role == 'editor':
            serializer = self.get_serializer(event)
            return Response(serializer.data)
        
        return Response({'detail': 'Событие не найдено'}, status=404)

    def update(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=kwargs['pk'])
        user = request.user
        
        if event.is_published:
            if user.role != 'editor':
                return Response({'detail': 'Недостаточно прав'}, status=403)
        else:
            if user.role != 'editor':
                return Response({'detail': 'Недостаточно прав'}, status=403)
        
        old_event = Event.objects.get(pk=kwargs['pk'])
        old_image_url = old_event.image_url
        old_image = old_event.image
        
        print('=' * 60)
        print(f'🔍 Обновляем событие: {event.title}')
        print(f'🔍 Старое изображение URL: {old_image_url}')
        print(f'🔍 Старое изображение файл: {old_image}')
        
        response = super().update(request, *args, **kwargs)
        
        event.refresh_from_db()
        
        new_image_url = event.image_url
        new_image = event.image
        
        print(f'🔍 Новое изображение URL: {new_image_url}')
        print(f'🔍 Новое изображение файл: {new_image}')
        
        if old_image_url and old_image_url != new_image_url:
            print(f'🔍 Изображение изменилось, удаляем старое: {old_image_url}')
            
            if '/media/' in old_image_url:
                filename = old_image_url.split('/media/')[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f'🔍 Путь к старому файлу: {file_path}')
                
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f'✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}')
                    except Exception as e:
                        print(f'❌ Ошибка удаления: {e}')
                else:
                    print(f'⚠️ Старый файл не найден: {file_path}')
        
        if old_image and old_image != new_image:
            file_path = old_image.path
            print(f'🔍 Удаляем старый файл image: {file_path}')
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'✅ Старое изображение УСПЕШНО УДАЛЕНО: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        
        print('=' * 60)
        
        return response

    def perform_destroy(self, instance):
        print('=' * 60)
        print(f'🔍 Удаляем событие: {instance.title}')
        print(f'🔍 ID события: {instance.id}')
        
        if instance.image:
            print(f'🔍 Поле image: {instance.image.name}')
            file_path = instance.image.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'✅ Изображение УСПЕШНО УДАЛЕНО: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        else:
            print('🔍 У события нет image (загружено через ссылку)')
        
        if instance.image_url:
            print(f'🔍 image_url: {instance.image_url}')
            
            if '/media/' in instance.image_url:
                filename = instance.image_url.split('/media/')[-1]
                filename = unquote(filename)
                file_path = os.path.join(settings.MEDIA_ROOT, filename)
                print(f'🔍 Декодированное имя: {filename}')
                print(f'🔍 Полный путь: {file_path}')
                
                if os.path.isfile(file_path):
                    try:
                        os.remove(file_path)
                        print(f'✅ Изображение по URL УСПЕШНО УДАЛЕНО: {file_path}')
                    except Exception as e:
                        print(f'❌ Ошибка удаления: {e}')
                else:
                    print(f'⚠️ Файл не найден: {file_path}')
        
        print('=' * 60)
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='my_events')
    def my_events(self, request):
        user = request.user
        
        if not user.is_authenticated:
            return Response(
                {'detail': 'Не авторизован'},
                status=401
            )
        
        if user.role != 'editor':
            return Response(
                {'detail': 'Недостаточно прав'},
                status=403
            )
        
        events = Event.objects.filter(author=user).order_by('event_date')
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(
        detail=False, 
        methods=['post'], 
        url_path='upload-image',
        parser_classes=[MultiPartParser, FormParser]
    )
    def upload_image(self, request):
        user = request.user
        
        if not user.is_authenticated or user.role != 'editor':
            return Response(
                {'detail': 'Недостаточно прав'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        if 'image' not in request.FILES:
            return Response(
                {'detail': 'Файл не передан'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        file = request.FILES['image']
        
        if file.size > 5 * 1024 * 1024:
            return Response(
                {'detail': 'Файл слишком большой (макс 5MB)'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        if file.content_type not in allowed_types:
            return Response(
                {'detail': 'Неподдерживаемый формат. Используйте JPEG, PNG, GIF или WEBP'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        filename = f"events/{user.id}_{file.name}"
        file_path = default_storage.save(filename, ContentFile(file.read()))
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
        
        print(f'📁 Загружено изображение: {file_path}')
        print(f'📁 URL: {file_url}')
        
        return Response({
            'image_url': file_url,
            'detail': 'Изображение загружено'
        }, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

---

### `backend/events/serializers.py`

```python
import os
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    author_role = serializers.CharField(source='author.role', read_only=True)
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'content',
            'author_name',
            'author_role',
            'event_date',
            'location',
            'price',
            'image',
            'image_url',
            'display_image',
            'created_at',
            'updated_at',
            'is_published',
            'excerpt',
        ]
        read_only_fields = ['author', 'author_name', 'author_role', 'created_at', 'updated_at']

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.excerpt = validated_data.get('excerpt', instance.excerpt)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.location = validated_data.get('location', instance.location)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.save()
        return instance
```

---

### `backend/events/permissions.py`

```python
from rest_framework import permissions


class IsEditorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.method == 'POST':
            return request.user.is_authenticated and request.user.role == 'editor'
        
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.role == 'editor'
```

---

### `backend/events/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]
```

---

### `backend/events/admin.py`

```python
from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'event_date', 'location', 'is_published']
    list_filter = ['is_published', 'event_date', 'location']
    search_fields = ['title', 'content', 'location']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content', 'excerpt', 'author', 'is_published')
        }),
        ('Детали события', {
            'fields': ('event_date', 'location', 'price', 'image', 'image_url')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
```
---

### `backend/events/signals.py`

```python
from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'event_date', 'location', 'is_published']
    list_filter = ['is_published', 'event_date', 'location']
    search_fields = ['title', 'content', 'location']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'content', 'excerpt', 'author', 'is_published')
        }),
        ('Детали события', {
            'fields': ('event_date', 'location', 'price', 'image', 'image_url')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

```

---

### `backend/likes/models.py`

```python
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from posts.models import Post
from comments.models import Comment


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пользователь'
    )
    
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='likes',
        verbose_name='Пост'
    )
    
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='likes',
        verbose_name='Комментарий'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        unique_together = [
            ['user', 'post'],
            ['user', 'comment'],
        ]
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = ['-created_at']

    def clean(self):
        if not self.post and not self.comment:
            raise ValidationError('Лайк должен быть привязан к посту или комментарию')
        if self.post and self.comment:
            raise ValidationError('Лайк не может быть привязан одновременно к посту и комментарию')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.post:
            return f"{self.user.username} → {self.post.title}"
        return f"{self.user.username} → комментарий {self.comment.id}"
```

---

### `backend/likes/views.py`

```python
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post
from comments.models import Comment


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        comment_id = request.data.get('comment')
        
        if not post_id and not comment_id:
            return Response(
                {'detail': 'Не указан пост или комментарий'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if post_id:
            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                return Response(
                    {'detail': 'Пост не найден'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            existing_like = Like.objects.filter(user=request.user, post=post).first()
            
            if existing_like:
                existing_like.delete()
                return Response(
                    {'detail': 'Лайк убран', 'action': 'unliked', 'type': 'post'},
                    status=status.HTTP_200_OK
                )
            else:
                like = Like.objects.create(user=request.user, post=post)
                serializer = self.get_serializer(like)
                return Response(
                    {'detail': 'Лайк поставлен', 'action': 'liked', 'type': 'post', 'data': serializer.data},
                    status=status.HTTP_201_CREATED
                )
        
        if comment_id:
            try:
                comment = Comment.objects.get(id=comment_id)
            except Comment.DoesNotExist:
                return Response(
                    {'detail': 'Комментарий не найден'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            existing_like = Like.objects.filter(user=request.user, comment=comment).first()
            
            if existing_like:
                existing_like.delete()
                return Response(
                    {'detail': 'Лайк убран', 'action': 'unliked', 'type': 'comment'},
                    status=status.HTTP_200_OK
                )
            else:
                like = Like.objects.create(user=request.user, comment=comment)
                serializer = self.get_serializer(like)
                return Response(
                    {'detail': 'Лайк поставлен', 'action': 'liked', 'type': 'comment', 'data': serializer.data},
                    status=status.HTTP_201_CREATED
                )
```

---

### `backend/likes/serializers.py`

```python
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'post', 'comment', 'username', 'created_at']
        read_only_fields = ['user', 'created_at']
```

---

### `backend/likes/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikeViewSet

router = DefaultRouter()
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
    path('', include(router.urls)),
]
```

---

### `backend/likes/admin.py`

```python
from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'post__title']
```

---

### `backend/contactinfo/models.py`

```python
from django.db import models


class ContactInfo(models.Model):
    address = models.CharField(
        max_length=255,
        default='г. Москва, ул. Культурная, д. 1',
        verbose_name='Адрес'
    )
    phone = models.CharField(
        max_length=50,
        default='+7 (495) 123-45-67',
        verbose_name='Телефон'
    )
    email = models.EmailField(
        default='info@kultcentr.ru',
        verbose_name='Email'
    )
    work_hours = models.CharField(
        max_length=100,
        default='Пн–Пт: 10:00 – 20:00',
        verbose_name='Часы работы'
    )
    description = models.TextField(
        default='Место, где искусство, традиции и творчество объединяются.\nМы создаём пространство для культурного развития и вдохновения.',
        verbose_name='Описание'
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        verbose_name='Instagram'
    )
    vk = models.URLField(
        blank=True,
        null=True,
        verbose_name='ВКонтакте'
    )
    telegram = models.URLField(
        blank=True,
        null=True,
        verbose_name='Telegram'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return f'Контактная информация (обновлено: {self.updated_at.strftime("%d.%m.%Y")})'

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
```

---

### `backend/contactinfo/views.py`

```python
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import ContactInfo
from .serializers import ContactInfoSerializer


class ContactInfoView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.first()


class ContactInfoUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactInfoSerializer

    def get_object(self):
        return ContactInfo.objects.first()

    def update(self, request, *args, **kwargs):
        user = request.user
        
        if user.role != 'editor':
            return Response(
                {'detail': 'Только главные редакторы могут редактировать контакты'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().update(request, *args, **kwargs)
```

---

### `backend/contactinfo/urls.py`

```python
from django.urls import path
from .views import ContactInfoView, ContactInfoUpdateView

urlpatterns = [
    path('', ContactInfoView.as_view(), name='contact_info'),
    path('update/', ContactInfoUpdateView.as_view(), name='contact_info_update'),
]
```

---

### `backend/contactinfo/admin.py`

```python
from django.contrib import admin
from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'updated_at']
    fieldsets = (
        ('Основная информация', {
            'fields': ('address', 'phone', 'email', 'work_hours', 'description')
        }),
        ('Социальные сети', {
            'fields': ('instagram', 'vk', 'telegram')
        }),
        ('Дата обновления', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['updated_at']
```

---

### `backend/contactinfo/serializers.py`

```python
from rest_framework import serializers
from .models import ContactInfo


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            "id",
            "address",
            "phone",
            "email",
            "work_hours",
            "description",
            "instagram",
            "vk",
            "telegram",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]

```

---

### `backend/manage.py`

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

---

## ПОЛНЫЕ ФАЙЛЫ ФРОНТЕНДА

### `frontend/nuxt.config.ts`

```typescript
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@pinia/nuxt', '@nuxtjs/tailwindcss'],
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000/api'
    }
  }
})
```

---

### `frontend/tailwind.config.js`

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './components/**/*.{vue,js}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './app.vue',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

---

### `frontend/assets/css/main.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-gray-50 text-gray-900 dark:bg-gray-900 dark:text-gray-100;
  }
}

@layer components {
  .card {
    @apply bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-md transition;
  }
}
```

---

### `frontend/store/auth.js`

```javascript
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        accessToken: null,
        refreshToken: null
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken && !!state.user,
        isAuthor: (state) => state.user?.role === 'author',
        isSubscriber: (state) => state.user?.role === 'subscriber',
        isEditor: (state) => state.user?.role === 'editor',
        username: (state) => state.user?.username || '',
    },

    actions: {
        setAuth(user, access, refresh) {
            this.user = user
            this.accessToken = access
            this.refreshToken = refresh

            if (process.client) {
                localStorage.setItem('access_token', access)
                localStorage.setItem('refresh_token', refresh)
                localStorage.setItem('user', JSON.stringify(user))
            }
        },

        restoreAuth() {
            if (process.client) {
                const access = localStorage.getItem('access_token')
                const refresh = localStorage.getItem('refresh_token')
                const userStr = localStorage.getItem('user')

                if (access && refresh && userStr) {
                    this.accessToken = access
                    this.refreshToken = refresh
                    this.user = JSON.parse(userStr)
                }
            }
        },

        logout() {
            this.user = null
            this.accessToken = null
            this.refreshToken = null

            if (process.client) {
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
                localStorage.removeItem('user')
            }
        }
    }
})
```

---

### `frontend/store/theme.js`

```javascript
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    darkMode: false,
  }),

  actions: {
    toggleTheme() {
      this.darkMode = !this.darkMode
      this.applyTheme()
    },

    applyTheme() {
      if (process.client) {
        if (this.darkMode) {
          document.documentElement.classList.add('dark')
          localStorage.setItem('theme', 'dark')
        } else {
          document.documentElement.classList.remove('dark')
          localStorage.setItem('theme', 'light')
        }
      }
    },

    loadTheme() {
      if (process.client) {
        const savedTheme = localStorage.getItem('theme')
        if (savedTheme === 'dark') {
          this.darkMode = true
          document.documentElement.classList.add('dark')
        } else {
          this.darkMode = false
          document.documentElement.classList.remove('dark')
        }
      }
    },
  },
})
```

---

### `frontend/middleware/auth.js`

```javascript
import { useAuthStore } from '~/store/auth'

export default defineNuxtRouteMiddleware((to, from) => {
  const authStore = useAuthStore()
  
  authStore.restoreAuth()
  
  if (!authStore.isAuthenticated) {
    return navigateTo('/auth/login')
  }
})
```

---

### `frontend/app.vue`

```vue
<template>
  <div class="flex flex-col min-h-screen">
    <!-- HEADER -->
    <header class="bg-white dark:bg-gray-800 shadow transition-colors duration-200 sticky top-0 z-50">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <NuxtLink to="/" class="text-xl font-bold text-gray-800 dark:text-white">
          🏛️ Центр Культуры
        </NuxtLink>
        
        <div class="flex items-center gap-6">
          <nav class="flex items-center gap-6">
            <NuxtLink to="/events" class="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition">
              🎭 Афиша
            </NuxtLink>
            <NuxtLink to="/posts" class="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition">
              📝 Публикации
            </NuxtLink>
            <NuxtLink to="/authors" class="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition">
              ✍️ Авторы
            </NuxtLink>
            <NuxtLink to="/contacts" class="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition">
              📞 Контакты
            </NuxtLink>
          </nav>
          
          <div class="flex items-center gap-4">
            <button 
              @click="themeStore.toggleTheme"
              class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition"
              :title="themeStore.darkMode ? 'Светлая тема' : 'Тёмная тема'"
              aria-label="Переключить тему"
            >
              <span class="text-xl">
                {{ themeStore.darkMode ? '☀️' : '🌙' }}
              </span>
            </button>
            
            <template v-if="authStore.isAuthenticated">
              <NuxtLink 
                to="/profile" 
                class="flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition font-medium"
              >
                <img 
                  v-if="authStore.user?.avatar_url" 
                  :src="authStore.user?.avatar_url" 
                  :alt="authStore.user?.username"
                  class="w-8 h-8 rounded-full object-cover"
                >
                <div 
                  v-else
                  class="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white text-xs font-bold"
                >
                  {{ getInitials(authStore.user) }}
                </div>
                {{ authStore.user?.username }}
              </NuxtLink>
              
              <button 
                @click="logout" 
                class="text-red-500 dark:text-red-400 hover:text-red-700 dark:hover:text-red-300 transition"
              >
                Выйти
              </button>
            </template>
            
            <template v-else>
              <NuxtLink to="/auth/login" class="text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition">
                Вход
              </NuxtLink>
              <NuxtLink to="/auth/register" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
                Регистрация
              </NuxtLink>
            </template>
          </div>
        </div>
      </div>
    </header>

    <!-- MAIN -->
    <main class="flex-1">
      <NuxtPage />
    </main>

    <!-- FOOTER -->
    <footer class="bg-gray-800 dark:bg-gray-900 text-gray-300 mt-10">
      <div class="container mx-auto px-4 py-8">
        <div v-if="contactsLoading" class="text-center py-4 text-gray-400">
          Загрузка контактов...
        </div>
        
        <div v-else-if="contacts" class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 class="text-white text-lg font-semibold mb-3">🏛️ Центр Культуры</h3>
            <p class="text-sm text-gray-400 leading-relaxed whitespace-pre-wrap">
              {{ contacts.description }}
            </p>
          </div>
          
          <div>
            <h3 class="text-white text-lg font-semibold mb-3">📞 Контакты</h3>
            <ul class="space-y-2 text-sm">
              <li class="flex items-center gap-2">
                <span>📍</span>
                <span>{{ contacts.address }}</span>
              </li>
              <li class="flex items-center gap-2">
                <span>📞</span>
                <a :href="`tel:${contacts.phone}`" class="hover:text-blue-400 transition">
                  {{ contacts.phone }}
                </a>
              </li>
              <li class="flex items-center gap-2">
                <span>✉️</span>
                <a :href="`mailto:${contacts.email}`" class="hover:text-blue-400 transition">
                  {{ contacts.email }}
                </a>
              </li>
              <li class="flex items-center gap-2">
                <span>🕐</span>
                <span>{{ contacts.work_hours }}</span>
              </li>
            </ul>
          </div>
          
          <div>
            <h3 class="text-white text-lg font-semibold mb-3">📂 Разделы</h3>
            <ul class="space-y-2 text-sm">
              <li>
                <NuxtLink to="/events" class="hover:text-blue-400 transition">
                  🎭 Афиша
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/posts" class="hover:text-blue-400 transition">
                  📝 Публикации
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/authors" class="hover:text-blue-400 transition">
                  ✍️ Авторы
                </NuxtLink>
              </li>
              <li>
                <NuxtLink to="/contacts" class="hover:text-blue-400 transition">
                  📞 Контакты
                </NuxtLink>
              </li>
            </ul>
          </div>
        </div>
        
        <div class="border-t border-gray-700 mt-6 pt-6 text-center text-sm text-gray-500">
          <p>© {{ new Date().getFullYear() }} Центр Культуры. Все права защищены.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import { useThemeStore } from '~/store/theme'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const themeStore = useThemeStore()

const contacts = ref(null)
const contactsLoading = ref(true)

const getInitials = (user) => {
  if (!user) return '?'
  const name = user.full_name || user.username
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

onMounted(async () => {
  authStore.restoreAuth()
  themeStore.loadTheme()
  
  try {
    const res = await fetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      contacts.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки контактов:', e)
  } finally {
    contactsLoading.value = false
  }
})

const logout = () => {
  authStore.logout()
  navigateTo('/')
}
</script>
```

---

### `frontend/pages/index.vue`

```vue
<template>
  <div>
    <div class="w-full bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-800 dark:to-purple-800 text-white py-20 md:py-28 transition-colors duration-200">
      <div class="container mx-auto px-4 text-center">
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-4">
          🏛️ Добро пожаловать в Центр Культуры
        </h1>
        <p class="text-lg md:text-xl text-blue-100 dark:text-blue-200 max-w-2xl mx-auto">
          Место, где искусство, традиции и творчество объединяются
        </p>
      </div>
    </div>

    <div class="container mx-auto p-4">
      <div class="space-y-10">
        <!-- Афиша -->
        <div>
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-gray-800 dark:text-gray-200">🎭 Афиша</h2>
            <NuxtLink to="/events" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
              Все события →
            </NuxtLink>
          </div>
          
          <div v-if="eventsLoading" class="text-center py-10">
            <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
          </div>
          
          <div v-else-if="events.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
            <p class="text-gray-500 dark:text-gray-400">Пока нет событий</p>
          </div>
          
          <div v-else>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
              <div 
                v-for="event in events.slice(0, 5)" 
                :key="event.id" 
                class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-lg transition overflow-hidden flex flex-col"
              >
                <NuxtLink :to="`/events/${event.id}`" class="flex flex-col h-full">
                  <div v-if="event.display_image" class="h-40 overflow-hidden flex-shrink-0">
                    <img :src="event.display_image" :alt="event.title" class="w-full h-full object-cover">
                  </div>
                  <div v-else class="h-40 bg-gradient-to-r from-purple-400 to-blue-500 flex items-center justify-center flex-shrink-0">
                    <span class="text-white text-4xl">🎭</span>
                  </div>
                  
                  <div class="p-3 flex flex-col flex-1">
                    <h3 class="text-sm font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition line-clamp-2">
                      {{ event.title }}
                    </h3>
                    <p class="text-gray-500 dark:text-gray-400 text-xs mt-1 line-clamp-2 flex-1">
                      {{ event.excerpt || event.content?.substring(0, 80) }}...
                    </p>
                    
                    <div class="flex flex-wrap gap-1 mt-2 pt-2 border-t border-gray-100 dark:border-gray-700 text-xs text-gray-400 dark:text-gray-500">
                      <span v-if="event.event_date">📅 {{ formatDateShort(event.event_date) }}</span>
                      <span v-if="event.location">📍 {{ event.location }}</span>
                    </div>
                  </div>
                </NuxtLink>
              </div>
            </div>
            
            <div v-if="events.length > 5" class="text-center mt-4">
              <NuxtLink to="/events" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
                Показать ещё {{ events.length - 5 }} событий →
              </NuxtLink>
            </div>
          </div>
        </div>
        
        <!-- Публикации -->
        <div>
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-gray-800 dark:text-gray-200">📝 Публикации</h2>
            <NuxtLink to="/posts" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
              Все публикации →
            </NuxtLink>
          </div>
          
          <div v-if="postsLoading" class="text-center py-10">
            <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
          </div>
          
          <div v-else-if="posts.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
            <p class="text-gray-500 dark:text-gray-400">Пока нет публикаций</p>
          </div>
          
          <div v-else>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              <div 
                v-for="post in posts.filter(p => p.is_published).slice(0, 8)" 
                :key="post.id" 
                class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-md transition overflow-hidden flex flex-col"
              >
                <div v-if="post.display_image" class="h-40 overflow-hidden flex-shrink-0">
                  <img :src="post.display_image" :alt="post.title" class="w-full h-full object-cover">
                </div>
                <div v-else class="h-40 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-600 flex items-center justify-center flex-shrink-0">
                  <span class="text-gray-400 dark:text-gray-500 text-4xl">📝</span>
                </div>
                
                <div class="p-4 flex flex-col flex-1">
                  <NuxtLink :to="`/posts/${post.id}`" class="flex-1">
                    <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition line-clamp-2">
                      {{ post.title }}
                    </h3>
                    <p class="text-gray-600 dark:text-gray-400 text-sm mt-1 line-clamp-3">
                      {{ post.excerpt || post.content?.substring(0, 100) }}...
                    </p>
                  </NuxtLink>
                  
                  <div class="flex justify-between items-center mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
                    <div class="flex items-center gap-3 text-xs text-gray-400 dark:text-gray-500">
                      <div class="flex items-center gap-1">
                        <img 
                          v-if="post.author_avatar" 
                          :src="post.author_avatar" 
                          :alt="post.author_name"
                          class="w-5 h-5 rounded-full object-cover"
                        >
                        <div 
                          v-else
                          class="w-5 h-5 rounded-full bg-blue-500 flex items-center justify-center text-white text-[8px] font-bold"
                        >
                          {{ getInitials(post.author_name) }}
                        </div>
                        <span>{{ post.author_name }}</span>
                      </div>
                      <span>👁️ {{ post.views || 0 }}</span>
                      <span>💬 {{ post.comments?.length || 0 }}</span>
                      <LikeButton 
                        :post-id="post.id"
                        :initial-likes-count="post.likes_count || 0"
                        :initial-is-liked="post.user_has_liked || false"
                        @update="(data) => { 
                          post.likes_count = data.likesCount; 
                          post.user_has_liked = data.isLiked; 
                        }"
                      />
                    </div>
                    <span class="text-xs text-gray-400 dark:text-gray-500">{{ formatDateShort(post.created_at) }}</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div v-if="posts.filter(p => p.is_published).length > 8" class="text-center mt-4">
              <NuxtLink to="/posts" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
                Показать ещё {{ posts.filter(p => p.is_published).length - 8 }} публикаций →
              </NuxtLink>
            </div>
          </div>
        </div>
        
        <!-- Авторы -->
        <div>
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-gray-800 dark:text-gray-200">✍️ Авторы</h2>
            <NuxtLink to="/authors" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
              Все авторы →
            </NuxtLink>
          </div>
          
          <div v-if="authorsLoading" class="text-center py-10">
            <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
          </div>
          
          <div v-else-if="authors.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
            <p class="text-gray-500 dark:text-gray-400">Пока нет авторов</p>
          </div>
          
          <div v-else>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
              <div 
                v-for="author in authors.slice(0, 6)" 
                :key="author.id" 
                class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow hover:shadow-md transition text-center"
              >
                <div class="w-16 h-16 mx-auto rounded-full bg-blue-500 flex items-center justify-center text-white text-xl font-bold overflow-hidden">
                  <img v-if="author.avatar_url" :src="author.avatar_url" :alt="author.username" class="w-full h-full object-cover">
                  <span v-else>{{ getInitials(author.full_name || author.username) }}</span>
                </div>
                <h3 class="text-sm font-semibold text-gray-800 dark:text-gray-200 mt-2">{{ getFullName(author) }}</h3>
                <p class="text-xs text-gray-400 dark:text-gray-500">{{ author.role_display }}</p>
                <NuxtLink 
                  :to="`/authors/${author.id}`" 
                  class="mt-2 inline-block text-xs text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition"
                >
                  Публикации автора →
                </NuxtLink>
              </div>
            </div>
            
            <div v-if="authors.length > 6" class="text-center mt-4">
              <NuxtLink to="/authors" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
                Показать всех авторов →
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const posts = ref([])
const events = ref([])
const authors = ref([])
const postsLoading = ref(true)
const eventsLoading = ref(true)
const authorsLoading = ref(true)

const formatDateShort = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
  })
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const getFullName = (user) => {
  return user.full_name || user.username
}

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/posts/`, { headers })
    posts.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки постов:', e)
  } finally {
    postsLoading.value = false
  }
})

onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/events/`, { headers })
    events.value = await res.json()
  } catch (e) {
    console.error('Ошибка загрузки событий:', e)
  } finally {
    eventsLoading.value = false
  }
})

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/auth/users/`)
    if (res.ok) {
      const allUsers = await res.json()
      authors.value = allUsers.filter(user => user.role === 'author' || user.role === 'editor')
    }
  } catch (e) {
    console.error('Ошибка загрузки авторов:', e)
  } finally {
    authorsLoading.value = false
  }
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
```

---

### `frontend/pages/profile.vue`

```vue
<template>
  <div class="max-w-4xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="error" class="text-red-500 text-center py-10">
      {{ error }}
    </div>
    
    <div v-else>
      <!-- РЕЖИМ ПРОСМОТРА -->
      <div v-if="!isEditing">
        <div class="flex flex-col items-center mb-6">
          <div class="w-32 h-32 rounded-full bg-blue-500 flex items-center justify-center text-white text-5xl font-bold shadow-lg overflow-hidden">
            <img v-if="avatarPreview" :src="avatarPreview" alt="Аватар" class="w-full h-full object-cover">
            <span v-else>{{ userInitials }}</span>
          </div>
          <h2 class="text-2xl font-bold mt-3 text-gray-800 dark:text-gray-200">{{ fullName || username }}</h2>
          <p class="text-gray-500 dark:text-gray-400 text-sm">{{ roleDisplay }}</p>
        </div>
        
        <div class="space-y-4 border-t border-gray-100 dark:border-gray-700 pt-6">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Имя</label>
              <p class="text-gray-800 dark:text-gray-200">{{ form.first_name || '—' }}</p>
            </div>
            <div>
              <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Фамилия</label>
              <p class="text-gray-800 dark:text-gray-200">{{ form.last_name || '—' }}</p>
            </div>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Отчество</label>
            <p class="text-gray-800 dark:text-gray-200">{{ form.patronymic || '—' }}</p>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Email</label>
            <p class="text-gray-800 dark:text-gray-200">{{ form.email || '—' }}</p>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Дата рождения</label>
            <p class="text-gray-800 dark:text-gray-200">{{ form.birth_date ? formatDate(form.birth_date) : '—' }}</p>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">О себе</label>
            <p class="text-gray-700 dark:text-gray-300 whitespace-pre-wrap">{{ form.bio || '—' }}</p>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Роль</label>
            <p class="text-gray-800 dark:text-gray-200">
              <span class="inline-block bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 px-3 py-1 rounded-full text-sm">
                {{ form.role_display }}
              </span>
            </p>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Дата регистрации</label>
            <p class="text-gray-800 dark:text-gray-200">{{ formatDate(form.date_joined) }}</p>
          </div>
        </div>
        
        <button 
          @click="startEditing"
          class="mt-6 w-full bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          ✏️ Редактировать профиль
        </button>
      </div>
      
      <!-- РЕЖИМ РЕДАКТИРОВАНИЯ -->
      <form v-else @submit.prevent="updateProfile" enctype="multipart/form-data">
        <div class="flex flex-col items-center mb-6">
          <div class="w-32 h-32 rounded-full bg-blue-500 flex items-center justify-center text-white text-5xl font-bold shadow-lg overflow-hidden">
            <img v-if="avatarPreview" :src="avatarPreview" alt="Аватар" class="w-full h-full object-cover">
            <span v-else>{{ userInitials }}</span>
          </div>
          <h2 class="text-2xl font-bold mt-3 text-gray-800 dark:text-gray-200">{{ fullName || username }}</h2>
          <p class="text-gray-500 dark:text-gray-400 text-sm">{{ roleDisplay }}</p>
        </div>
        
        <div class="space-y-4 border-t border-gray-100 dark:border-gray-700 pt-6">
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Имя пользователя</label>
            <input 
              v-model="form.username" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-gray-100 dark:bg-gray-700 cursor-not-allowed text-gray-600 dark:text-gray-400"
              disabled
            >
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Аватар</label>
            <input 
              type="file" 
              accept="image/*"
              @change="onFileSelected"
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            >
          </div>
          
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Имя</label>
              <input 
                v-model="form.first_name" 
                type="text" 
                class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              >
            </div>
            <div>
              <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Фамилия</label>
              <input 
                v-model="form.last_name" 
                type="text" 
                class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              >
            </div>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Отчество</label>
            <input 
              v-model="form.patronymic" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            >
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Email</label>
            <input 
              v-model="form.email" 
              type="email" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            >
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Дата рождения</label>
            <input 
              v-model="form.birth_date" 
              type="date" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            >
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">О себе</label>
            <textarea 
              v-model="form.bio" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
              rows="4"
              placeholder="Расскажите о себе..."
            ></textarea>
          </div>
          
          <div>
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Роль</label>
            <input 
              :value="form.role_display" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-gray-100 dark:bg-gray-700 cursor-not-allowed text-gray-600 dark:text-gray-400"
              disabled
            >
          </div>
        </div>
        
        <div class="flex gap-3 mt-6">
          <button 
            type="submit" 
            class="flex-1 bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
            :disabled="submitting"
          >
            {{ submitting ? 'Сохранение...' : 'Сохранить' }}
          </button>
          <button 
            type="button"
            @click="cancelEditing"
            class="flex-1 bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
          >
            Отмена
          </button>
        </div>
        
        <p v-if="success" class="mt-4 text-green-500 text-sm text-center">{{ success }}</p>
        <p v-if="submitError" class="mt-4 text-red-500 text-sm text-center">{{ submitError }}</p>
      </form>
    </div>
    
    <!-- СМЕНА ПАРОЛЯ -->
    <div class="mt-6 border-t border-gray-200 dark:border-gray-700 pt-6">
      <button 
        @click="showChangePassword = !showChangePassword"
        class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm font-medium"
      >
        {{ showChangePassword ? 'Скрыть смену пароля' : 'Изменить пароль' }}
      </button>
      
      <div v-if="showChangePassword" class="mt-4 bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
        <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">Смена пароля</h3>
        
        <form @submit.prevent="changePassword">
          <div class="mb-3">
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Текущий пароль</label>
            <input 
              v-model="passwordForm.old_password" 
              type="password" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
            >
          </div>
          
          <div class="mb-3">
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Новый пароль</label>
            <input 
              v-model="passwordForm.new_password" 
              type="password" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
              minlength="8"
            >
          </div>
          
          <div class="mb-3">
            <label class="block text-gray-500 dark:text-gray-400 text-sm font-medium">Подтвердите новый пароль</label>
            <input 
              v-model="passwordForm.new_password2" 
              type="password" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              required
              minlength="8"
            >
          </div>
          
          <div class="flex gap-3">
            <button 
              type="submit" 
              class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
              :disabled="passwordSubmitting"
            >
              {{ passwordSubmitting ? 'Сохранение...' : 'Сменить пароль' }}
            </button>
            <button 
              type="button"
              @click="showChangePassword = false"
              class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
            >
              Отмена
            </button>
          </div>
          
          <p v-if="passwordSuccess" class="mt-3 text-green-500 text-sm">{{ passwordSuccess }}</p>
          <p v-if="passwordError" class="mt-3 text-red-500 text-sm">{{ passwordError }}</p>
        </form>
      </div>
    </div>
    
    <!-- МОИ АФИШИ -->
    <div v-if="authStore.isEditor" class="mt-10 border-t border-gray-200 dark:border-gray-700 pt-8">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">🎭 Мои афиши</h2>
      
      <div class="flex gap-2 mb-4">
        <button 
          @click="eventFilter = 'all'"
          class="px-4 py-1 rounded-lg text-sm transition"
          :class="eventFilter === 'all' ? 'bg-blue-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'"
        >
          Все
        </button>
        <button 
          @click="eventFilter = 'published'"
          class="px-4 py-1 rounded-lg text-sm transition"
          :class="eventFilter === 'published' ? 'bg-green-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'"
        >
          Опубликованные
        </button>
        <button 
          @click="eventFilter = 'draft'"
          class="px-4 py-1 rounded-lg text-sm transition"
          :class="eventFilter === 'draft' ? 'bg-yellow-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'"
        >
          Черновики
        </button>
      </div>
      
      <div v-if="userEventsLoading" class="text-center py-6">
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>
      
      <div v-else-if="filteredEvents.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
        Нет событий
      </div>
      
      <div v-else class="space-y-3">
        <div 
          v-for="event in filteredEvents" 
          :key="event.id" 
          class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg hover:shadow transition"
        >
          <NuxtLink :to="event.is_published ? `/events/${event.id}` : `/events/edit-${event.id}`" class="block">
            <div class="flex justify-between items-start">
              <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
                {{ event.title }}
              </h3>
              <span 
                v-if="event.is_published" 
                class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-1 rounded-full flex-shrink-0 ml-2"
              >
                Опубликовано
              </span>
              <span 
                v-else 
                class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-1 rounded-full flex-shrink-0 ml-2"
              >
                Черновик
              </span>
            </div>
            <p class="text-gray-600 dark:text-gray-400 text-sm mt-1">{{ event.excerpt || event.content?.substring(0, 100) }}...</p>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">{{ formatDate(event.created_at) }}</p>
          </NuxtLink>
        </div>
      </div>
    </div>
    
    <!-- МОИ ПОСТЫ -->
    <div v-if="authStore.isAuthor || authStore.isEditor" class="mt-10 border-t border-gray-200 dark:border-gray-700 pt-8">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">📝 Мои посты</h2>
      
      <div class="flex gap-2 mb-4">
        <button 
          @click="postFilter = 'all'"
          class="px-4 py-1 rounded-lg text-sm transition"
          :class="postFilter === 'all' ? 'bg-blue-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'"
        >
          Все
        </button>
        <button 
          @click="postFilter = 'published'"
          class="px-4 py-1 rounded-lg text-sm transition"
          :class="postFilter === 'published' ? 'bg-green-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'"
        >
          Опубликованные
        </button>
        <button 
          @click="postFilter = 'draft'"
          class="px-4 py-1 rounded-lg text-sm transition"
          :class="postFilter === 'draft' ? 'bg-yellow-500 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'"
        >
          Черновики
        </button>
      </div>
      
      <div v-if="userPostsLoading" class="text-center py-6">
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>
      
      <div v-else-if="filteredPosts.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
        Нет постов
      </div>
      
      <div v-else class="space-y-3">
        <div 
          v-for="post in filteredPosts" 
          :key="post.id" 
          class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg hover:shadow transition flex gap-4"
        >
          <div v-if="post.display_image" class="h-20 w-20 rounded-lg overflow-hidden flex-shrink-0">
            <img :src="post.display_image" :alt="post.title" class="w-full h-full object-cover">
          </div>
          <div v-else class="h-20 w-20 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-500 rounded-lg flex items-center justify-center flex-shrink-0">
            <span class="text-gray-400 dark:text-gray-500 text-2xl">📝</span>
          </div>
          
          <NuxtLink :to="post.is_published ? `/posts/${post.id}` : `/posts/edit-${post.id}`" class="block flex-1">
            <div class="flex justify-between items-start">
              <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
                {{ post.title }}
              </h3>
              <span 
                v-if="post.is_published" 
                class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-1 rounded-full flex-shrink-0 ml-2"
              >
                Опубликовано
              </span>
              <span 
                v-else 
                class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-1 rounded-full flex-shrink-0 ml-2"
              >
                Черновик
              </span>
            </div>
            <p class="text-gray-600 dark:text-gray-400 text-sm mt-1 line-clamp-2">{{ post.excerpt || post.content?.substring(0, 100) }}...</p>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">{{ formatDate(post.created_at) }}</p>
          </NuxtLink>
        </div>
      </div>
    </div>
    
    <!-- МОИ КОММЕНТАРИИ -->
    <div v-if="authStore.isAuthenticated" class="mt-10 border-t border-gray-200 dark:border-gray-700 pt-8">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">💬 Мои комментарии</h2>
      
      <div v-if="userCommentsLoading" class="text-center py-6">
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>
      
      <div v-else-if="userComments.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
        Нет комментариев
      </div>
      
      <div v-else class="space-y-3">
        <div 
          v-for="comment in userComments" 
          :key="comment.id" 
          class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg hover:shadow transition"
        >
          <NuxtLink :to="`/posts/${comment.post}`" class="block">
            <div class="flex justify-between items-start">
              <p class="text-gray-700 dark:text-gray-300">{{ comment.content }}</p>
              <span class="text-xs bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300 px-2 py-1 rounded-full flex-shrink-0 ml-2">
                ❤️ {{ comment.likes_count || 0 }}
              </span>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">К посту #{{ comment.post }} • {{ formatDate(comment.created_at) }}</p>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()

const loading = ref(true)
const submitting = ref(false)
const isEditing = ref(false)
const error = ref('')
const submitError = ref('')
const success = ref('')

const avatarFile = ref(null)
const avatarPreview = ref(null)

const form = ref({
  username: '',
  first_name: '',
  last_name: '',
  patronymic: '',
  email: '',
  birth_date: '',
  bio: '',
  role_display: '',
  date_joined: ''
})

const originalForm = ref({})

const userPosts = ref([])
const userPostsLoading = ref(true)
const postFilter = ref('all')

const userEvents = ref([])
const userEventsLoading = ref(true)
const eventFilter = ref('all')

const userComments = ref([])
const userCommentsLoading = ref(true)

const showChangePassword = ref(false)
const passwordSubmitting = ref(false)
const passwordSuccess = ref('')
const passwordError = ref('')

const passwordForm = ref({
  old_password: '',
  new_password: '',
  new_password2: ''
})

const filteredPosts = computed(() => {
  if (postFilter.value === 'published') {
    return userPosts.value.filter(p => p.is_published)
  }
  if (postFilter.value === 'draft') {
    return userPosts.value.filter(p => !p.is_published)
  }
  return userPosts.value
})

const filteredEvents = computed(() => {
  if (eventFilter.value === 'published') {
    return userEvents.value.filter(e => e.is_published)
  }
  if (eventFilter.value === 'draft') {
    return userEvents.value.filter(e => !e.is_published)
  }
  return userEvents.value
})

const fullName = computed(() => {
  const parts = []
  if (form.value.last_name) parts.push(form.value.last_name)
  if (form.value.first_name) parts.push(form.value.first_name)
  if (form.value.patronymic) parts.push(form.value.patronymic)
  return parts.length ? parts.join(' ') : form.value.username
})

const username = computed(() => form.value.username)
const roleDisplay = computed(() => form.value.role_display)

const userInitials = computed(() => {
  if (avatarPreview.value) return ''
  
  if (form.value.first_name && form.value.last_name) {
    return `${form.value.first_name[0]}${form.value.last_name[0]}`.toUpperCase()
  }
  if (form.value.first_name) {
    return form.value.first_name[0].toUpperCase()
  }
  return form.value.username?.[0]?.toUpperCase() || '?'
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const onFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    avatarFile.value = file
    avatarPreview.value = URL.createObjectURL(file)
  }
}

const loadProfile = async () => {
  try {
    const res = await fetch(`${API_URL}/auth/users/me/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const user = await res.json()
      form.value = {
        username: user.username,
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        patronymic: user.patronymic || '',
        email: user.email || '',
        birth_date: user.birth_date || '',
        bio: user.bio || '',
        role_display: user.role_display || '',
        date_joined: user.date_joined || ''
      }
      
      if (user.avatar_url) {
        avatarPreview.value = user.avatar_url
      }
      
      originalForm.value = { ...form.value }
    } else {
      error.value = 'Не удалось загрузить профиль'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
}

const loadUserPosts = async () => {
  try {
    const res = await fetch(`${API_URL}/posts/my_posts/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      userPosts.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки постов:', e)
  } finally {
    userPostsLoading.value = false
  }
}

const loadUserEvents = async () => {
  try {
    const res = await fetch(`${API_URL}/events/my_events/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      userEvents.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки событий:', e)
  } finally {
    userEventsLoading.value = false
  }
}

const loadUserComments = async () => {
  try {
    const res = await fetch(`${API_URL}/comments/my_comments/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      userComments.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки комментариев:', e)
  } finally {
    userCommentsLoading.value = false
  }
}

onMounted(async () => {
  authStore.restoreAuth()
  await loadProfile()
  
  if (authStore.isAuthor || authStore.isEditor) {
    await loadUserPosts()
  }
  
  if (authStore.isEditor) {
    await loadUserEvents()
  }
  
  if (authStore.isAuthenticated) {
    await loadUserComments()
  }
})

const startEditing = () => {
  originalForm.value = { ...form.value }
  isEditing.value = true
  submitError.value = ''
  success.value = ''
}

const cancelEditing = () => {
  form.value = { ...originalForm.value }
  isEditing.value = false
  submitError.value = ''
  success.value = ''
  avatarFile.value = null
}

const updateProfile = async () => {
  submitting.value = true
  submitError.value = ''
  success.value = ''
  
  try {
    const formData = new FormData()
    formData.append('email', form.value.email)
    formData.append('first_name', form.value.first_name)
    formData.append('last_name', form.value.last_name)
    formData.append('patronymic', form.value.patronymic)
    formData.append('birth_date', form.value.birth_date || '')
    formData.append('bio', form.value.bio || '')
    
    if (avatarFile.value) {
      formData.append('avatar', avatarFile.value)
    }
    
    const res = await fetch(`${API_URL}/auth/users/me/update/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const user = await res.json()
      authStore.user = user
      if (process.client) {
        localStorage.setItem('user', JSON.stringify(user))
      }
      
      form.value = {
        ...form.value,
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        patronymic: user.patronymic || '',
        email: user.email || '',
        birth_date: user.birth_date || '',
        bio: user.bio || '',
        role_display: user.role_display || '',
      }
      
      if (user.avatar_url) {
        avatarPreview.value = user.avatar_url
      }
      
      originalForm.value = { ...form.value }
      
      success.value = 'Профиль обновлён!'
      isEditing.value = false
      
      setTimeout(() => {
        success.value = ''
      }, 3000)
      
    } else {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const changePassword = async () => {
  if (!passwordForm.value.old_password || !passwordForm.value.new_password || !passwordForm.value.new_password2) {
    passwordError.value = 'Заполните все поля'
    return
  }
  
  if (passwordForm.value.new_password !== passwordForm.value.new_password2) {
    passwordError.value = 'Новые пароли не совпадают'
    return
  }
  
  if (passwordForm.value.new_password.length < 8) {
    passwordError.value = 'Пароль должен содержать минимум 8 символов'
    return
  }
  
  passwordSubmitting.value = true
  passwordError.value = ''
  passwordSuccess.value = ''
  
  try {
    const res = await fetch(`${API_URL}/auth/users/me/change-password/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        old_password: passwordForm.value.old_password,
        new_password: passwordForm.value.new_password,
        new_password2: passwordForm.value.new_password2
      })
    })
    
    const data = await res.json()
    
    if (res.ok) {
      passwordSuccess.value = 'Пароль успешно изменён!'
      passwordForm.value = {
        old_password: '',
        new_password: '',
        new_password2: ''
      }
      setTimeout(() => {
        passwordSuccess.value = ''
        showChangePassword.value = false
      }, 3000)
    } else {
      passwordError.value = data.old_password || data.detail || 'Ошибка смены пароля'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    passwordError.value = 'Ошибка подключения к серверу'
  } finally {
    passwordSubmitting.value = false
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
```

---

### `frontend/pages/auth/login.vue`

```vue
<template>
  <div class="max-w-md mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">Вход</h1>
    
    <form @submit.prevent="login">
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Имя пользователя</label>
        <input 
          v-model="username" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Пароль</label>
        <input 
          v-model="password" 
          type="password" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <button 
        type="submit" 
        class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
        :disabled="loading"
      >
        {{ loading ? 'Вход...' : 'Войти' }}
      </button>
      
      <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      
      <p class="mt-4 text-center text-gray-600 dark:text-gray-400">
        <button 
          @click="showResetPassword = !showResetPassword"
          class="text-blue-500 dark:text-blue-400 hover:underline"
          type="button"
        >
          {{ showResetPassword ? 'Скрыть' : 'Забыли пароль?' }}
        </button>
      </p>
      
      <p class="mt-2 text-center text-gray-600 dark:text-gray-400">
        Нет аккаунта? <NuxtLink to="/auth/register" class="text-blue-500 dark:text-blue-400 hover:underline">Регистрация</NuxtLink>
      </p>
      
      <div v-if="showResetPassword" class="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
        <h2 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">Восстановление пароля</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
          Введите email или имя пользователя, и мы отправим ссылку для сброса пароля.
        </p>
        
        <form @submit.prevent="requestPasswordReset">
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Email или имя пользователя</label>
            <input 
              v-model="resetEmail" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              placeholder="email@example.com или username"
              required
            >
          </div>
          
          <button 
            type="submit" 
            class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
            :disabled="resetLoading"
          >
            {{ resetLoading ? 'Отправка...' : 'Отправить ссылку' }}
          </button>
          
          <p v-if="resetSuccess" class="mt-3 text-green-500 text-sm">{{ resetSuccess }}</p>
          <p v-if="resetError" class="mt-3 text-red-500 text-sm">{{ resetError }}</p>
        </form>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()
const router = useRouter()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

const showResetPassword = ref(false)
const resetEmail = ref('')
const resetLoading = ref(false)
const resetSuccess = ref('')
const resetError = ref('')

const login = async () => {
  if (!username.value || !password.value) return
  
  loading.value = true
  error.value = ''
  
  try {
    const res = await fetch(`${API_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    })
    
    if (res.ok) {
      const data = await res.json()
      
      const userRes = await fetch(`${API_URL}/auth/users/me/`, {
        headers: {
          'Authorization': `Bearer ${data.access}`
        }
      })
      
      if (userRes.ok) {
        const user = await userRes.json()
        authStore.setAuth(user, data.access, data.refresh)
        router.push('/')
      }
    } else {
      const data = await res.json()
      error.value = data.detail || 'Неверное имя пользователя или пароль'
    }
  } catch (e) {
    error.value = 'Ошибка подключения к серверу'
    console.error(e)
  } finally {
    loading.value = false
  }
}

const requestPasswordReset = async () => {
  if (!resetEmail.value.trim()) {
    resetError.value = 'Введите email или имя пользователя'
    return
  }
  
  resetLoading.value = true
  resetError.value = ''
  resetSuccess.value = ''
  
  try {
    const isEmail = resetEmail.value.includes('@')
    const requestBody = isEmail 
      ? { email: resetEmail.value } 
      : { username: resetEmail.value }
    
    const res = await fetch(`${API_URL}/auth/password-reset/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    })
    
    const data = await res.json()
    
    if (res.ok) {
      resetSuccess.value = data.detail || 'Ссылка отправлена на email'
      resetEmail.value = ''
      setTimeout(() => {
        showResetPassword.value = false
        resetSuccess.value = ''
      }, 5000)
    } else {
      resetError.value = data.detail || data.message || 'Ошибка отправки'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    resetError.value = 'Ошибка подключения к серверу'
  } finally {
    resetLoading.value = false
  }
}
</script>
```

---

### `frontend/pages/auth/register.vue`

```vue
<template>
  <div class="max-w-md mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">Регистрация</h1>
    
    <form @submit.prevent="register">
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Имя пользователя *</label>
        <input 
          v-model="username" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Email *</label>
        <input 
          v-model="email" 
          type="email" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Пароль *</label>
        <input 
          v-model="password" 
          type="password" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Подтвердите пароль *</label>
        <input 
          v-model="password2" 
          type="password" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <button 
        type="submit" 
        class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
        :disabled="loading"
      >
        {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
      </button>
      
      <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      <p v-if="successMessage" class="mt-4 text-green-500 text-sm">{{ successMessage }}</p>
      <p class="mt-4 text-center text-gray-600 dark:text-gray-400">
        Уже есть аккаунт? <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">Вход</NuxtLink>
      </p>
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const password2 = ref('')
const loading = ref(false)
const error = ref('')
const successMessage = ref('')

const register = async () => {
  if (!username.value || !email.value || !password.value || !password2.value) {
    error.value = 'Заполните все поля'
    return
  }
  
  if (password.value !== password2.value) {
    error.value = 'Пароли не совпадают'
    return
  }
  
  loading.value = true
  error.value = ''
  successMessage.value = ''
  
  try {
    const res = await fetch(`${API_URL}/auth/register/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value,
        password2: password2.value
      })
    })
    
    const data = await res.json()
    
    if (res.ok) {
      successMessage.value = 'Регистрация успешна! Теперь вы можете войти.'
      error.value = ''
      username.value = ''
      email.value = ''
      password.value = ''
      password2.value = ''
    } else {
      if (data.email) {
        error.value = `Email: ${data.email.join(', ')}`
      } else if (data.username) {
        error.value = `Имя пользователя: ${data.username.join(', ')}`
      } else if (data.password) {
        error.value = `Пароль: ${data.password.join(', ')}`
      } else if (data.detail) {
        error.value = data.detail
      } else {
        error.value = JSON.stringify(data)
      }
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
}
</script>
```

---

### `frontend/pages/contacts/index.vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 mb-6">📞 Контакты</h1>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-10 text-red-500">
      {{ error }}
    </div>
    
    <div v-else-if="contact" class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 transition-colors duration-200">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">🏛️ О нас</h2>
          <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">
            {{ contact.description }}
          </p>
        </div>
        
        <div>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">📋 Контактная информация</h2>
          <ul class="space-y-3 text-gray-600 dark:text-gray-300">
            <li class="flex items-start gap-3">
              <span class="text-lg">📍</span>
              <span>{{ contact.address }}</span>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-lg">📞</span>
              <a :href="`tel:${contact.phone}`" class="hover:text-blue-500 transition">
                {{ contact.phone }}
              </a>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-lg">✉️</span>
              <a :href="`mailto:${contact.email}`" class="hover:text-blue-500 transition">
                {{ contact.email }}
              </a>
            </li>
            <li class="flex items-start gap-3">
              <span class="text-lg">🕐</span>
              <span>{{ contact.work_hours }}</span>
            </li>
          </ul>
          
          <div v-if="contact.instagram || contact.vk || contact.telegram" class="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
            <h3 class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-2">Мы в соцсетях</h3>
            <div class="flex gap-3">
              <a v-if="contact.instagram" :href="contact.instagram" target="_blank" class="text-pink-500 hover:text-pink-600 transition text-2xl">
                📸
              </a>
              <a v-if="contact.vk" :href="contact.vk" target="_blank" class="text-blue-500 hover:text-blue-600 transition text-2xl">
                💙
              </a>
              <a v-if="contact.telegram" :href="contact.telegram" target="_blank" class="text-blue-400 hover:text-blue-500 transition text-2xl">
                ✈️
              </a>
            </div>
          </div>
          
          <div v-if="authStore.isEditor" class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
            <NuxtLink 
              to="/contacts/edit" 
              class="inline-block bg-yellow-500 text-white px-6 py-2 rounded-lg hover:bg-yellow-600 transition"
            >
              ✏️ Редактировать контакты
            </NuxtLink>
          </div>
          
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-4">
            Обновлено: {{ formatDate(contact.updated_at) }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const contact = ref(null)
const loading = ref(true)
const error = ref('')

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const res = await fetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      contact.value = await res.json()
    } else {
      error.value = 'Не удалось загрузить контакты'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})
</script>
```

---

### `frontend/pages/contacts/edit.vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">✏️ Редактировать контакты</h1>
    
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут редактировать контакты.</p>
      <NuxtLink to="/contacts" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        К контактам
      </NuxtLink>
    </div>
    
    <div v-else-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <form v-else @submit.prevent="updateContact">
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Адрес</label>
        <input 
          v-model="form.address" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Телефон</label>
        <input 
          v-model="form.phone" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Email</label>
        <input 
          v-model="form.email" 
          type="email" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Часы работы</label>
        <input 
          v-model="form.work_hours" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Описание</label>
        <textarea 
          v-model="form.description" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
          rows="4"
        ></textarea>
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Instagram (ссылка)</label>
        <input 
          v-model="form.instagram" 
          type="url" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          placeholder="https://instagram.com/..."
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">ВКонтакте (ссылка)</label>
        <input 
          v-model="form.vk" 
          type="url" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          placeholder="https://vk.com/..."
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Telegram (ссылка)</label>
        <input 
          v-model="form.telegram" 
          type="url" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          placeholder="https://t.me/..."
        >
      </div>
      
      <div class="flex gap-3">
        <button 
          type="submit" 
          class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
          :disabled="submitting"
        >
          {{ submitting ? 'Сохранение...' : 'Сохранить' }}
        </button>
        <NuxtLink 
          to="/contacts" 
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Отмена
        </NuxtLink>
      </div>
      
      <p v-if="submitError" class="mt-4 text-red-500 text-sm">{{ submitError }}</p>
      <p v-if="success" class="mt-4 text-green-500 text-sm">{{ success }}</p>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()
const router = useRouter()

const loading = ref(true)
const submitting = ref(false)
const submitError = ref('')
const success = ref('')

const form = ref({
  address: '',
  phone: '',
  email: '',
  work_hours: '',
  description: '',
  instagram: '',
  vk: '',
  telegram: '',
})

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const res = await fetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      const data = await res.json()
      form.value = {
        address: data.address || '',
        phone: data.phone || '',
        email: data.email || '',
        work_hours: data.work_hours || '',
        description: data.description || '',
        instagram: data.instagram || '',
        vk: data.vk || '',
        telegram: data.telegram || '',
      }
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})

const updateContact = async () => {
  submitting.value = true
  submitError.value = ''
  success.value = ''
  
  try {
    const res = await fetch(`${API_URL}/contact-info/update/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(form.value)
    })
    
    if (res.ok) {
      success.value = 'Контактная информация обновлена!'
      setTimeout(() => {
        router.push('/contacts')
      }, 1500)
    } else {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>
```

---

### `frontend/pages/posts/index.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">📝 Все публикации</h1>
      <NuxtLink 
        v-if="authStore.isAuthor || authStore.isEditor"
        to="/posts/create" 
        class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        ➕ Создать пост
      </NuxtLink>
    </div>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="posts.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">Нет публикаций. Создайте первую!</p>
    </div>
    
    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="post in posts" 
          :key="post.id" 
          class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-lg transition overflow-hidden flex flex-col"
        >
          <div v-if="post.display_image" class="h-48 overflow-hidden flex-shrink-0">
            <img :src="post.display_image" :alt="post.title" class="w-full h-full object-cover">
          </div>
          <div v-else class="h-48 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-600 flex items-center justify-center flex-shrink-0">
            <span class="text-gray-400 dark:text-gray-500 text-4xl">📝</span>
          </div>
          
          <div class="p-5 flex flex-col flex-1">
            <NuxtLink :to="`/posts/${post.id}`" class="flex-1">
              <div class="flex items-center gap-2">
                <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
                  {{ post.title }}
                </h2>
                <span 
                  v-if="!post.is_published && (authStore.user?.username === post.author_name || authStore.isEditor)"
                  class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-1 rounded-full flex-shrink-0"
                >
                  Черновик
                </span>
              </div>
              <p class="text-gray-600 dark:text-gray-400 text-sm">Автор: {{ post.author_name }}</p>
              <p class="text-gray-700 dark:text-gray-300 mt-2 line-clamp-3">{{ post.excerpt || post.content?.substring(0, 200) }}...</p>
            </NuxtLink>
            
            <div class="flex justify-between items-center mt-4 pt-4 border-t border-gray-100 dark:border-gray-700">
              <div class="flex items-center gap-4 text-sm text-gray-400 dark:text-gray-500">
                <div class="flex items-center gap-1">
                  <img 
                    v-if="post.author_avatar" 
                    :src="post.author_avatar" 
                    :alt="post.author_name"
                    class="w-5 h-5 rounded-full object-cover"
                  >
                  <div 
                    v-else
                    class="w-5 h-5 rounded-full bg-blue-500 flex items-center justify-center text-white text-[8px] font-bold"
                  >
                    {{ getInitials(post.author_name) }}
                  </div>
                  <span>{{ post.author_name }}</span>
                </div>
                <span>👁️ {{ post.views || 0 }}</span>
                <span>💬 {{ post.comments?.length || 0 }}</span>
                <LikeButton 
                  :post-id="post.id"
                  :initial-likes-count="post.likes_count || 0"
                  :initial-is-liked="post.user_has_liked || false"
                  @update="(data) => { 
                    post.likes_count = data.likesCount; 
                    post.user_has_liked = data.isLiked; 
                  }"
                />
              </div>
              <span class="text-sm text-gray-400 dark:text-gray-500">{{ formatDate(post.created_at) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const posts = ref([])
const loading = ref(true)

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/posts/`, { headers })
    posts.value = await res.json()
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
```

---

### `frontend/pages/posts/create.vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="!authStore.isAuthor && !authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только авторы и главные редакторы могут создавать посты.</p>
      <NuxtLink to="/" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        На главную
      </NuxtLink>
    </div>

    <template v-else>
      <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">✏️ Создать пост</h1>
      
      <form @submit.prevent="createPost" enctype="multipart/form-data">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Заголовок *</label>
          <input 
            v-model="title" 
            type="text" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Краткое описание</label>
          <input 
            v-model="excerpt" 
            type="text" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            placeholder="Короткое описание..."
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Содержание *</label>
          <textarea 
            v-model="content" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
            rows="10" 
            required
            placeholder="Текст поста..."
          ></textarea>
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Изображение</label>
          <div class="flex flex-col gap-2">
            <input 
              v-model="image_url" 
              type="url" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              placeholder="https://example.com/image.jpg"
            >
            <div class="flex items-center gap-2">
              <span class="text-gray-500 dark:text-gray-400 text-sm">или</span>
              <input 
                type="file" 
                accept="image/*"
                @change="onFileSelected"
                class="flex-1 border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm"
              >
            </div>
          </div>
          <div v-if="imagePreview" class="mt-2">
            <img :src="imagePreview" alt="Превью" class="h-32 w-auto rounded-lg object-cover">
            <button 
              @click="removeImage"
              type="button"
              class="mt-1 text-red-500 text-sm hover:text-red-700 transition"
            >
              Удалить изображение
            </button>
          </div>
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Добавьте ссылку на изображение или загрузите файл</p>
        </div>
        
        <div class="mb-6">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Статус публикации</label>
          <div class="flex gap-6">
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                type="radio" 
                :value="true" 
                v-model="is_published"
                class="w-4 h-4 text-blue-500"
              >
              <span class="text-gray-700 dark:text-gray-300">Опубликовать</span>
            </label>
            <label class="flex items-center gap-2 cursor-pointer">
              <input 
                type="radio" 
                :value="false" 
                v-model="is_published"
                class="w-4 h-4 text-gray-400"
              >
              <span class="text-gray-700 dark:text-gray-300">Сохранить как черновик</span>
            </label>
          </div>
        </div>
        
        <div class="flex gap-3">
          <button 
            type="submit" 
            class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
            :disabled="submitting"
          >
            {{ submitting ? 'Создание...' : is_published ? 'Опубликовать' : 'Сохранить черновик' }}
          </button>
          <button 
            type="button"
            @click="cancel"
            class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
          >
            Отменить
          </button>
        </div>
        
        <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()
const router = useRouter()

const title = ref('')
const excerpt = ref('')
const content = ref('')
const image_url = ref('')
const is_published = ref(true)
const submitting = ref(false)
const error = ref('')

const imageFile = ref(null)
const imagePreview = ref('')

const onFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
    image_url.value = ''
  }
}

const removeImage = () => {
  imageFile.value = null
  imagePreview.value = ''
  image_url.value = ''
}

const createPost = async () => {
  if (!title.value || !content.value) {
    error.value = 'Заполните заголовок и содержание'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    let finalImageUrl = image_url.value || null
    
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('image', imageFile.value)
      
      const uploadRes = await fetch(`${API_URL}/posts/upload-image/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        },
        body: formData
      })
      
      if (uploadRes.ok) {
        const data = await uploadRes.json()
        finalImageUrl = data.image_url
      } else {
        const err = await uploadRes.json()
        error.value = err.detail || 'Ошибка загрузки изображения'
        submitting.value = false
        return
      }
    }
    
    const res = await fetch(`${API_URL}/posts/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        title: title.value,
        excerpt: excerpt.value,
        content: content.value,
        image_url: finalImageUrl,
        is_published: is_published.value
      })
    })
    
    if (res.ok) {
      const post = await res.json()
      router.push(`/posts/${post.id}`)
    } else {
      const data = await res.json()
      error.value = data.detail || 'Ошибка создания поста'
    }
  } catch (e) {
    error.value = 'Ошибка подключения к серверу'
    console.error(e)
  } finally {
    submitting.value = false
  }
}

const cancel = () => {
  router.push('/')
}
</script>
```

---

### `frontend/pages/posts/[id].vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <NuxtLink to="/posts" class="text-blue-500 dark:text-blue-400 hover:underline mb-4 inline-block">
      ← Назад к списку
    </NuxtLink>

    <div v-if="post" class="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
      <div v-if="post.image_url" class="w-full max-h-96 overflow-hidden">
        <img :src="post.image_url" :alt="post.title" class="w-full h-full object-cover">
      </div>
      
      <div class="p-8">
        <div class="flex justify-between items-start mb-2">
          <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">{{ post.title }}</h1>
          
          <div 
            v-if="authStore.isAuthenticated && (authStore.user?.username === post.author_name || authStore.isEditor)" 
            class="flex gap-2 flex-shrink-0 ml-4"
          >
            <NuxtLink 
              :to="`/posts/edit-${post.id}`" 
              class="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition text-sm"
            >
              ✏️ Редактировать
            </NuxtLink>
            
            <button 
              @click="deletePost" 
              class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition text-sm disabled:opacity-50"
              :disabled="deleting"
            >
              {{ deleting ? 'Удаление...' : '🗑️ Удалить' }}
            </button>
          </div>
        </div>
        
        <div class="flex items-center gap-4 mt-2">
          <span 
            v-if="!post.is_published && (authStore.user?.username === post.author_name || authStore.isEditor)"
            class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-1 rounded-full"
          >
            📄 Черновик
          </span>
        </div>
        
        <!-- Автор с аватаркой -->
        <div class="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400 mb-2">
          <img 
            v-if="post.author_avatar" 
            :src="post.author_avatar" 
            :alt="post.author_name"
            class="w-6 h-6 rounded-full object-cover"
          >
          <div 
            v-else
            class="w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center text-white text-[10px] font-bold"
          >
            {{ getInitials(post.author_name) }}
          </div>
          <span>Автор: {{ post.author_name }}</span>
          <span class="text-gray-400 dark:text-gray-500">|</span>
          <span>{{ formatDate(post.created_at) }}</span>
        </div>
        
        <!-- ПРОСМОТРЫ -->
        <p class="text-gray-500 dark:text-gray-400 text-sm mb-2">
          👁️ {{ post.views || 0 }} просмотров
        </p>
        
        <div class="flex items-center gap-6 mb-4 text-sm text-gray-500 dark:text-gray-400">
          <LikeButton 
            :post-id="post.id"
            :initial-likes-count="post.likes_count || 0"
            :initial-is-liked="post.user_has_liked || false"
            @update="(data) => { 
              post.likes_count = data.likesCount; 
              post.user_has_liked = data.isLiked; 
            }"
          />
          <span>💬 {{ post.comments?.length || 0 }} комментариев</span>
        </div>
        
        <div class="text-gray-800 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">
          {{ post.content }}
        </div>
      </div>
    </div>

    <!-- Комментарии -->
    <div v-if="post" class="mt-8 bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">
        💬 Комментарии ({{ totalCommentsCount }})
      </h2>

      <div v-if="post.comments?.length === 0" class="text-gray-500 dark:text-gray-400">
        Пока нет комментариев. Будьте первым!
      </div>

      <div v-else>
        <CommentItem 
          v-for="comment in post.comments" 
          :key="comment.id"
          :comment="comment"
          :editing-id="editingCommentId"
          :saving-edit="savingEdit"
          @start-edit="startEditComment"
          @start-reply="(commentId, authorName) => startReplyComment(commentId, authorName)"
          @save-edit="saveEditComment"
          @cancel-edit="cancelEditComment"
          @delete-comment="deleteComment"
        />
      </div>
    </div>

    <!-- Форма добавления комментария -->
    <div v-if="post" class="mt-6 bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
      <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">
        {{ replyToCommentId ? 'Ответ на комментарий' : 'Добавить комментарий' }}
      </h3>
      
      <div v-if="replyToCommentId" class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg mb-3 border border-gray-200 dark:border-gray-600">
        <p class="text-sm text-gray-600 dark:text-gray-300">
          Ответ для <span class="font-semibold">{{ replyToAuthorName }}</span>:
        </p>
        <button 
          @click="cancelReply"
          class="text-red-500 text-sm hover:text-red-700 transition"
        >
          Отменить ответ
        </button>
      </div>
      
      <form v-if="authStore.isAuthenticated" @submit.prevent="submitComment">
        <textarea 
          v-model="newComment" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
          rows="3" 
          placeholder="Напишите ваш комментарий..."
          required
        ></textarea>
        <button 
          type="submit" 
          class="mt-2 bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition disabled:opacity-50"
          :disabled="submitting"
        >
          {{ submitting ? 'Отправка...' : replyToCommentId ? 'Ответить' : 'Отправить' }}
        </button>
      </form>
      
      <div v-else class="text-center py-3 text-gray-500 dark:text-gray-400">
        <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">
          Войдите
        </NuxtLink>, чтобы оставить комментарий
      </div>
    </div>

    <div v-else-if="loading" class="text-center py-20 text-gray-500 dark:text-gray-400">
      Загрузка поста...
    </div>

    <div v-else class="text-center py-20 text-red-500">
      Пост не найден
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const post = ref(null)
const loading = ref(true)
const newComment = ref('')
const submitting = ref(false)
const replyToCommentId = ref(null)
const replyToAuthorName = ref('')
const editingCommentId = ref(null)
const savingEdit = ref(false)
const deleting = ref(false)

const totalCommentsCount = computed(() => {
  if (!post.value?.comments) return 0
  let count = 0
  const countComments = (comments) => {
    comments.forEach(c => {
      count++
      if (c.replies && c.replies.length > 0) {
        countComments(c.replies)
      }
    })
  }
  countComments(post.value.comments)
  return count
})

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const id = route.params.id
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/posts/${id}/`, { headers })
    
    if (res.ok) {
      post.value = await res.json()
    } else {
      router.push('/posts')
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})

const submitComment = async () => {
  if (!newComment.value.trim()) return
  
  submitting.value = true
  
  try {
    const body = {
      post: post.value.id,
      content: newComment.value.trim()
    }
    
    if (replyToCommentId.value) {
      body.parent = replyToCommentId.value
    }
    
    const res = await fetch(`${API_URL}/comments/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(body)
    })
    
    if (res.ok) {
      const comment = await res.json()
      
      if (replyToCommentId.value) {
        const parentComment = findComment(post.value.comments, replyToCommentId.value)
        if (parentComment) {
          if (!parentComment.replies) {
            parentComment.replies = []
          }
          parentComment.replies.push(comment)
        }
      } else {
        if (post.value.comments) {
          post.value.comments.push(comment)
        } else {
          post.value.comments = [comment]
        }
      }
      
      newComment.value = ''
      cancelReply()
    } else {
      const error = await res.json()
      console.error('Ошибка сервера:', error)
      alert('Ошибка при отправке комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    submitting.value = false
  }
}

const findComment = (comments, id) => {
  if (!comments) return null
  for (const comment of comments) {
    if (comment.id === id) {
      return comment
    }
    if (comment.replies && comment.replies.length > 0) {
      const found = findComment(comment.replies, id)
      if (found) return found
    }
  }
  return null
}

const startReplyComment = (commentId, authorName) => {
  replyToCommentId.value = commentId
  replyToAuthorName.value = authorName
  const form = document.querySelector('form')
  if (form) {
    form.scrollIntoView({ behavior: 'smooth' })
  }
}

const cancelReply = () => {
  replyToCommentId.value = null
  replyToAuthorName.value = ''
}

const startEditComment = (comment) => {
  editingCommentId.value = comment.id
}

const cancelEditComment = () => {
  editingCommentId.value = null
}

const saveEditComment = async (commentId, content) => {
  if (!content.trim()) return
  
  savingEdit.value = true
  
  try {
    const res = await fetch(`${API_URL}/comments/${commentId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        content: content.trim()
      })
    })
    
    if (res.ok) {
      const updatedComment = await res.json()
      
      const updateCommentInTree = (comments) => {
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].id === commentId) {
            comments[i] = updatedComment
            return true
          }
          if (comments[i].replies && comments[i].replies.length > 0) {
            if (updateCommentInTree(comments[i].replies)) {
              return true
            }
          }
        }
        return false
      }
      
      updateCommentInTree(post.value.comments)
      cancelEditComment()
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при редактировании комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    savingEdit.value = false
  }
}

const deleteComment = async (commentId) => {
  if (!confirm('Вы уверены, что хотите удалить этот комментарий?')) return
  
  try {
    const res = await fetch(`${API_URL}/comments/${commentId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const removeCommentFromTree = (comments) => {
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].id === commentId) {
            comments.splice(i, 1)
            return true
          }
          if (comments[i].replies && comments[i].replies.length > 0) {
            if (removeCommentFromTree(comments[i].replies)) {
              return true
            }
          }
        }
        return false
      }
      
      removeCommentFromTree(post.value.comments)
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
      alert('Ошибка при удалении комментария')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

const deletePost = async () => {
  if (!confirm(`Вы уверены, что хотите удалить пост "${post.value.title}"?`)) return
  
  deleting.value = true
  
  try {
    const res = await fetch(`${API_URL}/posts/${post.value.id}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      router.push('/posts')
    } else {
      alert('Ошибка при удалении поста')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    deleting.value = false
  }
}
</script>
```
---

### `frontend/pages/posts/edit-[id].vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">✏️ Редактировать пост</h1>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-10 text-red-500">
      {{ error }}
    </div>
    
    <form v-else @submit.prevent="updatePost" enctype="multipart/form-data">
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Заголовок *</label>
        <input 
          v-model="form.title" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          required
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Краткое описание</label>
        <input 
          v-model="form.excerpt" 
          type="text" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          placeholder="Короткое описание..."
        >
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Содержание *</label>
        <textarea 
          v-model="form.content" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
          rows="10" 
          required
          placeholder="Текст поста..."
        ></textarea>
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Изображение</label>
        <div class="flex flex-col gap-2">
          <input 
            v-model="form.image_url" 
            type="url" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            placeholder="https://example.com/image.jpg"
          >
          <div class="flex items-center gap-2">
            <span class="text-gray-500 dark:text-gray-400 text-sm">или</span>
            <input 
              type="file" 
              accept="image/*"
              @change="onFileSelected"
              class="flex-1 border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm"
            >
          </div>
        </div>
        <div v-if="imagePreview || form.image_url" class="mt-2 flex items-center gap-3">
          <img 
            :src="imagePreview || form.image_url" 
            alt="Превью" 
            class="h-32 w-auto rounded-lg object-cover"
          >
          <button 
            @click="removeImage"
            type="button"
            class="text-red-500 text-sm hover:text-red-700 transition"
          >
            Удалить изображение
          </button>
        </div>
        <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Добавьте ссылку на изображение или загрузите файл</p>
      </div>
      
      <div class="mb-6">
        <label class="block text-gray-700 dark:text-gray-300 mb-2">Статус публикации</label>
        <div class="flex gap-6">
          <label class="flex items-center gap-2 cursor-pointer">
            <input 
              type="radio" 
              :value="true" 
              v-model="form.is_published"
              class="w-4 h-4 text-blue-500"
            >
            <span class="text-gray-700 dark:text-gray-300">Опубликовать</span>
          </label>
          <label class="flex items-center gap-2 cursor-pointer">
            <input 
              type="radio" 
              :value="false" 
              v-model="form.is_published"
              class="w-4 h-4 text-gray-400"
            >
            <span class="text-gray-700 dark:text-gray-300">Сохранить как черновик</span>
          </label>
        </div>
      </div>
      
      <div class="flex gap-3">
        <button 
          type="submit" 
          class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
          :disabled="submitting"
        >
          {{ submitting ? 'Сохранение...' : form.is_published ? 'Опубликовать' : 'Сохранить черновик' }}
        </button>
        <button 
          type="button"
          @click="cancel"
          class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
        >
          Отменить
        </button>
        <button 
          type="button"
          @click="deletePost"
          class="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition"
        >
          🗑️ Удалить пост
        </button>
      </div>
      
      <p v-if="submitError" class="mt-4 text-red-500 text-sm">{{ submitError }}</p>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const submitError = ref('')

// === ЗАГРУЗКА ИЗОБРАЖЕНИЯ ===
const imageFile = ref(null)
const imagePreview = ref('')

const form = ref({
  title: '',
  excerpt: '',
  content: '',
  image_url: '',
  is_published: true
})

const getPostId = () => {
  const id = route.params.id
  if (typeof id === 'string' && id.includes('edit-')) {
    return id.replace('edit-', '')
  }
  return id
}

const onFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
    form.value.image_url = ''
  }
}

const removeImage = () => {
  imageFile.value = null
  imagePreview.value = ''
  form.value.image_url = ''
}

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const id = getPostId()
    const res = await fetch(`${API_URL}/posts/${id}/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const post = await res.json()
      
      if (post.author_name !== authStore.user?.username && !authStore.isEditor) {
        router.push(`/posts/${id}`)
        return
      }
      
      form.value = {
        title: post.title,
        excerpt: post.excerpt || '',
        content: post.content,
        image_url: post.image_url || '',
        is_published: post.is_published
      }
      if (post.image_url) {
        imagePreview.value = post.image_url
      }
    } else {
      error.value = 'Пост не найден'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})

const updatePost = async () => {
  if (!form.value.title || !form.value.content) {
    submitError.value = 'Заполните заголовок и содержание'
    return
  }
  
  submitting.value = true
  submitError.value = ''
  
  try {
    let finalImageUrl = form.value.image_url || null
    
    // Если есть файл — загружаем его
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('image', imageFile.value)
      
      const uploadRes = await fetch(`${API_URL}/posts/upload-image/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        },
        body: formData
      })
      
      if (uploadRes.ok) {
        const data = await uploadRes.json()
        finalImageUrl = data.image_url
      } else {
        const err = await uploadRes.json()
        submitError.value = err.detail || 'Ошибка загрузки изображения'
        submitting.value = false
        return
      }
    }
    
    const id = getPostId()
    const res = await fetch(`${API_URL}/posts/${id}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        title: form.value.title,
        excerpt: form.value.excerpt,
        content: form.value.content,
        image_url: finalImageUrl,
        is_published: form.value.is_published
      })
    })
    
    if (res.ok) {
      const post = await res.json()
      router.push(`/posts/${post.id}`)
    } else {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const cancel = () => {
  const id = getPostId()
  router.push(`/posts/${id}`)
}

const deletePost = async () => {
  if (!confirm(`Вы уверены, что хотите удалить пост "${form.value.title}"?`)) return
  
  try {
    const id = getPostId()
    const res = await fetch(`${API_URL}/posts/${id}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      router.push('/posts')
    } else {
      alert('Ошибка при удалении поста')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}
</script>
```

---

### `frontend/pages/reset-password/[uidb64]/[token].vue`

```vue
<template>
  <div class="max-w-md mx-auto mt-20 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Проверка ссылки...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">❌</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Ошибка</h2>
      <p class="text-gray-600 dark:text-gray-400">{{ errorMessage }}</p>
      <NuxtLink 
        to="/auth/login" 
        class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        На страницу входа
      </NuxtLink>
    </div>
    
    <div v-else-if="success" class="text-center py-10">
      <div class="text-green-500 text-6xl mb-4">✅</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Пароль изменён!</h2>
      <p class="text-gray-600 dark:text-gray-400">Теперь вы можете войти с новым паролем.</p>
      <NuxtLink 
        to="/auth/login" 
        class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        Перейти к входу
      </NuxtLink>
    </div>
    
    <div v-else class="text-center py-10">
      <div class="text-blue-500 text-6xl mb-4">🔑</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Создайте новый пароль</h2>
      
      <form @submit.prevent="resetPassword" class="mt-6 text-left">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Новый пароль</label>
          <input 
            v-model="newPassword" 
            type="password" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
            minlength="8"
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Подтвердите пароль</label>
          <input 
            v-model="newPassword2" 
            type="password" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
            minlength="8"
          >
        </div>
        
        <button 
          type="submit" 
          class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
          :disabled="submitting"
        >
          {{ submitting ? 'Сохранение...' : 'Сохранить новый пароль' }}
        </button>
        
        <p v-if="formError" class="mt-3 text-red-500 text-sm">{{ formError }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const loading = ref(true)
const error = ref(false)
const success = ref(false)
const submitting = ref(false)
const errorMessage = ref('')
const formError = ref('')
const newPassword = ref('')
const newPassword2 = ref('')

onMounted(async () => {
  try {
    const { uidb64, token } = route.params
    console.log('📡 Проверка ссылки сброса:', uidb64, token)
    
    // Проверяем, что ссылка валидна (делаем GET запрос для проверки)
    // Можно сразу показать форму
    loading.value = false
  } catch (e) {
    console.error('❌ Ошибка:', e)
    error.value = true
    errorMessage.value = 'Неверная ссылка для сброса пароля'
    loading.value = false
  }
})

const resetPassword = async () => {
  if (!newPassword.value || !newPassword2.value) {
    formError.value = 'Заполните все поля'
    return
  }
  
  if (newPassword.value !== newPassword2.value) {
    formError.value = 'Пароли не совпадают'
    return
  }
  
  if (newPassword.value.length < 8) {
    formError.value = 'Пароль должен содержать минимум 8 символов'
    return
  }
  
  submitting.value = true
  formError.value = ''
  
  try {
    const { uidb64, token } = route.params
    
    const res = await fetch(`${API_URL}/auth/password-reset/${uidb64}/${token}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        new_password: newPassword.value,
        new_password2: newPassword2.value
      })
    })
    
    const data = await res.json()
    
    if (res.ok) {
      success.value = true
    } else {
      formError.value = data.detail || 'Ошибка сброса пароля'
    }
  } catch (e) {
    console.error('❌ Ошибка:', e)
    formError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>
```

---

### `frontend/pages/events/index.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">🎭 Афиша</h1>
      <NuxtLink 
        v-if="authStore.isEditor"
        to="/events/create" 
        class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition"
      >
        ➕ Создать событие
      </NuxtLink>
    </div>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="events.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">Пока нет событий. Создайте первое!</p>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <NuxtLink 
        v-for="event in events" 
        :key="event.id" 
        :to="`/events/${event.id}`" 
        class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-lg transition overflow-hidden flex flex-col"
      >
        <div v-if="event.image_url" class="h-48 overflow-hidden flex-shrink-0">
          <img :src="event.image_url" :alt="event.title" class="w-full h-full object-cover">
        </div>
        <div v-else class="h-48 bg-gradient-to-r from-purple-400 to-blue-500 flex items-center justify-center flex-shrink-0">
          <span class="text-white text-4xl">🎭</span>
        </div>
        
        <div class="p-5 flex flex-col flex-1">
          <div class="flex items-center gap-2">
            <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">
              {{ event.title }}
            </h2>
            <span 
              v-if="!event.is_published && authStore.isEditor"
              class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-1 rounded-full flex-shrink-0"
            >
              Черновик
            </span>
          </div>
          <p class="text-gray-600 dark:text-gray-400 text-sm flex-1">{{ event.excerpt || event.content?.substring(0, 120) }}...</p>
          
          <div class="mt-3 flex flex-wrap gap-2 text-sm text-gray-500 dark:text-gray-400">
            <span v-if="event.event_date" class="flex items-center gap-1">
              📅 {{ formatDate(event.event_date) }}
            </span>
            <span v-if="event.location" class="flex items-center gap-1">
              📍 {{ event.location }}
            </span>
            <span v-if="event.price" class="flex items-center gap-1">
              💰 {{ event.price }}
            </span>
          </div>
          
          <div class="mt-3 pt-3 border-t border-gray-100 dark:border-gray-700 flex justify-between items-center">
            <span class="text-sm text-gray-400 dark:text-gray-500">👤 {{ event.author_name }}</span>
            <span v-if="event.is_published" class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-1 rounded-full">
              Опубликовано
            </span>
            <span v-else class="text-xs bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 px-2 py-1 rounded-full">
              Черновик
            </span>
          </div>
        </div>
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const events = ref([])
const loading = ref(true)

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  authStore.restoreAuth()
})

onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/events/`, { headers })
    events.value = await res.json()
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>
```

---

### `frontend/pages/events/[id].vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <NuxtLink to="/events" class="text-blue-500 dark:text-blue-400 hover:underline mb-4 inline-block">
      ← Назад к афише
    </NuxtLink>

    <div v-if="loading" class="text-center py-20 text-gray-500 dark:text-gray-400">
      Загрузка...
    </div>

    <div v-else-if="event" class="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden transition-colors duration-200">
      <div v-if="event.image_url" class="w-full h-96 overflow-hidden">
        <img :src="event.image_url" :alt="event.title" class="w-full h-full object-cover">
      </div>
      <div v-else class="w-full h-96 bg-gradient-to-r from-purple-400 to-blue-500 flex items-center justify-center">
        <span class="text-white text-6xl">🎭</span>
      </div>
      
      <div class="p-8">
        <div class="flex justify-between items-start mb-4">
          <div>
            <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">{{ event.title }}</h1>
            <span 
              v-if="!event.is_published && authStore.isEditor"
              class="text-xs bg-yellow-100 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300 px-2 py-1 rounded-full mt-2 inline-block"
            >
              📄 Черновик
            </span>
          </div>
          
          <div v-if="authStore.isEditor" class="flex gap-2 flex-shrink-0 ml-4">
            <NuxtLink 
              :to="`/events/edit-${event.id}`" 
              class="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition text-sm"
            >
              ✏️ Редактировать
            </NuxtLink>
            <button 
              @click="deleteEvent" 
              class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition text-sm disabled:opacity-50"
              :disabled="deleting"
            >
              {{ deleting ? 'Удаление...' : '🗑️ Удалить' }}
            </button>
          </div>
        </div>
        
        <div class="flex flex-wrap gap-4 mb-4 text-sm text-gray-500 dark:text-gray-400">
          <span v-if="event.event_date" class="flex items-center gap-1">
            📅 {{ formatDate(event.event_date) }}
          </span>
          <span v-if="event.location" class="flex items-center gap-1">
            📍 {{ event.location }}
          </span>
          <span v-if="event.price" class="flex items-center gap-1">
            💰 {{ event.price }}
          </span>
          <span class="flex items-center gap-1">
            👤 {{ event.author_name }}
          </span>
          <span v-if="event.is_published" class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-1 rounded-full">
            Опубликовано
          </span>
          <span v-else class="text-xs bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 px-2 py-1 rounded-full">
            Черновик
          </span>
        </div>
        
        <div class="text-gray-800 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">
          {{ event.content }}
        </div>
      </div>
    </div>

    <div v-else class="text-center py-20 text-red-500">
      Событие не найдено
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const event = ref(null)
const loading = ref(true)
const deleting = ref(false)

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const id = route.params.id
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/events/${id}/`, { headers })
    
    if (res.ok) {
      event.value = await res.json()
    } else {
      router.push('/events')
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})

const deleteEvent = async () => {
  if (!confirm(`Вы уверены, что хотите удалить событие "${event.value.title}"?`)) return
  
  deleting.value = true
  
  try {
    const res = await fetch(`${API_URL}/events/${event.value.id}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      router.push('/events')
    } else {
      alert('Ошибка при удалении события')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    deleting.value = false
  }
}
</script>
```

---

### `frontend/pages/events/create.vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главный редактор может создавать события.</p>
      <NuxtLink to="/events" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        К афише
      </NuxtLink>
    </div>

    <template v-else>
      <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">🎭 Создать событие</h1>
      
      <form @submit.prevent="createEvent" enctype="multipart/form-data">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Название события *</label>
          <input 
            v-model="title" 
            type="text" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Краткое описание</label>
          <input 
            v-model="excerpt" 
            type="text" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            placeholder="Короткое описание..."
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Полное описание *</label>
          <textarea 
            v-model="content" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
            rows="8" 
            required
            placeholder="Подробное описание события..."
          ></textarea>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Дата и время</label>
            <input 
              v-model="event_date" 
              type="datetime-local" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            >
          </div>
          
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Место проведения</label>
            <input 
              v-model="location" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              placeholder="Где пройдёт событие..."
            >
          </div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Стоимость</label>
            <input 
              v-model="price" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              placeholder="Бесплатно / 500 ₽..."
            >
          </div>
          
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Изображение</label>
            <div class="flex flex-col gap-2">
              <input 
                v-model="image_url" 
                type="url" 
                class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                placeholder="https://example.com/image.jpg"
              >
              <div class="flex items-center gap-2">
                <span class="text-gray-500 dark:text-gray-400 text-sm">или</span>
                <input 
                  type="file" 
                  accept="image/*"
                  @change="onFileSelected"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm"
                >
              </div>
            </div>
            <div v-if="imagePreview" class="mt-2">
              <img :src="imagePreview" alt="Превью" class="h-32 w-auto rounded-lg object-cover">
              <button 
                @click="removeImage"
                type="button"
                class="mt-1 text-red-500 text-sm hover:text-red-700 transition"
              >
                Удалить изображение
              </button>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Добавьте ссылку на изображение или загрузите файл</p>
          </div>
        </div>
        
        <div class="mb-4">
          <label class="flex items-center gap-2">
            <input 
              v-model="is_published" 
              type="checkbox" 
              class="w-4 h-4 text-blue-500"
            >
            <span class="text-gray-700 dark:text-gray-300">Опубликовать сразу</span>
          </label>
        </div>
        
        <div class="flex gap-3">
          <button 
            type="submit" 
            class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
            :disabled="submitting"
          >
            {{ submitting ? 'Создание...' : 'Создать' }}
          </button>
          <NuxtLink 
            to="/events" 
            class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
          >
            Отмена
          </NuxtLink>
        </div>
        
        <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()
const router = useRouter()

const title = ref('')
const excerpt = ref('')
const content = ref('')
const event_date = ref('')
const location = ref('')
const price = ref('')
const image_url = ref('')
const is_published = ref(true)
const submitting = ref(false)
const error = ref('')

const imageFile = ref(null)
const imagePreview = ref('')

const onFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
    image_url.value = ''
  }
}

const removeImage = () => {
  imageFile.value = null
  imagePreview.value = ''
  image_url.value = ''
}

const createEvent = async () => {
  if (!title.value || !content.value) {
    error.value = 'Заполните название и описание'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    let finalImageUrl = image_url.value || null
    
    // Если есть файл — загружаем его
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('image', imageFile.value)
      
      const uploadRes = await fetch(`${API_URL}/events/upload-image/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        },
        body: formData
      })
      
      if (uploadRes.ok) {
        const data = await uploadRes.json()
        finalImageUrl = data.image_url
      } else {
        const err = await uploadRes.json()
        error.value = err.detail || 'Ошибка загрузки изображения'
        submitting.value = false
        return
      }
    }
    
    // Создаём событие
    const res = await fetch(`${API_URL}/events/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        title: title.value,
        excerpt: excerpt.value,
        content: content.value,
        event_date: event_date.value || null,
        location: location.value || null,
        price: price.value || null,
        image_url: finalImageUrl,
        is_published: is_published.value
      })
    })
    
    if (res.ok) {
      const event = await res.json()
      router.push(`/events/${event.id}`)
    } else {
      const data = await res.json()
      error.value = data.detail || 'Ошибка создания события'
    }
  } catch (e) {
    error.value = 'Ошибка подключения к серверу'
    console.error(e)
  } finally {
    submitting.value = false
  }
}
</script>
```

---

### `frontend/pages/events/edit-[id].vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главный редактор может создавать события.</p>
      <NuxtLink to="/events" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        К афише
      </NuxtLink>
    </div>

    <template v-else>
      <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">🎭 Создать событие</h1>
      
      <form @submit.prevent="createEvent" enctype="multipart/form-data">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Название события *</label>
          <input 
            v-model="title" 
            type="text" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            required
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Краткое описание</label>
          <input 
            v-model="excerpt" 
            type="text" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            placeholder="Короткое описание..."
          >
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Полное описание *</label>
          <textarea 
            v-model="content" 
            class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" 
            rows="8" 
            required
            placeholder="Подробное описание события..."
          ></textarea>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Дата и время</label>
            <input 
              v-model="event_date" 
              type="datetime-local" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
            >
          </div>
          
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Место проведения</label>
            <input 
              v-model="location" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              placeholder="Где пройдёт событие..."
            >
          </div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Стоимость</label>
            <input 
              v-model="price" 
              type="text" 
              class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
              placeholder="Бесплатно / 500 ₽..."
            >
          </div>
          
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2">Изображение</label>
            <div class="flex flex-col gap-2">
              <input 
                v-model="image_url" 
                type="url" 
                class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
                placeholder="https://example.com/image.jpg"
              >
              <div class="flex items-center gap-2">
                <span class="text-gray-500 dark:text-gray-400 text-sm">или</span>
                <input 
                  type="file" 
                  accept="image/*"
                  @change="onFileSelected"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm"
                >
              </div>
            </div>
            <div v-if="imagePreview" class="mt-2">
              <img :src="imagePreview" alt="Превью" class="h-32 w-auto rounded-lg object-cover">
              <button 
                @click="removeImage"
                type="button"
                class="mt-1 text-red-500 text-sm hover:text-red-700 transition"
              >
                Удалить изображение
              </button>
            </div>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Добавьте ссылку на изображение или загрузите файл</p>
          </div>
        </div>
        
        <div class="mb-4">
          <label class="flex items-center gap-2">
            <input 
              v-model="is_published" 
              type="checkbox" 
              class="w-4 h-4 text-blue-500"
            >
            <span class="text-gray-700 dark:text-gray-300">Опубликовать сразу</span>
          </label>
        </div>
        
        <div class="flex gap-3">
          <button 
            type="submit" 
            class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
            :disabled="submitting"
          >
            {{ submitting ? 'Создание...' : 'Создать' }}
          </button>
          <NuxtLink 
            to="/events" 
            class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-6 py-2 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition"
          >
            Отмена
          </NuxtLink>
        </div>
        
        <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()
const router = useRouter()

const title = ref('')
const excerpt = ref('')
const content = ref('')
const event_date = ref('')
const location = ref('')
const price = ref('')
const image_url = ref('')
const is_published = ref(true)
const submitting = ref(false)
const error = ref('')

const imageFile = ref(null)
const imagePreview = ref('')

const onFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    imagePreview.value = URL.createObjectURL(file)
    image_url.value = ''
  }
}

const removeImage = () => {
  imageFile.value = null
  imagePreview.value = ''
  image_url.value = ''
}

const createEvent = async () => {
  if (!title.value || !content.value) {
    error.value = 'Заполните название и описание'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    let finalImageUrl = image_url.value || null
    
    // Если есть файл — загружаем его
    if (imageFile.value) {
      const formData = new FormData()
      formData.append('image', imageFile.value)
      
      const uploadRes = await fetch(`${API_URL}/events/upload-image/`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        },
        body: formData
      })
      
      if (uploadRes.ok) {
        const data = await uploadRes.json()
        finalImageUrl = data.image_url
      } else {
        const err = await uploadRes.json()
        error.value = err.detail || 'Ошибка загрузки изображения'
        submitting.value = false
        return
      }
    }
    
    // Создаём событие
    const res = await fetch(`${API_URL}/events/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify({
        title: title.value,
        excerpt: excerpt.value,
        content: content.value,
        event_date: event_date.value || null,
        location: location.value || null,
        price: price.value || null,
        image_url: finalImageUrl,
        is_published: is_published.value
      })
    })
    
    if (res.ok) {
      const event = await res.json()
      router.push(`/events/${event.id}`)
    } else {
      const data = await res.json()
      error.value = data.detail || 'Ошибка создания события'
    }
  } catch (e) {
    error.value = 'Ошибка подключения к серверу'
    console.error(e)
  } finally {
    submitting.value = false
  }
}
</script>
```

---

### `frontend/components/Commentitem.vue`

```vue
<template>
  <div class="comment-wrapper">
    <div class="comment-item">
      <div class="flex justify-between items-start">
        <div class="flex items-center gap-2">
          <!-- Аватарка автора комментария -->
          <img 
            v-if="comment.author_avatar" 
            :src="comment.author_avatar" 
            :alt="comment.author_name"
            class="w-6 h-6 rounded-full object-cover flex-shrink-0"
          >
          <div 
            v-else
            class="w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center text-white text-[10px] font-bold flex-shrink-0"
          >
            {{ getInitials(comment.author_name) }}
          </div>
          
          <div>
            <span class="font-semibold text-gray-800 dark:text-white">{{ comment.author_name }}</span>
            <span class="text-gray-400 dark:text-gray-400 text-sm ml-2">{{ formatDate(comment.created_at) }}</span>
            <span v-if="comment.updated_at !== comment.created_at" class="text-gray-400 dark:text-gray-400 text-sm ml-1">
              (изменён)
            </span>
            <button 
              v-if="authStore.isAuthenticated"
              @click="handleReply"
              class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm ml-3"
            >
              Ответить
            </button>
          </div>
        </div>
        
        <div class="flex items-center gap-2">
          <LikeButton 
            :comment-id="comment.id"
            :initial-likes-count="comment.likes_count || 0"
            :initial-is-liked="comment.user_has_liked || false"
            @update="(data) => { 
              comment.likes_count = data.likesCount; 
              comment.user_has_liked = data.isLiked; 
            }"
          />
          
          <button 
            v-if="comment.can_edit"
            @click="$emit('start-edit', comment)"
            class="text-yellow-500 hover:text-yellow-700 transition text-sm"
            title="Редактировать"
          >
            ✏️
          </button>
          
          <button 
            v-if="comment.can_delete"
            @click="$emit('delete-comment', comment.id)"
            class="text-red-500 hover:text-red-700 transition text-sm"
            title="Удалить"
          >
            🗑️
          </button>
        </div>
      </div>
      
      <p v-if="!isEditing" class="text-gray-700 dark:text-gray-200 mt-1">
        {{ comment.content }}
      </p>
      
      <div v-else class="mt-2">
        <textarea 
          v-model="localEditContent" 
          class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
          rows="2"
        ></textarea>
        <div class="flex gap-2 mt-2">
          <button 
            @click="$emit('save-edit', comment.id, localEditContent)"
            class="bg-blue-500 text-white px-4 py-1 rounded-lg hover:bg-blue-600 transition text-sm"
            :disabled="savingEdit"
          >
            {{ savingEdit ? 'Сохранение...' : 'Сохранить' }}
          </button>
          <button 
            @click="$emit('cancel-edit')"
            class="bg-gray-300 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-4 py-1 rounded-lg hover:bg-gray-400 dark:hover:bg-gray-500 transition text-sm"
          >
            Отмена
          </button>
        </div>
      </div>
    </div>

    <div v-if="comment.replies && comment.replies.length > 0" class="replies-container ml-6 pl-4 border-l-2 border-gray-200 dark:border-gray-700">
      <CommentItem 
        v-for="reply in comment.replies" 
        :key="reply.id"
        :comment="reply"
        :editing-id="editingId"
        :saving-edit="savingEdit"
        @start-edit="$emit('start-edit', $event)"
        @start-reply="(...args) => $emit('start-reply', ...args)"
        @save-edit="$emit('save-edit', $event[0], $event[1])"
        @cancel-edit="$emit('cancel-edit')"
        @delete-comment="$emit('delete-comment', $event)"
      />
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()

const props = defineProps({
  comment: {
    type: Object,
    required: true
  },
  editingId: {
    type: Number,
    default: null
  },
  savingEdit: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits([
  'start-edit',
  'start-reply',
  'save-edit',
  'cancel-edit',
  'delete-comment'
])

const isEditing = computed(() => props.editingId === props.comment.id)
const localEditContent = ref('')

watch(() => props.editingId, (newId) => {
  if (newId === props.comment.id) {
    localEditContent.value = props.comment.content
  }
}, { immediate: true })

const handleReply = () => {
  emit('start-reply', props.comment.id, props.comment.author_name)
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<style scoped>
.comment-wrapper {
  margin-bottom: 8px;
}
.comment-item {
  padding: 8px 0;
}
.replies-container {
  margin-top: 4px;
}
</style>
```

---

### `frontend/components/LikeButton.vue`

```vue
<template>
  <button 
    @click="toggleLike"
    :disabled="loading"
    class="flex items-center gap-1 transition hover:scale-110"
    :class="[
      isLiked ? 'text-red-500' : 'text-gray-400 hover:text-red-400',
      loading ? 'opacity-50 cursor-not-allowed' : ''
    ]"
  >
    <span class="text-sm">{{ isLiked ? '❤️' : '🤍' }}</span>
    <span class="text-sm font-medium">{{ likesCount }}</span>
  </button>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const props = defineProps({
  postId: {
    type: Number,
    default: null
  },
  commentId: {
    type: Number,
    default: null
  },
  initialLikesCount: {
    type: Number,
    default: 0
  },
  initialIsLiked: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const likesCount = ref(props.initialLikesCount)
const isLiked = ref(props.initialIsLiked)
const loading = ref(false)

const toggleLike = async () => {
  if (!authStore.isAuthenticated) {
    alert('Войдите в систему, чтобы ставить лайки')
    return
  }
  
  loading.value = true
  
  try {
    const body = {}
    if (props.postId) {
      body.post = props.postId
    } else if (props.commentId) {
      body.comment = props.commentId
    } else {
      console.error('Не указан postId или commentId')
      loading.value = false
      return
    }
    
    const res = await fetch(`${API_URL}/likes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(body)
    })
    
    if (res.ok) {
      const data = await res.json()
      
      if (data.action === 'liked') {
        isLiked.value = true
        likesCount.value += 1
      } else if (data.action === 'unliked') {
        isLiked.value = false
        likesCount.value -= 1
      }
      
      emit('update', {
        likesCount: likesCount.value,
        isLiked: isLiked.value
      })
    } else {
      const error = await res.json()
      console.error('Ошибка:', error)
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
}
</script>
```

---

### `frontend/pages/authors/index.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200 mb-6">✍️ Все авторы</h1>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="authors.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">Пока нет авторов</p>
    </div>
    
    <div v-else>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
        <div 
          v-for="author in authors" 
          :key="author.id" 
          class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow hover:shadow-md transition text-center"
        >
          <!-- Аватарка -->
          <div class="w-20 h-20 mx-auto rounded-full bg-blue-500 flex items-center justify-center text-white text-2xl font-bold overflow-hidden">
            <img v-if="author.avatar_url" :src="author.avatar_url" :alt="author.username" class="w-full h-full object-cover">
            <span v-else>{{ getInitials(author) }}</span>
          </div>
          <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 mt-2">{{ getFullName(author) }}</h3>
          <p class="text-xs text-gray-400 dark:text-gray-500">{{ author.role_display }}</p>
          <NuxtLink 
            :to="`/authors/${author.id}`" 
            class="mt-3 inline-block text-sm text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition"
          >
            Публикации автора →
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authors = ref([])
const loading = ref(true)

const getInitials = (user) => {
  const name = user.full_name || user.username
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const getFullName = (user) => {
  return user.full_name || user.username
}

onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/auth/users/`)
    if (res.ok) {
      const allUsers = await res.json()
      authors.value = allUsers.filter(user => user.role === 'author' || user.role === 'editor')
    }
  } catch (e) {
    console.error('Ошибка загрузки авторов:', e)
  } finally {
    loading.value = false
  }
})
</script>
```

---

### `frontend/pages/authors/[id].vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <NuxtLink to="/" class="text-blue-500 dark:text-blue-400 hover:underline mb-4 inline-block">
      ← На главную
    </NuxtLink>

    <div v-if="author" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg mb-8 transition-colors duration-200">
      <div class="flex items-center gap-6">
        <!-- Аватарка -->
        <div class="w-24 h-24 rounded-full bg-blue-500 flex items-center justify-center text-white text-3xl font-bold overflow-hidden flex-shrink-0">
          <img v-if="author.avatar_url" :src="author.avatar_url" :alt="author.username" class="w-full h-full object-cover">
          <span v-else>{{ getInitials(author) }}</span>
        </div>
        <div>
          <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">{{ getFullName(author) }}</h1>
          <p class="text-gray-500 dark:text-gray-400">{{ author.role_display }}</p>
          <p v-if="author.bio" class="text-gray-600 dark:text-gray-300 mt-2">{{ author.bio }}</p>
        </div>
      </div>
    </div>

    <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">📝 Публикации автора</h2>

    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>

    <div v-else-if="posts.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">У автора пока нет публикаций</p>
    </div>

    <div v-else class="space-y-4">
      <div 
        v-for="post in posts" 
        :key="post.id" 
        class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow hover:shadow-md transition flex gap-4"
      >
        <div v-if="post.image_url" class="h-24 w-24 rounded-lg overflow-hidden flex-shrink-0">
          <img :src="post.image_url" :alt="post.title" class="w-full h-full object-cover">
        </div>
        <div v-else class="h-24 w-24 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-500 rounded-lg flex items-center justify-center flex-shrink-0">
          <span class="text-gray-400 dark:text-gray-500 text-2xl">📝</span>
        </div>
        
        <NuxtLink :to="`/posts/${post.id}`" class="block flex-1">
          <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">{{ post.title }}</h3>
          <p class="text-gray-600 dark:text-gray-400 text-sm">{{ formatDate(post.created_at) }}</p>
          <p class="text-gray-700 dark:text-gray-300 mt-1 line-clamp-2">{{ post.excerpt || post.content?.substring(0, 150) }}...</p>
          <div class="flex items-center gap-4 mt-2 text-sm text-gray-400 dark:text-gray-500">
            <span>💬 {{ post.comments?.length || 0 }}</span>
            <span>❤️ {{ post.likes_count || 0 }}</span>
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const route = useRoute()
const author = ref(null)
const posts = ref([])
const loading = ref(true)

const getInitials = (user) => {
  const name = user.full_name || user.username
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const getFullName = (user) => {
  return user.full_name || user.username
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

onMounted(async () => {
  try {
    const authorId = route.params.id
    
    const authorRes = await fetch(`${API_URL}/auth/users/${authorId}/`)
    if (authorRes.ok) {
      author.value = await authorRes.json()
    }
    
    if (author.value?.username) {
      const headers = {}
      if (authStore.isAuthenticated) {
        headers['Authorization'] = `Bearer ${authStore.accessToken}`
      }
      
      const url = `${API_URL}/posts/?author_name=${author.value.username}`
      const postsRes = await fetch(url, { headers })
      if (postsRes.ok) {
        posts.value = await postsRes.json()
      }
    }
  } catch (e) {
    console.error('Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
```

---

### `frontend/pages/confirm-email/[uidb64]/[token].vue`

```vue
<template>
  <div style="margin-top: 120px;">
    <div class="max-w-md mx-auto bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
      <div v-if="loading" class="text-center py-10">
        <p class="text-gray-500 dark:text-gray-400">Подтверждение...</p>
      </div>
      
      <div v-else-if="success" class="text-center py-10">
        <div class="text-green-500 text-6xl mb-4">✅</div>
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Email подтверждён!</h2>
        <p class="text-gray-600 dark:text-gray-400">Теперь вы можете войти в систему.</p>
        <NuxtLink 
          to="/auth/login" 
          class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          Перейти к входу
        </NuxtLink>
      </div>
      
      <div v-else class="text-center py-10">
        <div class="text-red-500 text-6xl mb-4">❌</div>
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Ошибка подтверждения</h2>
        <p class="text-gray-600 dark:text-gray-400">{{ errorMessage || 'Неверная ссылка подтверждения' }}</p>
        <NuxtLink 
          to="/auth/login" 
          class="mt-6 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          На страницу входа
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const loading = ref(true)
const success = ref(false)
const errorMessage = ref('')

onMounted(async () => {
  try {
    const { uidb64, token } = route.params
    console.log('📡 Подтверждение email:', uidb64, token)
    
    const res = await fetch(`${API_URL}/auth/confirm-email/${uidb64}/${token}/`)
    const data = await res.json()
    console.log('📡 Ответ сервера:', res.status, data)
    
    if (res.ok) {
      success.value = true
    } else {
      errorMessage.value = data.detail || 'Неверная ссылка подтверждения'
    }
  } catch (e) {
    errorMessage.value = 'Ошибка подключения к серверу'
    console.error('❌ Ошибка:', e)
  } finally {
    loading.value = false
  }
})
</script>
```

---

### `frontend/layouts/default.vue`

```vue
<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow">
      <div class="container mx-auto p-4">
        <h1 class="text-2xl font-bold text-gray-800">🏛️ Центр Культуры</h1>
      </div>
    </header>
    <main class="container mx-auto p-4">
      <slot />
    </main>
  </div>
</template>
```

---