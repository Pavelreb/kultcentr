# ПОЛНЫЙ ПРОМТ ПРОЕКТА "ЦЕНТР КУЛЬТУРЫ"

## ОПИСАНИЕ ПРОЕКТА

Сайт "Центр Культуры" — полноценное веб-приложение для публикации статей, новостей, анонсов мероприятий, галереи фотографий и культурных событий. Платформа с системой ролей, где авторы могут делиться публикациями, пользователи — комментировать, а редакторы — управлять контентом.

Проект разработан с использованием современного компонентного подхода, где каждый элемент интерфейса вынесен в отдельный переиспользуемый компонент. Вся логика разделена между бэкендом (Django REST Framework) и фронтендом (Nuxt 3).

---

## СТЕК ТЕХНОЛОГИЙ

### Бэкенд:
- **Python 3.13** — язык программирования
- **Django 6.0.7** — веб-фреймворк
- **Django REST Framework** — создание REST API
- **djangorestframework-simplejwt** — JWT аутентификация
- **django-cors-headers** — CORS заголовки
- **Pillow** — работа с изображениями
- **SQLite** — база данных (разработка)
- **Django Admin** — администрирование

### Фронтенд:
- **Nuxt 4.4.8 (Vue 3)** — фреймворк
- **Tailwind CSS** — стилизация
- **Pinia** — управление состоянием
- **Vue Router** — маршрутизация

---

## ПОЛНЫЙ ФУНКЦИОНАЛ

### 👤 Пользователи и роли

| Роль | Что может |
|------|-----------|
| **Гость** | Смотреть посты, события, авторов, контакты, галерею |
| **Подписчик** | Смотреть + комментировать + редактировать профиль + лайки |
| **Автор** | Всё, что подписчик + создавать/редактировать/удалять свои посты + удалять комментарии под своими постами |
| **Главный редактор** | Всё, что автор + редактировать/удалять любые посты и события + создавать события + удалять любые комментарии + редактировать контакты + управлять баннером + управлять галереей |
| **Админ** | Всё (доступ в админку) |

### 📝 Посты
- CRUD операции
- Изображения (файл или ссылка)
- Черновики
- Лайки
- Комментарии (вложенные)
- Просмотры
- Автоудаление файлов
- Создание через единое меню "Создать" в шапке

### 🎭 Афиша (События)
- CRUD (только редакторы)
- Изображения (файл или ссылка)
- Черновики
- Сортировка по дате (ближайшие первыми)
- Автоудаление файлов
- Создание через единое меню "Создать" в шапке

### 📸 Галерея
- Альбомы с названием, описанием и датой события
- Фотографии в альбомах
- Обложка альбома
- Просмотры фотографий
- Лайки фотографий
- Комментарии к фотографиям (вложенные)
- Lightbox с навигацией и каруселью миниатюр
- Автоудаление файлов
- Создание через единое меню "Создать" в шапке

### 💬 Комментарии
- **К постам**: `/api/comments/` с полем `post`
- **К фото**: `/api/photo-comments/` с полем `photo`
- Создание (только авторизованные)
- Редактирование (только свои)
- Удаление (свои, автор поста, редактор)
- Вложенность
- Лайки
- Аватарки авторов

### ❤️ Лайки
- На посты, комментарии и фотографии
- Только авторизованные

### 👤 Профиль
- Страница просмотра `/profile`
- Страница редактирования `/profile/edit`
- ФИО, дата рождения, аватарка
- Смена пароля
- Мои посты, Мои афиши, Мои комментарии (к постам и галерее)

### 📞 Контакты
- Страница `/contacts` (доступна всем)
- Редактирование в настройках `/settings` (только редакторы)
- Данные в футере (автообновление)

### 🎨 Баннер
- Управление Hero-баннером на главной
- Заголовок и подзаголовок
- Фоновое изображение (файл или ссылка)
- Кнопка с текстом и ссылкой
- Включение/отключение кнопки
- Активность баннера
- Редактирование только для редакторов
- Сброс к дефолтным значениям

### ✍️ Авторы
- Блок на главной
- Страница всех авторов
- Страница автора с публикациями

### 🎨 Дизайн
- Адаптив (мобильные, планшеты, десктоп)
- Тёмная тема (переключение)
- Hero-баннер
- Семантические теги (header, main, footer)
- Компонентный подход
- Единое меню "Создать" в шапке

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

## СТРУКТУРА ПРОЕКТА

```
kultcentr/
├── backend/
│   ├── config/
│   │   ├── settings.py              # Настройки Django
│   │   └── urls.py                  # Корневые URL
│   ├── users/                       # Пользователи
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── utils.py
│   ├── posts/                       # Посты
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── comments/                    # Комментарии к постам
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── events/                      # События
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── likes/                       # Лайки
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── contactinfo/                 # Контакты
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── banner/                      # Баннер
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── gallery/                     # Галерея
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── comment_views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── permissions.py
│   ├── manage.py
│   └── db.sqlite3
├── frontend/
│   ├── components/
│   │   ├── layout/                  # Компоненты макета
│   │   │   ├── AppHeader.vue
│   │   │   ├── AppFooter.vue
│   │   │   └── AppLogo.vue
│   │   ├── common/                  # Общие компоненты
│   │   │   ├── ThemeToggle.vue
│   │   │   ├── BurgerMenu.vue
│   │   │   ├── AuthButtons.vue
│   │   │   └── CreateMenu.vue
│   │   ├── ui/                      # UI-компоненты
│   │   │   ├── UiButton.vue
│   │   │   ├── UiInput.vue
│   │   │   ├── UiTextarea.vue
│   │   │   ├── UiCheckbox.vue
│   │   │   ├── UiCard.vue
│   │   │   └── UiFileInput.vue
│   │   ├── features/                # Компоненты функций
│   │   │   └── banner/
│   │   │       └── HeroBanner.vue
│   │   └── content/                 # Контентные компоненты
│   │       ├── PostCard.vue
│   │       ├── EventCard.vue
│   │       ├── AlbumCard.vue
│   │       └── AuthorCard.vue
│   ├── pages/
│   │   ├── index.vue                # Главная
│   │   ├── profile/                 # Профиль
│   │   │   ├── index.vue            # Просмотр
│   │   │   └── edit.vue             # Редактирование
│   │   ├── settings/
│   │   │   └── index.vue            # Настройки
│   │   ├── contacts/
│   │   │   └── index.vue            # Контакты
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
│   │   ├── gallery/
│   │   │   ├── index.vue
│   │   │   ├── create.vue
│   │   │   ├── [id].vue
│   │   │   └── edit-[id].vue
│   │   ├── authors/
│   │   │   ├── index.vue
│   │   │   └── [id].vue
│   │   └── reset-password/
│   │       └── [uidb64]/
│   │           └── [token].vue
│   ├── store/
│   │   ├── auth.js
│   │   └── theme.js
│   ├── middleware/
│   │   ├── auth.js
│   │   └── editor.js
│   ├── assets/
│   │   └── css/
│   │       └── main.css
│   ├── app.vue
│   ├── nuxt.config.ts
│   └── tailwind.config.js
├── requirements.txt
├── package.json
└── venv/
```

---

## ПОЛНЫЕ ФАЙЛЫ ПРОЕКТА

### БЭКЕНД

#### `backend/manage.py`

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

#### `backend/config/settings.py`

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
    "banner",
    "gallery",
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

#### `backend/config/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('comments.urls')),
    path('api/', include('gallery.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('events.urls')),
    path('api/', include('likes.urls')),
    path('api/auth/', include('users.urls')),
    path('api/contact-info/', include('contactinfo.urls')),
    path('api/banner/', include('banner.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### USERS

#### `backend/users/models.py`

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

#### `backend/users/views.py`

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

#### `backend/users/serializers.py`

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

#### `backend/users/urls.py`

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

#### `backend/users/admin.py`

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

#### `backend/users/utils.py`

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

### POSTS

#### `backend/posts/models.py`

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

#### `backend/posts/views.py`

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

#### `backend/posts/serializers.py`

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

#### `backend/posts/permissions.py`

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

#### `backend/posts/urls.py`

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

#### `backend/posts/admin.py`

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

### COMMENTS (для постов)

#### `backend/comments/models.py`

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

#### `backend/comments/views.py`

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
        if not post_id:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({'post': 'Это поле обязательно'})
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
        print(f'💬 Создан комментарий к посту: {serializer.instance.content[:30]}...')

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

#### `backend/comments/serializers.py`

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

#### `backend/comments/permissions.py`

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

#### `backend/comments/urls.py`

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

#### `backend/comments/admin.py`

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

### EVENTS

#### `backend/events/models.py`

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

#### `backend/events/views.py`

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
    parser_classes = [MultiPartParser, FormParser]

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user = request.user
        
        if instance.is_published:
            if user.role != 'editor':
                return Response({'detail': 'Недостаточно прав'}, status=403)
        else:
            if user.role != 'editor':
                return Response({'detail': 'Недостаточно прав'}, status=403)
        
        data = request.data.copy()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        print(f'📸 Создано событие: {serializer.instance.title}')
    
    def perform_update(self, serializer):
        serializer.save()
        print(f'📸 Обновлено событие: {serializer.instance.title}')

    def perform_destroy(self, instance):
        print(f'🗑️ Удаляем событие: {instance.title}')
        if instance.image:
            file_path = instance.image.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'🗑️ Изображение события удалено: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        instance.delete()

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
        
        filename = f"events/temp_{user.id}_{file.name}"
        file_path = default_storage.save(filename, ContentFile(file.read()))
        file_url = request.build_absolute_uri(settings.MEDIA_URL + file_path)
        
        print(f'📁 Загружено изображение: {file_path}')
        print(f'📁 URL: {file_url}')
        
        return Response({
            'image_url': file_url,
            'detail': 'Изображение загружено'
        }, status=status.HTTP_200_OK)
```

---

#### `backend/events/serializers.py`

```python
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
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
            'image_url': {'required': False, 'allow_null': True, 'allow_blank': True},
        }

    def get_display_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return obj.image_url

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            request = self.context.get('request')
            if request:
                data['image_url'] = request.build_absolute_uri(instance.image.url)
            else:
                data['image_url'] = instance.image.url
        return data

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
        
        if 'image' in validated_data:
            instance.image = validated_data.get('image')
        
        if 'image_url' in validated_data:
            instance.image_url = validated_data.get('image_url')
        
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.save()
        return instance
```

---

#### `backend/events/permissions.py`

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

#### `backend/events/urls.py`

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

#### `backend/events/admin.py`

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

### LIKES

#### `backend/likes/models.py`

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

#### `backend/likes/views.py`

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

#### `backend/likes/serializers.py`

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

#### `backend/likes/urls.py`

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

#### `backend/likes/admin.py`

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

### CONTACTINFO

#### `backend/contactinfo/models.py`

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

#### `backend/contactinfo/views.py`

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

#### `backend/contactinfo/serializers.py`

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

#### `backend/contactinfo/urls.py`

```python
from django.urls import path
from .views import ContactInfoView, ContactInfoUpdateView

urlpatterns = [
    path('', ContactInfoView.as_view(), name='contact_info'),
    path('update/', ContactInfoUpdateView.as_view(), name='contact_info_update'),
]
```

---

#### `backend/contactinfo/admin.py`

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

### BANNER

#### `backend/banner/models.py`

```python
from django.db import models
from django.conf import settings
import os


class Banner(models.Model):
    """Модель для управления Hero-баннером на главной странице"""
    
    title = models.CharField(
        max_length=200,
        default='🏛️ Добро пожаловать в Центр Культуры',
        verbose_name='Заголовок баннера'
    )
    subtitle = models.TextField(
        default='Место, где искусство, традиции и творчество объединяются',
        verbose_name='Подзаголовок'
    )
    
    background_image = models.ImageField(
        upload_to='banner/',
        blank=True,
        null=True,
        verbose_name='Фоновое изображение'
    )
    background_image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на фоновое изображение'
    )
    
    button_text = models.CharField(
        max_length=100,
        default='Смотреть афишу',
        blank=True,
        null=True,
        verbose_name='Текст кнопки'
    )
    button_link = models.CharField(
        max_length=200,
        default='/events',
        blank=True,
        null=True,
        verbose_name='Ссылка кнопки'
    )
    button_enabled = models.BooleanField(
        default=True,
        verbose_name='Кнопка активна'
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name='Баннер активен'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'
    
    def __str__(self):
        return f'Баннер (обновлен: {self.updated_at.strftime("%d.%m.%Y %H:%M")})'
    
    def delete(self, *args, **kwargs):
        if self.background_image:
            file_path = self.background_image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f'🗑️ Фоновое изображение баннера удалено: {file_path}')
        super().delete(*args, **kwargs)
```

---

#### `backend/banner/serializers.py`

```python
from rest_framework import serializers
from .models import Banner


class BannerSerializer(serializers.ModelSerializer):
    background_image_url_display = serializers.SerializerMethodField()
    has_background = serializers.SerializerMethodField()
    
    class Meta:
        model = Banner
        fields = [
            'id',
            'title',
            'subtitle',
            'background_image',
            'background_image_url',
            'background_image_url_display',
            'has_background',
            'button_text',
            'button_link',
            'button_enabled',
            'is_active',
            'updated_at',
        ]
        read_only_fields = ['id', 'updated_at']
    
    def get_background_image_url_display(self, obj):
        if obj.background_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.background_image.url)
            return obj.background_image.url
        return obj.background_image_url
    
    def get_has_background(self, obj):
        return bool(obj.background_image or obj.background_image_url)
```

---

#### `backend/banner/views.py`

```python
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import os
from .models import Banner
from .serializers import BannerSerializer


class BannerView(generics.RetrieveAPIView):
    """Публичный просмотр баннера"""
    permission_classes = [permissions.AllowAny]
    serializer_class = BannerSerializer
    
    def get_object(self):
        banner = Banner.objects.first()
        if not banner:
            banner = Banner.objects.create()
        return banner


class BannerUpdateView(generics.UpdateAPIView):
    """Обновление баннера (только для редакторов)"""
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = BannerSerializer
    
    def get_object(self):
        banner = Banner.objects.first()
        if not banner:
            banner = Banner.objects.create()
        return banner
    
    def update(self, request, *args, **kwargs):
        user = request.user
        
        if user.role != 'editor':
            return Response(
                {'detail': 'Только главные редакторы могут редактировать баннер'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        instance = self.get_object()
        old_background = instance.background_image
        
        data = request.data.copy()
        
        if 'background_image_url' in data and data['background_image_url'] == '':
            data['background_image_url'] = None
        
        if 'background_image' in data and data['background_image'] == '':
            data.pop('background_image', None)
        
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        instance.refresh_from_db()
        if old_background and old_background != instance.background_image:
            file_path = old_background.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'🗑️ Старое фоновое изображение баннера удалено: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        
        response_data = serializer.data
        response_data['background_image_url_display'] = serializer.get_background_image_url_display(instance)
        response_data['has_background'] = serializer.get_has_background(instance)
        
        return Response(response_data)
    
    def perform_update(self, serializer):
        print('=' * 60)
        print('🎨 ОБНОВЛЕНИЕ БАННЕРА')
        print(f'👤 Редактор: {self.request.user.username}')
        print(f'📝 Заголовок: {serializer.validated_data.get("title", "не изменён")}')
        print(f'📝 Подзаголовок: {serializer.validated_data.get("subtitle", "не изменён")}')
        print(f'🔘 Кнопка активна: {serializer.validated_data.get("button_enabled", "не изменён")}')
        print(f'📊 Баннер активен: {serializer.validated_data.get("is_active", "не изменён")}')
        print('=' * 60)
        serializer.save()
```

---

#### `backend/banner/urls.py`

```python
from django.urls import path
from .views import BannerView, BannerUpdateView

urlpatterns = [
    path('', BannerView.as_view(), name='banner'),
    path('update/', BannerUpdateView.as_view(), name='banner_update'),
]
```

---

#### `backend/banner/admin.py`

```python
from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'has_background', 'updated_at']
    list_filter = ['is_active', 'updated_at']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'subtitle', 'is_active')
        }),
        ('Изображение', {
            'fields': ('background_image', 'background_image_url')
        }),
        ('Кнопка', {
            'fields': ('button_text', 'button_link', 'button_enabled')
        }),
        ('Дата обновления', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['updated_at']
    
    def has_background(self, obj):
        return bool(obj.background_image or obj.background_image_url)
    has_background.boolean = True
    has_background.short_description = 'Есть изображение'
```

---

### GALLERY

#### `backend/gallery/models.py`

```python
from django.db import models
from django.conf import settings
from django.utils import timezone
import os


class Album(models.Model):
    """Модель альбома"""
    
    title = models.CharField(
        max_length=200,
        verbose_name='Название альбома'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    date = models.DateField(
        verbose_name='Дата события',
        help_text='Укажите дату, к которой относится альбом'
    )
    cover_image = models.ImageField(
        upload_to='albums/covers/',
        blank=True,
        null=True,
        verbose_name='Обложка альбома'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликован'
    )
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-date']
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.cover_image:
            file_path = self.cover_image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f'🗑️ Обложка альбома удалена: {file_path}')
        super().delete(*args, **kwargs)


class Photo(models.Model):
    """Модель фотографии"""
    
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Альбом'
    )
    image = models.ImageField(
        upload_to='albums/photos/',
        verbose_name='Фотография'
    )
    caption = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Подпись'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок'
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата загрузки'
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name='Просмотры'
    )
    likes_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество лайков'
    )
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['order', 'uploaded_at']
    
    def __str__(self):
        return f"{self.album.title} - {self.id}"
    
    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    
    def delete(self, *args, **kwargs):
        if self.image:
            file_path = self.image.path
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f'🗑️ Фотография удалена: {file_path}')
        super().delete(*args, **kwargs)


class PhotoLike(models.Model):
    """Модель лайка для фотографии"""
    
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Фотография'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photo_likes',
        verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    class Meta:
        unique_together = ['photo', 'user']
        verbose_name = 'Лайк фотографии'
        verbose_name_plural = 'Лайки фотографий'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} → {self.photo.id}"


class PhotoComment(models.Model):
    """Модель комментария к фотографии"""
    
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Фотография'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photo_comments',
        verbose_name='Пользователь'
    )
    content = models.TextField(
        verbose_name='Текст комментария'
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name='Родительский комментарий'
    )
    
    class Meta:
        verbose_name = 'Комментарий к фото'
        verbose_name_plural = 'Комментарии к фото'
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"
```

---

#### `backend/gallery/serializers.py`

```python
from rest_framework import serializers
from .models import Album, Photo, PhotoLike, PhotoComment


class PhotoCommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев к фото"""
    user_name = serializers.ReadOnlyField(source='user.username')
    user_avatar = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    
    class Meta:
        model = PhotoComment
        fields = [
            'id',
            'photo',
            'user',
            'user_name',
            'user_avatar',
            'content',
            'created_at',
            'updated_at',
            'can_edit',
            'can_delete'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    
    def get_user_avatar(self, obj):
        if obj.user.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.user.avatar.url)
            return obj.user.avatar.url
        return None
    
    def get_can_edit(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.user == request.user
    
    def get_can_delete(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        
        user = request.user
        if obj.user == user:
            return True
        if user.role == 'editor':
            return True
        return False


class PhotoLikeSerializer(serializers.ModelSerializer):
    """Сериализатор для лайков фото"""
    user_name = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = PhotoLike
        fields = ['id', 'photo', 'user', 'user_name', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class PhotoSerializer(serializers.ModelSerializer):
    """Сериализатор для фотографий"""
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Photo
        fields = [
            'id',
            'album',
            'image',
            'image_url',
            'thumbnail_url',
            'caption',
            'order',
            'uploaded_at',
            'views',
            'likes_count',
            'user_has_liked',
            'comments_count',
            'comments'
        ]
        read_only_fields = ['id', 'uploaded_at', 'views', 'likes_count']
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    
    def get_thumbnail_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    
    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.likes.filter(user=request.user).exists()
    
    def get_comments(self, obj):
        comments = obj.comments.all()
        context = {'request': self.context.get('request')}
        return PhotoCommentSerializer(comments, many=True, context=context).data


class AlbumListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка альбомов"""
    cover_image_url = serializers.SerializerMethodField()
    photos_count = serializers.IntegerField(source='photos.count', read_only=True)
    
    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'description',
            'date',
            'cover_image',
            'cover_image_url',
            'photos_count',
            'created_at',
            'updated_at',
            'is_published'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        
        first_photo = obj.photos.first()
        if first_photo and first_photo.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.image.url)
            return first_photo.image.url
        return None


class AlbumDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детального просмотра альбома"""
    photos = PhotoSerializer(many=True, read_only=True)
    cover_image_url = serializers.SerializerMethodField()
    photos_count = serializers.IntegerField(source='photos.count', read_only=True)
    
    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'description',
            'date',
            'cover_image',
            'cover_image_url',
            'photos',
            'photos_count',
            'created_at',
            'updated_at',
            'is_published'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_cover_image_url(self, obj):
        if obj.cover_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        
        first_photo = obj.photos.first()
        if first_photo and first_photo.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_photo.image.url)
            return first_photo.image.url
        return None


class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и обновления альбома"""
    
    class Meta:
        model = Album
        fields = [
            'id',
            'title',
            'description',
            'date',
            'cover_image',
            'is_published'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
```

---

#### `backend/gallery/views.py`

```python
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
from .models import Album, Photo, PhotoLike
from .serializers import (
    AlbumListSerializer, AlbumDetailSerializer, 
    AlbumCreateUpdateSerializer, PhotoSerializer
)
from .permissions import IsEditorOrReadOnly


class AlbumViewSet(viewsets.ModelViewSet):
    """ViewSet для альбомов"""
    queryset = Album.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsEditorOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AlbumListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return AlbumCreateUpdateSerializer
        return AlbumDetailSerializer
    
    def get_queryset(self):
        queryset = Album.objects.all()
        
        if self.action == 'list':
            return queryset.filter(is_published=True)
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save()
        print(f'📸 Создан альбом: {serializer.instance.title}')
    
    def perform_update(self, serializer):
        instance = serializer.instance
        old_cover = instance.cover_image
        
        serializer.save()
        
        if old_cover and old_cover != instance.cover_image:
            file_path = old_cover.path
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f'🗑️ Старая обложка альбома удалена: {file_path}')
                except Exception as e:
                    print(f'❌ Ошибка удаления: {e}')
        
        print(f'📸 Обновлён альбом: {serializer.instance.title}')
    
    def perform_destroy(self, instance):
        print(f'🗑️ Удаляем альбом: {instance.title}')
        instance.delete()
    
    @action(detail=True, methods=['post'], url_path='upload-photos')
    def upload_photos(self, request, pk=None):
        """Загрузка нескольких фотографий в альбом"""
        album = self.get_object()
        
        if request.user.role != 'editor':
            return Response(
                {'detail': 'Только редакторы могут загружать фотографии'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        if 'photos' not in request.FILES:
            return Response(
                {'detail': 'Файлы не переданы'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        files = request.FILES.getlist('photos')
        uploaded_photos = []
        
        print(f'📸 Получено {len(files)} файлов для загрузки')
        
        for file in files:
            print(f'  - {file.name} ({file.size} байт, {file.content_type})')
            
            if file.size > 10 * 1024 * 1024:
                print(f'  ⚠️ Файл {file.name} слишком большой, пропускаем')
                continue
            
            allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
            if file.content_type not in allowed_types:
                print(f'  ⚠️ Файл {file.name} имеет неподдерживаемый тип {file.content_type}, пропускаем')
                continue
            
            photo = Photo.objects.create(
                album=album,
                image=file,
                caption=request.data.get('caption', '')
            )
            uploaded_photos.append(photo)
            print(f'  ✅ Загружено фото: {file.name}')
        
        print(f'📸 Успешно загружено {len(uploaded_photos)} фотографий')
        
        serializer = PhotoSerializer(uploaded_photos, many=True, context={'request': request})
        
        return Response({
            'detail': f'Загружено {len(uploaded_photos)} фотографий',
            'photos': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    @action(
        detail=True, 
        methods=['post'], 
        url_path='photos/(?P<photo_id>[^/.]+)/view',
        permission_classes=[AllowAny]
    )
    def view_photo(self, request, pk=None, photo_id=None):
        """Увеличить количество просмотров фотографии"""
        album = self.get_object()
        photo = get_object_or_404(Photo, id=photo_id, album=album)
        
        photo.views += 1
        photo.save(update_fields=['views'])
        
        return Response({
            'detail': 'Просмотр засчитан',
            'views': photo.views
        }, status=status.HTTP_200_OK)
    
    @action(
        detail=True, 
        methods=['post'], 
        url_path='photos/(?P<photo_id>[^/.]+)/like',
        permission_classes=[IsAuthenticated]
    )
    def like_photo(self, request, pk=None, photo_id=None):
        """Поставить/убрать лайк на фотографии"""
        album = self.get_object()
        photo = get_object_or_404(Photo, id=photo_id, album=album)
        
        existing_like = PhotoLike.objects.filter(photo=photo, user=request.user).first()
        
        if existing_like:
            existing_like.delete()
            photo.likes_count -= 1
            photo.save(update_fields=['likes_count'])
            return Response({
                'detail': 'Лайк убран',
                'action': 'unliked',
                'likes_count': photo.likes_count,
                'photo_id': photo.id
            }, status=status.HTTP_200_OK)
        else:
            PhotoLike.objects.create(photo=photo, user=request.user)
            photo.likes_count += 1
            photo.save(update_fields=['likes_count'])
            return Response({
                'detail': 'Лайк поставлен',
                'action': 'liked',
                'likes_count': photo.likes_count,
                'photo_id': photo.id
            }, status=status.HTTP_201_CREATED)

    @action(
        detail=True, 
        methods=['delete'], 
        url_path='photos/(?P<photo_id>[^/.]+)',
        permission_classes=[IsAuthenticated]
    )
    def delete_photo(self, request, pk=None, photo_id=None):
        """Удаление фотографии из альбома"""
        album = self.get_object()
        
        if request.user.role != 'editor':
            return Response(
                {'detail': 'Только редакторы могут удалять фотографии'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        photo = get_object_or_404(Photo, id=photo_id, album=album)
        photo.delete()
        
        return Response(
            {'detail': 'Фотография удалена'},
            status=status.HTTP_200_OK
        )


class PhotoReorderView(generics.UpdateAPIView):
    """Обновление порядка фотографий"""
    permission_classes = [IsAuthenticated]
    
    def post(self, request, album_id):
        if request.user.role != 'editor':
            return Response(
                {'detail': 'Только редакторы могут изменять порядок'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        album = get_object_or_404(Album, id=album_id)
        photo_ids = request.data.get('photo_ids', [])
        
        for index, photo_id in enumerate(photo_ids):
            Photo.objects.filter(id=photo_id, album=album).update(order=index)
        
        return Response(
            {'detail': 'Порядок фотографий обновлён'},
            status=status.HTTP_200_OK
        )
```

---

#### `backend/gallery/comment_views.py`

```python
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import PhotoComment, Photo
from .serializers import PhotoCommentSerializer


class PhotoCommentViewSet(viewsets.ModelViewSet):
    """ViewSet для комментариев к фотографиям"""
    queryset = PhotoComment.objects.all().select_related('user', 'photo')
    serializer_class = PhotoCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
    
    def get_queryset(self):
        queryset = PhotoComment.objects.all().select_related('user', 'photo')
        photo_id = self.request.query_params.get('photo_id')
        if photo_id:
            queryset = queryset.filter(photo_id=photo_id)
        return queryset
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def perform_create(self, serializer):
        photo_id = self.request.data.get('photo')
        if not photo_id:
            from rest_framework.exceptions import ValidationError
            raise ValidationError({'photo': 'Это поле обязательно'})
        photo = get_object_or_404(Photo, id=photo_id)
        serializer.save(user=self.request.user, photo=photo)
        print(f'💬 Создан комментарий к фото: {serializer.instance.content[:30]}...')
    
    @action(detail=False, methods=['get'], url_path='my_comments')
    def my_comments(self, request):
        """Получить комментарии текущего пользователя"""
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Не авторизован'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        comments = PhotoComment.objects.filter(user=request.user).order_by('-created_at')
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        """Получить конкретный комментарий"""
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            print(f'🔍 Получен комментарий к фото {instance.id}')
            return Response(serializer.data)
        except Exception as e:
            print(f'❌ Ошибка получения комментария: {e}')
            return Response(
                {'detail': 'Комментарий не найден'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def update(self, request, *args, **kwargs):
        """Обновить комментарий (PUT)"""
        try:
            instance = self.get_object()
            
            print(f'🔍 Обновление комментария к фото {instance.id} пользователем {request.user.username}')
            print(f'🔍 Автор комментария: {instance.user.username}')
            
            if instance.user != request.user:
                return Response(
                    {'detail': 'Вы можете редактировать только свои комментарии'},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            
            print(f'✅ Комментарий к фото {instance.id} обновлён')
            return Response(serializer.data)
            
        except Exception as e:
            print(f'❌ Ошибка обновления комментария: {e}')
            return Response(
                {'detail': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request, *args, **kwargs):
        """Обновить комментарий (PATCH)"""
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        """Удалить комментарий"""
        try:
            instance = self.get_object()
            
            print(f'🔍 Удаление комментария к фото {instance.id} пользователем {request.user.username}')
            
            if instance.user != request.user and request.user.role != 'editor':
                return Response(
                    {'detail': 'Вы можете удалять только свои комментарии'},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            self.perform_destroy(instance)
            print(f'✅ Комментарий к фото {instance.id} удалён')
            return Response(
                {'detail': 'Комментарий удалён'},
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(f'❌ Ошибка удаления комментария: {e}')
            return Response(
                {'detail': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
```

---

#### `backend/gallery/permissions.py`

```python
from rest_framework import permissions


class IsEditorOrReadOnly(permissions.BasePermission):
    """Разрешение: только чтение для всех, запись только для редакторов"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.role == 'editor'
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.role == 'editor'
```

---

#### `backend/gallery/urls.py`

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, PhotoReorderView
from .comment_views import PhotoCommentViewSet

router = DefaultRouter()
router.register(r'photo-comments', PhotoCommentViewSet, basename='photo-comment')
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = [
    path('', include(router.urls)),
    path('albums/<int:album_id>/reorder/', PhotoReorderView.as_view(), name='photo-reorder'),
]
```

---

#### `backend/gallery/admin.py`

```python
from django.contrib import admin
from .models import Album, Photo, PhotoLike, PhotoComment


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ['image', 'caption', 'order']
    ordering = ['order']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'photos_count', 'is_published', 'created_at']
    list_filter = ['is_published', 'date']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PhotoInline]
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description', 'date', 'is_published')
        }),
        ('Изображение', {
            'fields': ('cover_image',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def photos_count(self, obj):
        return obj.photos.count()
    photos_count.short_description = 'Количество фото'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'caption', 'order', 'views', 'likes_count', 'uploaded_at']
    list_filter = ['album', 'uploaded_at']
    search_fields = ['caption']


@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'photo__id']


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'user', 'content', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'content']
```

---

### ФРОНТЕНД

#### `frontend/nuxt.config.ts`

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

#### `frontend/tailwind.config.js`

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

#### `frontend/assets/css/main.css`

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

#### `frontend/store/auth.js`

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
                console.log('✅ Авторизация установлена')
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
                    console.log('✅ Авторизация восстановлена из localStorage')
                    return true
                } else {
                    console.log('⚠️ Токены не найдены в localStorage')
                    return false
                }
            }
            return false
        },

        logout() {
            this.user = null
            this.accessToken = null
            this.refreshToken = null

            if (process.client) {
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
                localStorage.removeItem('user')
                console.log('👋 Выход выполнен')
            }
        }
    }
})
```

---

#### `frontend/store/theme.js`

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

#### `frontend/middleware/auth.js`

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

#### `frontend/middleware/editor.js`

```javascript
import { useAuthStore } from '~/store/auth'

export default defineNuxtRouteMiddleware((to, from) => {
  const authStore = useAuthStore()
  
  authStore.restoreAuth()
  
  if (!authStore.isAuthenticated) {
    return navigateTo('/auth/login')
  }
  
  if (!authStore.isEditor) {
    return navigateTo('/')
  }
})
```

---

### КОМПОНЕНТЫ

#### `frontend/components/layout/AppHeader.vue`

```vue
<template>
  <header class="bg-white dark:bg-gray-800 shadow transition-colors duration-200 sticky top-0 z-50">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
      <!-- Левая часть: Логотип + Бургер -->
      <div class="flex items-center gap-2">
        <AppLogo />
        <BurgerMenu />
      </div>
      
      <!-- Правая часть: Создать + Переключатель темы + Кнопки пользователя -->
      <div class="flex items-center gap-2 md:gap-4">
        <CreateMenu />
        <ThemeToggle />
        <AuthButtons />
      </div>
    </div>
  </header>
</template>

<script setup>
import AppLogo from './AppLogo.vue'
import BurgerMenu from '~/components/common/BurgerMenu.vue'
import ThemeToggle from '~/components/common/ThemeToggle.vue'
import AuthButtons from '~/components/common/AuthButtons.vue'
import CreateMenu from '~/components/common/CreateMenu.vue'
</script>
```

---

#### `frontend/components/layout/AppFooter.vue`

```vue
<template>
  <footer class="app-footer text-gray-300 mt-10">
    <div class="container mx-auto px-4">
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
            <li class="flex items-center gap-2 text-gray-300">
              <span>📍</span>
              <span>{{ contacts.address }}</span>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <span>📞</span>
              <a :href="`tel:${contacts.phone}`" class="text-gray-300 hover:text-blue-400 transition">
                {{ contacts.phone }}
              </a>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <span>✉️</span>
              <a :href="`mailto:${contacts.email}`" class="text-gray-300 hover:text-blue-400 transition">
                {{ contacts.email }}
              </a>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <span>🕐</span>
              <span>{{ contacts.work_hours }}</span>
            </li>
          </ul>
        </div>
        
        <div>
          <h3 class="text-white text-lg font-semibold mb-3">📂 Разделы</h3>
          <ul class="space-y-2 text-sm">
            <li>
              <NuxtLink to="/events" class="text-gray-300 hover:text-blue-400 transition">
                🎭 Афиша
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/posts" class="text-gray-300 hover:text-blue-400 transition">
                📝 Публикации
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/gallery" class="text-gray-300 hover:text-blue-400 transition">
                📸 Галерея
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/authors" class="text-gray-300 hover:text-blue-400 transition">
                ✍️ Авторы
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/contacts" class="text-gray-300 hover:text-blue-400 transition">
                📞 Контакты
              </NuxtLink>
            </li>
            <li v-if="authStore.isEditor">
              <NuxtLink to="/settings" class="text-gray-300 hover:text-yellow-400 transition">
                ⚙️ Настройки
              </NuxtLink>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="border-t border-gray-800 mt-6 pt-6 text-center text-sm text-gray-500">
        <p>© {{ new Date().getFullYear() }} Центр Культуры. Все права защищены.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const contacts = ref(null)
const contactsLoading = ref(true)

const loadContacts = async () => {
  contactsLoading.value = true
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
}

onMounted(async () => {
  await loadContacts()
  window.addEventListener('contacts-updated', loadContacts)
})

onUnmounted(() => {
  window.removeEventListener('contacts-updated', loadContacts)
})
</script>

<style scoped>
.app-footer {
  background-color: #111827 !important;
  padding-top: 40px !important;
  padding-bottom: 40px !important;
}

.app-footer,
.app-footer * {
  color: #d1d5db !important;
}

.app-footer h3 {
  color: #ffffff !important;
}

.app-footer a {
  color: #d1d5db !important;
}

.app-footer a:hover {
  color: #60a5fa !important;
}

:where(.dark) .app-footer {
  background-color: #111827 !important;
}

:where(.dark) .app-footer,
:where(.dark) .app-footer * {
  color: #d1d5db !important;
}

:where(.dark) .app-footer h3 {
  color: #ffffff !important;
}

:where(.dark) .app-footer a {
  color: #d1d5db !important;
}

:where(.dark) .app-footer a:hover {
  color: #60a5fa !important;
}
</style>
```

---

#### `frontend/components/layout/AppLogo.vue`

```vue
<template>
  <NuxtLink to="/" class="flex items-center gap-2 text-xl font-bold text-gray-800 dark:text-white">
    <span class="text-2xl">🏛️</span>
    <span class="hidden sm:inline">Центр Культуры</span>
    <span class="sm:hidden">ЦК</span>
  </NuxtLink>
</template>
```

---

#### `frontend/components/common/BurgerMenu.vue`

```vue
<template>
  <div class="relative" ref="menuRef">
    <button 
      @click="toggleMenu"
      class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition text-gray-600 dark:text-gray-300 focus:outline-none"
      aria-label="Меню"
    >
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
      </svg>
    </button>
    
    <div 
      v-if="isMenuOpen"
      class="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50"
      @click.stop
    >
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Навигация
      </div>
      <NuxtLink 
        to="/" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">🏠</span>
        Главная
      </NuxtLink>
      <NuxtLink 
        to="/events" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">🎭</span>
        Афиша
      </NuxtLink>
      <NuxtLink 
        to="/posts" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">📝</span>
        Публикации
      </NuxtLink>
      <NuxtLink 
        to="/gallery" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">📸</span>
        Галерея
      </NuxtLink>
      <NuxtLink 
        to="/authors" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">✍️</span>
        Авторы
      </NuxtLink>
      <NuxtLink 
        to="/contacts" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">📞</span>
        Контакты
      </NuxtLink>
      
      <div v-if="authStore.isEditor" class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div v-if="authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Управление
      </div>
      <NuxtLink 
        v-if="authStore.isEditor"
        to="/settings" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-yellow-600 dark:text-yellow-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">⚙️</span>
        Настройки сайта
      </NuxtLink>
      
      <div class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Аккаунт
      </div>
      <template v-if="authStore.isAuthenticated">
        <NuxtLink 
          to="/profile" 
          class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
          @click="closeMenu"
        >
          <span class="text-lg">👤</span>
          Мой профиль
        </NuxtLink>
        <button 
          @click="handleLogout"
          class="flex items-center gap-3 px-4 py-2.5 text-sm text-red-500 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition w-full text-left"
        >
          <span class="text-lg">🚪</span>
          Выйти
        </button>
      </template>
      <template v-else>
        <NuxtLink 
          to="/auth/login" 
          class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
          @click="closeMenu"
        >
          <span class="text-lg">🔑</span>
          Войти
        </NuxtLink>
        <NuxtLink 
          to="/auth/register" 
          class="flex items-center gap-3 px-4 py-2.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
          @click="closeMenu"
        >
          <span class="text-lg">📝</span>
          Регистрация
        </NuxtLink>
      </template>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()

const isMenuOpen = ref(false)
const menuRef = ref(null)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleLogout = () => {
  authStore.logout()
  closeMenu()
  navigateTo('/')
}

const handleClickOutside = (event) => {
  if (menuRef.value && !menuRef.value.contains(event.target)) {
    isMenuOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>
```

---

#### `frontend/components/common/ThemeToggle.vue`

```vue
<template>
  <button 
    @click="toggleTheme"
    class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition text-gray-600 dark:text-gray-300"
    :title="themeStore.darkMode ? 'Светлая тема' : 'Тёмная тема'"
    aria-label="Переключить тему"
  >
    <span class="text-xl">
      {{ themeStore.darkMode ? '☀️' : '🌙' }}
    </span>
  </button>
</template>

<script setup>
import { useThemeStore } from '~/store/theme'

const themeStore = useThemeStore()

const toggleTheme = () => {
  themeStore.toggleTheme()
}
</script>
```

---

#### `frontend/components/common/AuthButtons.vue`

```vue
<template>
  <div class="flex items-center gap-3">
    <template v-if="authStore.isAuthenticated">
      <NuxtLink 
        to="/profile" 
        class="hidden md:flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition font-medium"
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
        <span class="hidden lg:inline">{{ authStore.user?.username }}</span>
      </NuxtLink>
      
      <UiButton 
        variant="danger"
        size="sm"
        @click="handleLogout"
        class="hidden md:inline-flex"
      >
        Выйти
      </UiButton>
    </template>
    
    <template v-else>
      <NuxtLink to="/auth/login">
        <UiButton variant="outline" size="sm">
          Войти
        </UiButton>
      </NuxtLink>
      
      <NuxtLink to="/auth/register">
        <UiButton variant="primary" size="sm">
          Регистрация
        </UiButton>
      </NuxtLink>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'

const authStore = useAuthStore()

const getInitials = (user) => {
  if (!user) return '?'
  const name = user.full_name || user.username
  const parts = name.split(' ')
  if (parts.length >= 2) {
    return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  }
  return name.substring(0, 2).toUpperCase()
}

const handleLogout = () => {
  authStore.logout()
  navigateTo('/')
}
</script>
```

---

#### `frontend/components/common/CreateMenu.vue`

```vue
<template>
  <div v-if="canCreate" class="relative" ref="menuRef">
    <!-- Кнопка "Создать" -->
    <button 
      @click="toggleMenu"
      class="flex items-center gap-1.5 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition text-sm font-medium"
      aria-label="Создать"
    >
      <span class="text-lg">➕</span>
      <span class="hidden sm:inline">Создать</span>
      <svg 
        class="w-4 h-4 transition-transform ml-1" 
        :class="isMenuOpen ? 'rotate-180' : ''" 
        fill="none" 
        stroke="currentColor" 
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
      </svg>
    </button>
    
    <!-- Выпадающее меню -->
    <div 
      v-if="isMenuOpen"
      class="absolute right-0 top-full mt-2 w-56 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50"
      @click.stop
    >
      <!-- Посты (доступно автору и редактору) -->
      <div v-if="authStore.isAuthor || authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Контент
      </div>
      <NuxtLink 
        v-if="authStore.isAuthor || authStore.isEditor"
        to="/posts/create" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">📝</span>
        Новый пост
      </NuxtLink>
      
      <!-- События (только редактор) -->
      <NuxtLink 
        v-if="authStore.isEditor"
        to="/events/create" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">🎭</span>
        Новое событие
      </NuxtLink>
      
      <!-- Альбомы (только редактор) -->
      <div v-if="authStore.isEditor" class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div v-if="authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
        Галерея
      </div>
      <NuxtLink 
        v-if="authStore.isEditor"
        to="/gallery/create" 
        class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition"
        @click="closeMenu"
      >
        <span class="text-lg">📸</span>
        Новый альбом
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()

const isMenuOpen = ref(false)
const menuRef = ref(null)

const canCreate = computed(() => {
  return authStore.isAuthor || authStore.isEditor
})

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleClickOutside = (event) => {
  if (menuRef.value && !menuRef.value.contains(event.target)) {
    isMenuOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>
```

---

#### `frontend/components/features/banner/HeroBanner.vue`

```vue
<template>
  <div class="relative w-full overflow-hidden transition-colors duration-200">
    <div 
      v-if="banner.has_background" 
      class="absolute inset-0 w-full h-full bg-cover bg-center"
      :style="{ backgroundImage: `url(${banner.background_image_url_display})` }"
    >
      <div class="absolute inset-0 bg-black bg-opacity-40"></div>
    </div>
    
    <div 
      v-else
      class="absolute inset-0 w-full h-full bg-gradient-to-r from-blue-600 to-purple-600 dark:from-blue-800 dark:to-purple-800"
    ></div>
    
    <div class="relative container mx-auto px-4 py-20 md:py-28 text-center text-white">
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-4">
        {{ banner.title }}
      </h1>
      <p class="text-lg md:text-xl text-blue-100 dark:text-blue-200 max-w-2xl mx-auto">
        {{ banner.subtitle }}
      </p>
      
      <NuxtLink 
        v-if="banner.button_enabled !== false && banner.button_text && banner.button_link"
        :to="banner.button_link"
        class="inline-block mt-6 bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition shadow-lg"
      >
        {{ banner.button_text }} →
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
defineProps({
  banner: {
    type: Object,
    required: true,
    default: () => ({
      title: '🏛️ Добро пожаловать в Центр Культуры',
      subtitle: 'Место, где искусство, традиции и творчество объединяются',
      has_background: false,
      background_image_url_display: '',
      button_text: '',
      button_link: '',
      button_enabled: true,
      is_active: true
    })
  }
})
</script>
```

---

### UI-КОМПОНЕНТЫ

#### `frontend/components/ui/UiButton.vue`

```vue
<template>
  <button 
    :type="type"
    :disabled="disabled"
    class="px-6 py-2 rounded-lg transition font-medium inline-flex items-center justify-center gap-2"
    :class="[variantClasses, sizeClasses, widthClass]"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup>
const props = defineProps({
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'danger', 'warning', 'outline', 'success'].includes(value)
  },
  type: {
    type: String,
    default: 'button'
  },
  disabled: {
    type: Boolean,
    default: false
  },
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  fullWidth: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

const variantClasses = computed(() => {
  const variants = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600 disabled:bg-blue-300 dark:disabled:bg-blue-800',
    secondary: 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600 disabled:bg-gray-100 dark:disabled:bg-gray-800 disabled:text-gray-400',
    danger: 'bg-red-500 text-white hover:bg-red-600 disabled:bg-red-300 dark:disabled:bg-red-800',
    warning: 'bg-yellow-500 text-white hover:bg-yellow-600 disabled:bg-yellow-300 dark:disabled:bg-yellow-800',
    success: 'bg-green-500 text-white hover:bg-green-600 disabled:bg-green-300 dark:disabled:bg-green-800',
    outline: 'bg-transparent border-2 border-blue-500 text-blue-500 hover:bg-blue-50 dark:hover:bg-blue-900/20 disabled:opacity-50'
  }
  return variants[props.variant] || variants.primary
})

const sizeClasses = computed(() => {
  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-6 py-2 text-base',
    lg: 'px-8 py-3 text-lg'
  }
  return sizes[props.size] || sizes.md
})

const widthClass = computed(() => {
  return props.fullWidth ? 'w-full' : ''
})
</script>
```

---

#### `frontend/components/ui/UiInput.vue`

```vue
<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <input 
      :type="type"
      :value="modelValue"
      :placeholder="placeholder"
      :required="required"
      :disabled="disabled"
      class="w-full border rounded-lg p-2 focus:outline-none focus:ring-2 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
      :class="inputClasses"
      @input="$emit('update:modelValue', $event.target.value)"
      @blur="$emit('blur')"
      @focus="$emit('focus')"
    />
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: [String, Number],
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'text'
  },
  placeholder: {
    type: String,
    default: ''
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: ''
  },
  hint: {
    type: String,
    default: ''
  },
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'success', 'error'].includes(value)
  }
})

defineEmits(['update:modelValue', 'blur', 'focus'])

const inputClasses = computed(() => {
  const variants = {
    default: 'border-gray-300 dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500',
    success: 'border-green-500 focus:ring-green-500 focus:border-green-500',
    error: 'border-red-500 focus:ring-red-500 focus:border-red-500'
  }
  return variants[props.variant] || variants.default
})
</script>
```

---

#### `frontend/components/ui/UiTextarea.vue`

```vue
<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <textarea 
      :value="modelValue"
      :placeholder="placeholder"
      :rows="rows"
      :required="required"
      :disabled="disabled"
      class="w-full border rounded-lg p-2 focus:outline-none focus:ring-2 transition resize-y min-h-[60px] bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
      :class="inputClasses"
      @input="$emit('update:modelValue', $event.target.value)"
      @blur="$emit('blur')"
      @focus="$emit('focus')"
    ></textarea>
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  label: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: ''
  },
  rows: {
    type: Number,
    default: 3
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: ''
  },
  hint: {
    type: String,
    default: ''
  },
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'success', 'error'].includes(value)
  }
})

defineEmits(['update:modelValue', 'blur', 'focus'])

const inputClasses = computed(() => {
  const variants = {
    default: 'border-gray-300 dark:border-gray-600 focus:ring-blue-500 focus:border-blue-500',
    success: 'border-green-500 focus:ring-green-500 focus:border-green-500',
    error: 'border-red-500 focus:ring-red-500 focus:border-red-500'
  }
  return variants[props.variant] || variants.default
})
</script>
```

---

#### `frontend/components/ui/UiCheckbox.vue`

```vue
<template>
  <label class="flex items-center gap-2 cursor-pointer group">
    <div class="relative">
      <input 
        type="checkbox"
        :checked="modelValue"
        :disabled="disabled"
        class="w-4 h-4 text-blue-500 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed"
        @change="$emit('update:modelValue', $event.target.checked)"
      />
    </div>
    <span class="text-gray-700 dark:text-gray-300 select-none" :class="disabled ? 'opacity-50' : ''">
      <slot />
    </span>
  </label>
</template>

<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

defineEmits(['update:modelValue'])
</script>
```

---

#### `frontend/components/ui/UiCard.vue`

```vue
<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow" :class="paddingClass">
    <slot />
  </div>
</template>

<script setup>
const props = defineProps({
  padding: {
    type: String,
    default: 'md',
    validator: (value) => ['none', 'sm', 'md', 'lg'].includes(value)
  }
})

const paddingClass = computed(() => {
  const paddings = {
    none: 'p-0',
    sm: 'p-3',
    md: 'p-6',
    lg: 'p-8'
  }
  return paddings[props.padding] || paddings.md
})
</script>
```

---

#### `frontend/components/ui/UiFileInput.vue`

```vue
<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    
    <div 
      class="relative border-2 border-dashed rounded-lg p-6 transition bg-white dark:bg-gray-700"
      :class="[
        isDragging ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20' : 'border-gray-300 dark:border-gray-600',
        disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer hover:border-blue-400'
      ]"
      @dragover.prevent="isDragging = true"
      @dragleave.prevent="isDragging = false"
      @drop.prevent="handleDrop"
      @click="triggerFileInput"
    >
      <div class="text-center">
        <div class="text-4xl mb-2">
          {{ multiple ? '📁' : '📄' }}
        </div>
        <p class="text-gray-600 dark:text-gray-300">
          {{ multiple ? 'Перетащите файлы сюда или кликните для выбора' : 'Перетащите файл сюда или кликните для выбора' }}
        </p>
        <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">
          {{ accept ? `Поддерживаемые форматы: ${accept}` : 'Любые форматы' }}
          {{ maxSize ? ` • Максимум: ${formatFileSize(maxSize)}` : '' }}
        </p>
        <p v-if="multiple" class="text-sm text-gray-400 dark:text-gray-500">
          Можно выбрать несколько файлов
        </p>
      </div>
      
      <input
        ref="fileInputRef"
        type="file"
        :accept="accept"
        :multiple="multiple"
        :disabled="disabled"
        class="absolute inset-0 opacity-0 cursor-pointer"
        @change="handleFileSelect"
      />
    </div>
    
    <!-- Предпросмотр файлов -->
    <div v-if="filePreviews.length > 0" class="mt-3">
      <div class="flex flex-wrap gap-2">
        <div 
          v-for="(file, index) in filePreviews" 
          :key="index"
          class="relative group"
        >
          <div v-if="file.preview" class="relative">
            <img 
              :src="file.preview" 
              :alt="file.name"
              class="w-20 h-20 object-cover rounded-lg border border-gray-200 dark:border-gray-600"
            />
            <button
              v-if="!disabled && removable"
              type="button"
              class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100"
              @click="removeFile(index)"
            >
              ✕
            </button>
          </div>
          
          <div v-else class="relative">
            <div class="w-20 h-20 bg-gray-100 dark:bg-gray-600 rounded-lg border border-gray-200 dark:border-gray-600 flex items-center justify-center">
              <span class="text-3xl">📄</span>
            </div>
            <button
              v-if="!disabled && removable"
              type="button"
              class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100"
              @click="removeFile(index)"
            >
              ✕
            </button>
          </div>
          
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1 truncate max-w-[80px] text-center">
            {{ file.name }}
          </p>
        </div>
      </div>
      
      <p v-if="multiple && filePreviews.length > 0" class="text-xs text-gray-400 dark:text-gray-500 mt-2">
        Выбрано файлов: {{ filePreviews.length }}
      </p>
    </div>
    
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: {
    type: [File, Array, null],
    default: null
  },
  label: {
    type: String,
    default: ''
  },
  hint: {
    type: String,
    default: ''
  },
  error: {
    type: String,
    default: ''
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  multiple: {
    type: Boolean,
    default: false
  },
  accept: {
    type: String,
    default: ''
  },
  maxSize: {
    type: Number,
    default: 5 * 1024 * 1024
  },
  removable: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits(['update:modelValue', 'change', 'remove'])

const fileInputRef = ref(null)
const isDragging = ref(false)
const filePreviews = ref([])

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Б'
  const k = 1024
  const sizes = ['Б', 'КБ', 'МБ', 'ГБ']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i]
}

const validateFileSize = (file) => {
  if (props.maxSize && file.size > props.maxSize) {
    return {
      valid: false,
      message: `Файл "${file.name}" слишком большой. Максимум: ${formatFileSize(props.maxSize)}`
    }
  }
  return { valid: true, message: '' }
}

const isImageFile = (file) => {
  if (!file) return false
  if (file.type && file.type.startsWith('image/')) return true
  if (file.name) {
    const ext = file.name.split('.').pop().toLowerCase()
    return ['jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'bmp', 'ico'].includes(ext)
  }
  return false
}

const createPreview = (file, callback) => {
  if (isImageFile(file)) {
    try {
      const reader = new FileReader()
      reader.onload = (e) => {
        const fileData = {
          file: file,
          preview: e.target.result,
          name: file.name,
          type: file.type,
          size: file.size
        }
        callback(fileData)
      }
      reader.readAsDataURL(file)
    } catch (e) {
      console.error('Ошибка создания превью:', e)
      callback(file)
    }
  } else {
    callback(file)
  }
}

const handleFileSelect = (event) => {
  const files = event.target.files
  if (!files || files.length === 0) return
  
  const filesArray = Array.from(files)
  processFiles(filesArray)
  event.target.value = ''
}

const handleDrop = (event) => {
  isDragging.value = false
  const files = event.dataTransfer.files
  if (!files || files.length === 0) return
  
  const filesArray = Array.from(files)
  processFiles(filesArray)
}

const processFiles = (filesArray) => {
  const errors = []
  
  if (!props.multiple) {
    filePreviews.value = []
  }
  
  let processedCount = 0
  
  for (const file of filesArray) {
    const sizeCheck = validateFileSize(file)
    if (!sizeCheck.valid) {
      errors.push(sizeCheck.message)
      continue
    }
    
    createPreview(file, (fileData) => {
      if (props.multiple) {
        filePreviews.value = [...filePreviews.value, fileData]
      } else {
        filePreviews.value = [fileData]
      }
      processedCount++
      
      if (processedCount === filesArray.length) {
        updateModel()
        emit('change', filePreviews.value)
      }
    })
  }
  
  if (errors.length > 0) {
    alert(errors.join('\n'))
  }
  
  if (filesArray.length === 0) {
    updateModel()
    emit('change', filePreviews.value)
  }
}

const updateModel = () => {
  if (props.multiple) {
    const files = filePreviews.value.map(f => f.file || f)
    emit('update:modelValue', files)
  } else {
    const first = filePreviews.value[0]
    if (first) {
      const fileData = first.file || first
      emit('update:modelValue', fileData)
    } else {
      emit('update:modelValue', null)
    }
  }
}

const triggerFileInput = () => {
  if (!props.disabled && fileInputRef.value) {
    fileInputRef.value.click()
  }
}

const removeFile = (index) => {
  filePreviews.value.splice(index, 1)
  updateModel()
  emit('remove', index)
  emit('change', filePreviews.value)
}

const reset = () => {
  filePreviews.value = []
  updateModel()
}

defineExpose({
  filePreviews,
  reset
})
</script>
```

---

### APP.VUE

#### `frontend/app.vue`

```vue
<template>
  <div class="flex flex-col min-h-screen">
    <AppHeader />
    <main class="flex-1">
      <NuxtPage />
    </main>
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from '~/components/layout/AppHeader.vue'
import AppFooter from '~/components/layout/AppFooter.vue'
</script>
```

---

### СТРАНИЦЫ

#### `frontend/pages/index.vue`

```vue
<template>
  <div>
    <!-- HERO БАННЕР -->
    <div v-if="bannerLoading" class="w-full h-64 bg-gray-200 dark:bg-gray-700 animate-pulse"></div>
    <HeroBanner 
      v-else-if="bannerData.is_active !== false"
      :banner="bannerData" 
    />

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
        
        <!-- Альбомы -->
        <div>
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-2xl font-semibold text-gray-800 dark:text-gray-200">📸 Фотоальбомы</h2>
            <NuxtLink to="/gallery" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
              Все альбомы →
            </NuxtLink>
          </div>
          
          <div v-if="albumsLoading" class="text-center py-10">
            <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
          </div>
          
          <div v-else-if="albums.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
            <p class="text-gray-500 dark:text-gray-400">Пока нет альбомов</p>
          </div>
          
          <div v-else>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
              <NuxtLink 
                v-for="album in albums.slice(0, 5)" 
                :key="album.id" 
                :to="`/gallery/${album.id}`" 
                class="group"
              >
                <div class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-xl transition overflow-hidden">
                  <div class="relative aspect-square overflow-hidden bg-gray-200 dark:bg-gray-700">
                    <img 
                      v-if="album.cover_image_url" 
                      :src="album.cover_image_url" 
                      :alt="album.title"
                      class="w-full h-full object-cover group-hover:scale-105 transition duration-300"
                    />
                    <div v-else class="w-full h-full flex items-center justify-center text-4xl text-gray-400 dark:text-gray-500">
                      📸
                    </div>
                    
                    <div class="absolute bottom-2 right-2 bg-black bg-opacity-60 text-white text-xs px-2 py-1 rounded-full">
                      {{ album.photos_count || 0 }} фото
                    </div>
                  </div>
                  
                  <div class="p-3">
                    <h3 class="text-sm font-semibold text-gray-800 dark:text-gray-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition line-clamp-1">
                      {{ album.title }}
                    </h3>
                    <p class="text-xs text-gray-400 dark:text-gray-500 mt-1 line-clamp-1">
                      📅 {{ formatDateShort(album.date) }}
                    </p>
                    <p v-if="!album.is_published && authStore.isEditor" class="text-xs text-yellow-600 dark:text-yellow-400 mt-1">
                      ⚠️ Черновик
                    </p>
                  </div>
                </div>
              </NuxtLink>
            </div>
            
            <div v-if="albums.length > 5" class="text-center mt-4">
              <NuxtLink to="/gallery" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition text-sm">
                Показать ещё {{ albums.length - 5 }} альбомов →
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
import HeroBanner from '~/components/features/banner/HeroBanner.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()

const bannerData = ref({
  title: '🏛️ Добро пожаловать в Центр Культуры',
  subtitle: 'Место, где искусство, традиции и творчество объединяются',
  has_background: false,
  background_image_url_display: '',
  button_text: '',
  button_link: '',
  button_enabled: true,
  is_active: true
})
const bannerLoading = ref(true)

const posts = ref([])
const events = ref([])
const authors = ref([])
const albums = ref([])
const postsLoading = ref(true)
const eventsLoading = ref(true)
const authorsLoading = ref(true)
const albumsLoading = ref(true)

const formatDateShort = (dateString) => {
  if (!dateString) return ''
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

// Загрузка баннера
onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const res = await fetch(`${API_URL}/banner/`)
    if (res.ok) {
      const data = await res.json()
      bannerData.value = {
        title: data.title || '🏛️ Добро пожаловать в Центр Культуры',
        subtitle: data.subtitle || 'Место, где искусство, традиции и творчество объединяются',
        has_background: data.has_background || false,
        background_image_url_display: data.background_image_url_display || '',
        button_text: data.button_text || '',
        button_link: data.button_link || '',
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : true,
        is_active: data.is_active !== undefined ? data.is_active : true
      }
    }
  } catch (e) {
    console.error('Ошибка загрузки баннера:', e)
  } finally {
    bannerLoading.value = false
  }
})

// Загрузка постов
onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/posts/`, { headers })
    if (res.ok) {
      posts.value = await res.json()
    } else {
      console.warn('Не удалось загрузить посты:', res.status)
      posts.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки постов:', e)
    posts.value = []
  } finally {
    postsLoading.value = false
  }
})

// Загрузка событий
onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/events/`, { headers })
    if (res.ok) {
      events.value = await res.json()
    } else {
      console.warn('Не удалось загрузить события:', res.status)
      events.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки событий:', e)
    events.value = []
  } finally {
    eventsLoading.value = false
  }
})

// Загрузка авторов
onMounted(async () => {
  try {
    const res = await fetch(`${API_URL}/auth/users/`)
    if (res.ok) {
      const allUsers = await res.json()
      authors.value = allUsers.filter(user => user.role === 'author' || user.role === 'editor')
    } else {
      authors.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки авторов:', e)
    authors.value = []
  } finally {
    authorsLoading.value = false
  }
})

// Загрузка альбомов
onMounted(async () => {
  try {
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    const res = await fetch(`${API_URL}/albums/`, { headers })
    if (res.ok) {
      albums.value = await res.json()
    } else {
      console.warn('Не удалось загрузить альбомы:', res.status)
      albums.value = []
    }
  } catch (e) {
    console.error('Ошибка загрузки альбомов:', e)
    albums.value = []
  } finally {
    albumsLoading.value = false
  }
})
</script>

<style scoped>
.line-clamp-1 {
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
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

#### `frontend/pages/profile/index.vue`

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
      <div class="flex justify-between items-start">
        <div class="flex flex-col items-center w-full">
          <div class="w-32 h-32 rounded-full bg-blue-500 flex items-center justify-center text-white text-5xl font-bold shadow-lg overflow-hidden">
            <img v-if="avatarPreview" :src="avatarPreview" alt="Аватар" class="w-full h-full object-cover">
            <span v-else>{{ userInitials }}</span>
          </div>
          <h2 class="text-2xl font-bold mt-3 text-gray-800 dark:text-gray-200">{{ fullName || username }}</h2>
          <p class="text-gray-500 dark:text-gray-400 text-sm">{{ roleDisplay }}</p>
        </div>
      </div>
      
      <div class="space-y-4 border-t border-gray-100 dark:border-gray-700 pt-6 mt-4">
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
      
      <div class="mt-6">
        <NuxtLink to="/profile/edit" class="block">
          <UiButton variant="primary" full-width>
            ✏️ Редактировать профиль
          </UiButton>
        </NuxtLink>
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
    
    <!-- МОИ КОММЕНТАРИИ (ГАЛЕРЕЯ) -->
    <div v-if="authStore.isAuthenticated" class="mt-10 border-t border-gray-200 dark:border-gray-700 pt-8">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">💬 Мои комментарии в галерее</h2>
      
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
          <NuxtLink :to="`/gallery/${comment.photo}`" class="block">
            <div class="flex justify-between items-start">
              <div>
                <p class="text-gray-700 dark:text-gray-300">{{ comment.content }}</p>
                <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">
                  К фото #{{ comment.photo }} • {{ formatDate(comment.created_at) }}
                </p>
              </div>
              <span class="text-xs bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300 px-2 py-1 rounded-full flex-shrink-0 ml-2">
                📸 Галерея
              </span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
    
    <!-- МОИ КОММЕНТАРИИ (ПОСТЫ) -->
    <div v-if="authStore.isAuthenticated" class="mt-10 border-t border-gray-200 dark:border-gray-700 pt-8">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4">💬 Мои комментарии к постам</h2>
      
      <div v-if="postCommentsLoading" class="text-center py-6">
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>
      
      <div v-else-if="postComments.length === 0" class="text-center py-6 text-gray-500 dark:text-gray-400">
        Нет комментариев
      </div>
      
      <div v-else class="space-y-3">
        <div 
          v-for="comment in postComments" 
          :key="comment.id" 
          class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg hover:shadow transition"
        >
          <NuxtLink :to="`/posts/${comment.post}`" class="block">
            <div class="flex justify-between items-start">
              <div>
                <p class="text-gray-700 dark:text-gray-300">{{ comment.content }}</p>
                <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">
                  К посту #{{ comment.post }} • {{ formatDate(comment.created_at) }}
                </p>
              </div>
              <span class="text-xs bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 px-2 py-1 rounded-full flex-shrink-0 ml-2">
                📝 Пост
              </span>
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase

const authStore = useAuthStore()

const loading = ref(true)
const error = ref('')

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

const userPosts = ref([])
const userPostsLoading = ref(true)
const postFilter = ref('all')

const userEvents = ref([])
const userEventsLoading = ref(true)
const eventFilter = ref('all')

const userComments = ref([])
const userCommentsLoading = ref(true)

const postComments = ref([])
const postCommentsLoading = ref(true)

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
    let allComments = []
    
    try {
      const postCommentsRes = await fetch(`${API_URL}/comments/my_comments/`, {
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        }
      })
      
      if (postCommentsRes.ok) {
        const postCommentsData = await postCommentsRes.json()
        allComments = [...allComments, ...postCommentsData.map(c => ({ ...c, type: 'post' }))]
      }
    } catch (e) {
      console.error('Ошибка загрузки комментариев к постам:', e)
    }
    
    try {
      const photoCommentsRes = await fetch(`${API_URL}/photo-comments/my_comments/`, {
        headers: {
          'Authorization': `Bearer ${authStore.accessToken}`
        }
      })
      
      if (photoCommentsRes.ok) {
        const photoCommentsData = await photoCommentsRes.json()
        allComments = [...allComments, ...photoCommentsData.map(c => ({ ...c, type: 'photo' }))]
      }
    } catch (e) {
      console.error('Ошибка загрузки комментариев к фото:', e)
    }
    
    allComments.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
    
    userComments.value = allComments.filter(c => c.type === 'photo')
    postComments.value = allComments.filter(c => c.type === 'post')
  } catch (e) {
    console.error('Ошибка загрузки комментариев:', e)
  } finally {
    userCommentsLoading.value = false
    postCommentsLoading.value = false
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

#### `frontend/pages/profile/edit.vue`

```vue
<template>
  <div class="max-w-4xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">✏️ Редактировать профиль</h1>
      <NuxtLink to="/profile" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition">
        ← Назад к профилю
      </NuxtLink>
    </div>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="error" class="text-red-500 text-center py-10">
      {{ error }}
    </div>
    
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
        <UiInput 
          v-model="form.username"
          label="Имя пользователя"
          disabled
        />
        
        <UiFileInput
          v-model="avatarFile"
          label="Аватар"
          accept="image/*"
          :max-size="2 * 1024 * 1024"
          hint="Рекомендуемый размер: 512x512px. Максимум 2MB."
        />
        
        <div class="grid grid-cols-2 gap-4">
          <UiInput 
            v-model="form.first_name"
            label="Имя"
          />
          <UiInput 
            v-model="form.last_name"
            label="Фамилия"
          />
        </div>
        
        <UiInput 
          v-model="form.patronymic"
          label="Отчество"
        />
        
        <UiInput 
          v-model="form.email"
          label="Email"
          type="email"
        />
        
        <UiInput 
          v-model="form.birth_date"
          label="Дата рождения"
          type="date"
        />
        
        <UiTextarea 
          v-model="form.bio"
          label="О себе"
          placeholder="Расскажите о себе..."
          rows="4"
        />
        
        <UiInput 
          v-model="form.role_display"
          label="Роль"
          disabled
        />
      </div>
      
      <div class="flex gap-3 mt-6">
        <UiButton 
          type="submit" 
          variant="primary"
          :disabled="submitting"
          full-width
        >
          {{ submitting ? 'Сохранение...' : '💾 Сохранить' }}
        </UiButton>
        <NuxtLink to="/profile" class="flex-1">
          <UiButton variant="secondary" full-width>
            Отмена
          </UiButton>
        </NuxtLink>
      </div>
      
      <p v-if="success" class="mt-4 text-green-500 text-sm text-center">{{ success }}</p>
      <p v-if="submitError" class="mt-4 text-red-500 text-sm text-center">{{ submitError }}</p>
    </form>
    
    <!-- Смена пароля -->
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
          <UiInput 
            v-model="passwordForm.old_password"
            label="Текущий пароль"
            type="password"
            required
          />
          
          <UiInput 
            v-model="passwordForm.new_password"
            label="Новый пароль"
            type="password"
            required
            hint="Минимум 8 символов"
          />
          
          <UiInput 
            v-model="passwordForm.new_password2"
            label="Подтвердите новый пароль"
            type="password"
            required
          />
          
          <div class="flex gap-3">
            <UiButton 
              type="submit"
              variant="primary"
              :disabled="passwordSubmitting"
            >
              {{ passwordSubmitting ? 'Сохранение...' : 'Сменить пароль' }}
            </UiButton>
            <UiButton 
              type="button"
              variant="secondary"
              @click="showChangePassword = false"
            >
              Отмена
            </UiButton>
          </div>
          
          <p v-if="passwordSuccess" class="mt-3 text-green-500 text-sm">{{ passwordSuccess }}</p>
          <p v-if="passwordError" class="mt-3 text-red-500 text-sm">{{ passwordError }}</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const router = useRouter()

const loading = ref(true)
const submitting = ref(false)
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

const showChangePassword = ref(false)
const passwordSubmitting = ref(false)
const passwordSuccess = ref('')
const passwordError = ref('')

const passwordForm = ref({
  old_password: '',
  new_password: '',
  new_password2: ''
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

onMounted(async () => {
  authStore.restoreAuth()
  
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
})

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
      if (avatarFile.value instanceof File) {
        formData.append('avatar', avatarFile.value)
        console.log('🖼️ Добавлен аватар:', avatarFile.value.name)
      } else if (Array.isArray(avatarFile.value) && avatarFile.value.length > 0) {
        const firstFile = avatarFile.value[0]
        if (firstFile instanceof File) {
          formData.append('avatar', firstFile)
          console.log('🖼️ Добавлен аватар из массива:', firstFile.name)
        }
      }
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
      
      success.value = '✅ Профиль обновлён!'
      
      setTimeout(() => {
        router.push('/profile')
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
      passwordSuccess.value = '✅ Пароль успешно изменён!'
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
```

---

#### `frontend/pages/settings/index.vue`

```vue
<template>
  <div class="max-w-5xl mx-auto mt-10 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">⚙️ Настройки сайта</h1>
      <NuxtLink 
        to="/" 
        class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition"
      >
        ← На главную
      </NuxtLink>
    </div>
    
    <div v-if="!authStore.isEditor" class="bg-white dark:bg-gray-800 p-8 rounded-lg shadow text-center py-20">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главные редакторы могут управлять настройками сайта.</p>
      <NuxtLink to="/" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        На главную
      </NuxtLink>
    </div>
    
    <template v-else>
      <!-- Вкладки -->
      <div class="flex gap-2 mb-6 border-b border-gray-200 dark:border-gray-700 overflow-x-auto">
        <button 
          @click="activeTab = 'banner'"
          class="px-6 py-3 font-medium transition rounded-t-lg whitespace-nowrap"
          :class="activeTab === 'banner' 
            ? 'bg-blue-500 text-white' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          🎨 Баннер
        </button>
        <button 
          @click="activeTab = 'contacts'"
          class="px-6 py-3 font-medium transition rounded-t-lg whitespace-nowrap"
          :class="activeTab === 'contacts' 
            ? 'bg-blue-500 text-white' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          📞 Контакты
        </button>
        <button 
          @click="activeTab = 'gallery'"
          class="px-6 py-3 font-medium transition rounded-t-lg whitespace-nowrap"
          :class="activeTab === 'gallery' 
            ? 'bg-blue-500 text-white' 
            : 'text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'"
        >
          📸 Галерея
        </button>
      </div>
      
      <!-- Блок настроек баннера -->
      <div v-show="activeTab === 'banner'" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">🎨 Настройка баннера</h2>
        
        <div class="mb-6 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700">
          <HeroBanner :banner="bannerPreview" />
        </div>
        
        <form @submit.prevent="updateBanner" enctype="multipart/form-data">
          <UiInput 
            v-model="bannerForm.title"
            label="Заголовок"
            placeholder="Введите заголовок баннера"
            required
          />
          
          <UiTextarea 
            v-model="bannerForm.subtitle"
            label="Подзаголовок"
            placeholder="Введите подзаголовок баннера"
            rows="3"
            required
          />
          
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Фоновое изображение</label>
            
            <div v-if="bannerForm.background_image_url_display && !bannerImageRemoved" class="mb-3">
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее изображение:</p>
              <div class="relative inline-block">
                <img 
                  :src="bannerForm.background_image_url_display" 
                  alt="Фон баннера" 
                  class="max-h-48 rounded-lg object-cover border border-gray-200 dark:border-gray-700"
                >
                <button 
                  @click="removeBannerImage"
                  type="button"
                  class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 transition text-sm"
                >
                  ✕
                </button>
              </div>
            </div>
            
            <div class="flex flex-col gap-2">
              <UiInput 
                v-model="bannerForm.background_image_url"
                placeholder="https://example.com/banner.jpg"
                @input="onUrlInput"
              />
              <div class="flex items-center gap-2">
                <span class="text-gray-500 dark:text-gray-400 text-sm">или</span>
                <input 
                  type="file" 
                  accept="image/*"
                  @change="onBannerFileSelected"
                  class="flex-1 border border-gray-300 dark:border-gray-600 rounded-lg p-2 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm cursor-pointer"
                >
              </div>
            </div>
            
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 1920x600px. Максимум 5MB.</p>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <UiInput 
              v-model="bannerForm.button_text"
              label="Текст кнопки"
              placeholder="Смотреть афишу"
            />
            
            <UiInput 
              v-model="bannerForm.button_link"
              label="Ссылка кнопки"
              placeholder="/events"
            />
          </div>
          
          <div class="mb-4">
            <UiCheckbox v-model="bannerForm.button_enabled">
              Показывать кнопку
            </UiCheckbox>
          </div>
          
          <div class="mb-6">
            <UiCheckbox v-model="bannerForm.is_active">
              Баннер активен (отображается на главной)
            </UiCheckbox>
          </div>
          
          <div class="flex gap-3">
            <UiButton 
              type="submit" 
              variant="primary"
              :disabled="bannerSubmitting"
            >
              {{ bannerSubmitting ? 'Сохранение...' : '💾 Сохранить баннер' }}
            </UiButton>
            <UiButton 
              type="button"
              variant="warning"
              @click="confirmResetBanner"
            >
              ↩️ Сбросить
            </UiButton>
          </div>
          
          <p v-if="bannerSubmitError" class="mt-4 text-red-500 text-sm">{{ bannerSubmitError }}</p>
          <p v-if="bannerSuccess" class="mt-4 text-green-500 text-sm">{{ bannerSuccess }}</p>
        </form>
      </div>
      
      <!-- Блок настроек контактов -->
      <div v-show="activeTab === 'contacts'" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">📞 Настройка контактов</h2>
        
        <form @submit.prevent="updateContacts">
          <UiInput 
            v-model="contactsForm.address"
            label="Адрес"
            placeholder="г. Москва, ул. Культурная, д. 1"
          />
          
          <UiInput 
            v-model="contactsForm.phone"
            label="Телефон"
            placeholder="+7 (495) 123-45-67"
          />
          
          <UiInput 
            v-model="contactsForm.email"
            label="Email"
            type="email"
            placeholder="info@kultcentr.ru"
          />
          
          <UiInput 
            v-model="contactsForm.work_hours"
            label="Часы работы"
            placeholder="Пн–Пт: 10:00 – 20:00"
          />
          
          <UiTextarea 
            v-model="contactsForm.description"
            label="Описание"
            placeholder="Описание организации..."
            rows="3"
          />
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <UiInput 
              v-model="contactsForm.instagram"
              label="Instagram"
              placeholder="https://instagram.com/..."
            />
            
            <UiInput 
              v-model="contactsForm.vk"
              label="ВКонтакте"
              placeholder="https://vk.com/..."
            />
            
            <UiInput 
              v-model="contactsForm.telegram"
              label="Telegram"
              placeholder="https://t.me/..."
            />
          </div>
          
          <div class="flex gap-3 mt-4">
            <UiButton 
              type="submit" 
              variant="primary"
              :disabled="contactsSubmitting"
            >
              {{ contactsSubmitting ? 'Сохранение...' : '💾 Сохранить контакты' }}
            </UiButton>
            <UiButton 
              type="button"
              variant="secondary"
              @click="resetContactsForm"
            >
              ↩️ Сбросить
            </UiButton>
          </div>
          
          <p v-if="contactsSubmitError" class="mt-4 text-red-500 text-sm">{{ contactsSubmitError }}</p>
          <p v-if="contactsSuccess" class="mt-4 text-green-500 text-sm">{{ contactsSuccess }}</p>
        </form>
      </div>
      
      <!-- Блок настроек галереи -->
      <div v-show="activeTab === 'gallery'" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
        <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">📸 Управление галереей</h2>
        
        <div class="space-y-4">
          <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
            <p class="text-gray-600 dark:text-gray-300">
              Управление альбомами и фотографиями доступно через страницу галереи.
            </p>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">
              Вы можете создавать альбомы, загружать фотографии, редактировать и удалять их.
            </p>
            <NuxtLink 
              to="/gallery" 
              class="inline-block mt-3 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition"
            >
              Перейти в галерею →
            </NuxtLink>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-blue-50 dark:bg-blue-900/20 p-4 rounded-lg border border-blue-200 dark:border-blue-800">
              <div class="text-2xl mb-2">📸</div>
              <h3 class="font-semibold text-gray-800 dark:text-gray-200">Создание альбомов</h3>
              <p class="text-sm text-gray-600 dark:text-gray-400">Создавайте альбомы с названием, описанием и датой события</p>
            </div>
            
            <div class="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg border border-green-200 dark:border-green-800">
              <div class="text-2xl mb-2">📤</div>
              <h3 class="font-semibold text-gray-800 dark:text-gray-200">Загрузка фото</h3>
              <p class="text-sm text-gray-600 dark:text-gray-400">Загружайте несколько фотографий одновременно в любой альбом</p>
            </div>
            
            <div class="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-lg border border-purple-200 dark:border-purple-800">
              <div class="text-2xl mb-2">🖼️</div>
              <h3 class="font-semibold text-gray-800 dark:text-gray-200">Просмотр</h3>
              <p class="text-sm text-gray-600 dark:text-gray-400">Удобный просмотр с Lightbox и навигацией между фото</p>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import HeroBanner from '~/components/features/banner/HeroBanner.vue'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiCheckbox from '~/components/ui/UiCheckbox.vue'

definePageMeta({
  middleware: ['auth', 'editor']
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const router = useRouter()

// Активная вкладка
const activeTab = ref('banner')

// ========== НАСТРОЙКИ БАННЕРА ==========
const bannerLoading = ref(true)
const bannerSubmitting = ref(false)
const bannerSubmitError = ref('')
const bannerSuccess = ref('')

const bannerImageFile = ref(null)
const bannerImagePreview = ref('')
const bannerImageRemoved = ref(false)

const DEFAULT_BANNER = {
  title: '🏛️ Добро пожаловать в Центр Культуры',
  subtitle: 'Место, где искусство, традиции и творчество объединяются',
  background_image_url: '',
  background_image_url_display: '',
  button_text: 'Смотреть афишу',
  button_link: '/events',
  button_enabled: true,
  is_active: true
}

const bannerForm = ref({
  title: '',
  subtitle: '',
  background_image_url: '',
  background_image_url_display: '',
  button_text: '',
  button_link: '',
  button_enabled: true,
  is_active: true
})

const bannerOriginalForm = ref({})

const bannerPreview = computed(() => ({
  ...bannerForm.value,
  has_background: !!(bannerForm.value.background_image_url_display || bannerImagePreview.value) && !bannerImageRemoved.value,
  background_image_url_display: bannerImagePreview.value || (bannerImageRemoved.value ? '' : bannerForm.value.background_image_url_display)
}))

const onBannerFileSelected = (event) => {
  const file = event.target.files[0]
  if (file) {
    bannerImageFile.value = file
    bannerImagePreview.value = URL.createObjectURL(file)
    bannerForm.value.background_image_url = ''
    bannerImageRemoved.value = false
  }
}

const onUrlInput = () => {
  if (bannerForm.value.background_image_url) {
    bannerImageRemoved.value = false
    bannerImageFile.value = null
    bannerImagePreview.value = ''
  }
}

const removeBannerImage = () => {
  bannerImageFile.value = null
  bannerImagePreview.value = ''
  bannerForm.value.background_image_url = ''
  bannerForm.value.background_image_url_display = ''
  bannerImageRemoved.value = true
}

const resetBannerForm = () => {
  bannerForm.value = { ...bannerOriginalForm.value }
  bannerImageFile.value = null
  bannerImagePreview.value = ''
  bannerImageRemoved.value = false
  bannerSubmitError.value = ''
  bannerSuccess.value = ''
}

const confirmResetBanner = () => {
  if (confirm('Вы уверены, что хотите сбросить настройки баннера к значениям по умолчанию?')) {
    applyDefaultBannerSettings()
  }
}

const applyDefaultBannerSettings = async () => {
  bannerSubmitting.value = true
  bannerSubmitError.value = ''
  bannerSuccess.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', DEFAULT_BANNER.title)
    formData.append('subtitle', DEFAULT_BANNER.subtitle)
    formData.append('button_text', DEFAULT_BANNER.button_text)
    formData.append('button_link', DEFAULT_BANNER.button_link)
    formData.append('button_enabled', DEFAULT_BANNER.button_enabled ? 'true' : 'false')
    formData.append('is_active', DEFAULT_BANNER.is_active ? 'true' : 'false')
    formData.append('background_image_url', '')
    
    const res = await fetch(`${API_URL}/banner/update/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const data = await res.json()
      bannerForm.value = {
        title: data.title || DEFAULT_BANNER.title,
        subtitle: data.subtitle || DEFAULT_BANNER.subtitle,
        background_image_url: data.background_image_url || '',
        background_image_url_display: data.background_image_url_display || '',
        button_text: data.button_text || DEFAULT_BANNER.button_text,
        button_link: data.button_link || DEFAULT_BANNER.button_link,
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : DEFAULT_BANNER.button_enabled,
        is_active: data.is_active !== undefined ? data.is_active : DEFAULT_BANNER.is_active
      }
      bannerOriginalForm.value = { ...bannerForm.value }
      bannerImageFile.value = null
      bannerImagePreview.value = ''
      bannerImageRemoved.value = false
      
      bannerSuccess.value = '✅ Настройки баннера сброшены к значениям по умолчанию!'
      
      setTimeout(() => {
        bannerSuccess.value = ''
      }, 3000)
    } else {
      const data = await res.json()
      bannerSubmitError.value = data.detail || data.message || 'Ошибка сброса настроек'
      console.error('Ошибка сервера:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    bannerSubmitError.value = 'Ошибка подключения к серверу'
  } finally {
    bannerSubmitting.value = false
  }
}

// ========== НАСТРОЙКИ КОНТАКТОВ ==========
const contactsLoading = ref(true)
const contactsSubmitting = ref(false)
const contactsSubmitError = ref('')
const contactsSuccess = ref('')

const DEFAULT_CONTACTS = {
  address: 'г. Москва, ул. Культурная, д. 1',
  phone: '+7 (495) 123-45-67',
  email: 'info@kultcentr.ru',
  work_hours: 'Пн–Пт: 10:00 – 20:00',
  description: 'Место, где искусство, традиции и творчество объединяются.\nМы создаём пространство для культурного развития и вдохновения.',
  instagram: '',
  vk: '',
  telegram: ''
}

const contactsForm = ref({
  address: '',
  phone: '',
  email: '',
  work_hours: '',
  description: '',
  instagram: '',
  vk: '',
  telegram: ''
})

const contactsOriginalForm = ref({})

const resetContactsForm = () => {
  if (confirm('Вы уверены, что хотите сбросить настройки контактов к значениям по умолчанию?')) {
    applyDefaultContactsSettings()
  }
}

const applyDefaultContactsSettings = async () => {
  contactsSubmitting.value = true
  contactsSubmitError.value = ''
  contactsSuccess.value = ''
  
  try {
    const res = await fetch(`${API_URL}/contact-info/update/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(DEFAULT_CONTACTS)
    })
    
    if (res.ok) {
      const data = await res.json()
      contactsForm.value = {
        address: data.address || DEFAULT_CONTACTS.address,
        phone: data.phone || DEFAULT_CONTACTS.phone,
        email: data.email || DEFAULT_CONTACTS.email,
        work_hours: data.work_hours || DEFAULT_CONTACTS.work_hours,
        description: data.description || DEFAULT_CONTACTS.description,
        instagram: data.instagram || '',
        vk: data.vk || '',
        telegram: data.telegram || ''
      }
      contactsOriginalForm.value = { ...contactsForm.value }
      
      contactsSuccess.value = '✅ Настройки контактов сброшены к значениям по умолчанию!'
      
      if (typeof window !== 'undefined') {
        window.dispatchEvent(new Event('contacts-updated'))
      }
      
      setTimeout(() => {
        contactsSuccess.value = ''
      }, 3000)
    } else {
      const data = await res.json()
      contactsSubmitError.value = data.detail || 'Ошибка сброса настроек'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    contactsSubmitError.value = 'Ошибка подключения к серверу'
  } finally {
    contactsSubmitting.value = false
  }
}

// ========== ЗАГРУЗКА ДАННЫХ ==========
onMounted(async () => {
  authStore.restoreAuth()
  await loadBanner()
  await loadContacts()
})

const loadBanner = async () => {
  try {
    const res = await fetch(`${API_URL}/banner/`)
    if (res.ok) {
      const data = await res.json()
      bannerForm.value = {
        title: data.title || DEFAULT_BANNER.title,
        subtitle: data.subtitle || DEFAULT_BANNER.subtitle,
        background_image_url: data.background_image_url || '',
        background_image_url_display: data.background_image_url_display || '',
        button_text: data.button_text || DEFAULT_BANNER.button_text,
        button_link: data.button_link || DEFAULT_BANNER.button_link,
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : DEFAULT_BANNER.button_enabled,
        is_active: data.is_active !== undefined ? data.is_active : DEFAULT_BANNER.is_active
      }
      bannerOriginalForm.value = { ...bannerForm.value }
      bannerImageRemoved.value = false
    }
  } catch (e) {
    console.error('Ошибка загрузки баннера:', e)
  } finally {
    bannerLoading.value = false
  }
}

const loadContacts = async () => {
  try {
    const res = await fetch(`${API_URL}/contact-info/`)
    if (res.ok) {
      const data = await res.json()
      contactsForm.value = {
        address: data.address || DEFAULT_CONTACTS.address,
        phone: data.phone || DEFAULT_CONTACTS.phone,
        email: data.email || DEFAULT_CONTACTS.email,
        work_hours: data.work_hours || DEFAULT_CONTACTS.work_hours,
        description: data.description || DEFAULT_CONTACTS.description,
        instagram: data.instagram || '',
        vk: data.vk || '',
        telegram: data.telegram || ''
      }
      contactsOriginalForm.value = { ...contactsForm.value }
    }
  } catch (e) {
    console.error('Ошибка загрузки контактов:', e)
  } finally {
    contactsLoading.value = false
  }
}

// ========== ОБНОВЛЕНИЕ БАННЕРА ==========
const updateBanner = async () => {
  if (!bannerForm.value.title || !bannerForm.value.subtitle) {
    bannerSubmitError.value = 'Заполните заголовок и подзаголовок'
    return
  }
  
  bannerSubmitting.value = true
  bannerSubmitError.value = ''
  bannerSuccess.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', bannerForm.value.title)
    formData.append('subtitle', bannerForm.value.subtitle)
    formData.append('button_text', bannerForm.value.button_text || '')
    formData.append('button_link', bannerForm.value.button_link || '')
    formData.append('button_enabled', bannerForm.value.button_enabled ? 'true' : 'false')
    formData.append('is_active', bannerForm.value.is_active ? 'true' : 'false')
    
    if (bannerImageRemoved.value) {
      formData.append('background_image_url', '')
    } else if (bannerForm.value.background_image_url) {
      formData.append('background_image_url', bannerForm.value.background_image_url)
    }
    
    if (bannerImageFile.value) {
      formData.append('background_image', bannerImageFile.value)
    }
    
    const res = await fetch(`${API_URL}/banner/update/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const data = await res.json()
      bannerForm.value = {
        ...bannerForm.value,
        title: data.title,
        subtitle: data.subtitle,
        background_image_url: data.background_image_url,
        background_image_url_display: data.background_image_url_display,
        button_text: data.button_text || '',
        button_link: data.button_link || '',
        button_enabled: data.button_enabled !== undefined ? data.button_enabled : true,
        is_active: data.is_active
      }
      bannerOriginalForm.value = { ...bannerForm.value }
      bannerImageFile.value = null
      bannerImagePreview.value = ''
      bannerImageRemoved.value = false
      
      bannerSuccess.value = '✅ Баннер успешно обновлён!'
      
      setTimeout(() => {
        bannerSuccess.value = ''
      }, 3000)
    } else {
      const data = await res.json()
      bannerSubmitError.value = data.detail || data.message || 'Ошибка обновления'
      console.error('Ошибка сервера:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    bannerSubmitError.value = 'Ошибка подключения к серверу'
  } finally {
    bannerSubmitting.value = false
  }
}

// ========== ОБНОВЛЕНИЕ КОНТАКТОВ ==========
const updateContacts = async () => {
  contactsSubmitting.value = true
  contactsSubmitError.value = ''
  contactsSuccess.value = ''
  
  try {
    const res = await fetch(`${API_URL}/contact-info/update/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: JSON.stringify(contactsForm.value)
    })
    
    if (res.ok) {
      const data = await res.json()
      contactsForm.value = {
        address: data.address || '',
        phone: data.phone || '',
        email: data.email || '',
        work_hours: data.work_hours || '',
        description: data.description || '',
        instagram: data.instagram || '',
        vk: data.vk || '',
        telegram: data.telegram || ''
      }
      contactsOriginalForm.value = { ...contactsForm.value }
      
      contactsSuccess.value = '✅ Контакты успешно обновлены!'
      
      if (typeof window !== 'undefined') {
        window.dispatchEvent(new Event('contacts-updated'))
      }
      
      setTimeout(() => {
        contactsSuccess.value = ''
      }, 3000)
    } else {
      const data = await res.json()
      contactsSubmitError.value = data.detail || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    contactsSubmitError.value = 'Ошибка подключения к серверу'
  } finally {
    contactsSubmitting.value = false
  }
}
</script>
```

---

#### `frontend/pages/contacts/index.vue`

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
              to="/settings" 
              class="inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
            >
              ⚙️ Редактировать контакты
            </NuxtLink>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-2">
              Перейти в настройки для редактирования контактов
            </p>
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

#### `frontend/pages/auth/login.vue`

```vue
<template>
  <div class="max-w-md mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">Вход</h1>
    
    <form @submit.prevent="login">
      <UiInput 
        v-model="username"
        label="Имя пользователя"
        placeholder="Введите имя пользователя"
        required
      />
      
      <UiInput 
        v-model="password"
        label="Пароль"
        type="password"
        placeholder="Введите пароль"
        required
      />
      
      <UiButton 
        type="submit" 
        variant="primary"
        :disabled="loading"
        full-width
      >
        {{ loading ? 'Вход...' : 'Войти' }}
      </UiButton>
      
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
          <UiInput 
            v-model="resetEmail"
            label="Email или имя пользователя"
            placeholder="email@example.com или username"
            required
          />
          
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="resetLoading"
            full-width
          >
            {{ resetLoading ? 'Отправка...' : 'Отправить ссылку' }}
          </UiButton>
          
          <p v-if="resetSuccess" class="mt-3 text-green-500 text-sm">{{ resetSuccess }}</p>
          <p v-if="resetError" class="mt-3 text-red-500 text-sm">{{ resetError }}</p>
        </form>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'

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

#### `frontend/pages/auth/register.vue`

```vue
<template>
  <div class="max-w-md mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">Регистрация</h1>
    
    <form @submit.prevent="register">
      <UiInput 
        v-model="username"
        label="Имя пользователя"
        placeholder="Введите имя пользователя"
        required
      />
      
      <UiInput 
        v-model="email"
        label="Email"
        type="email"
        placeholder="example@mail.com"
        required
      />
      
      <UiInput 
        v-model="password"
        label="Пароль"
        type="password"
        placeholder="Введите пароль"
        required
        hint="Минимум 8 символов"
      />
      
      <UiInput 
        v-model="password2"
        label="Подтвердите пароль"
        type="password"
        placeholder="Повторите пароль"
        required
      />
      
      <UiButton 
        type="submit" 
        variant="primary"
        :disabled="loading"
        full-width
      >
        {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
      </UiButton>
      
      <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      <p v-if="successMessage" class="mt-4 text-green-500 text-sm">{{ successMessage }}</p>
      
      <p class="mt-4 text-center text-gray-600 dark:text-gray-400">
        Уже есть аккаунт? <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">Войти</NuxtLink>
      </p>
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'

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
  
  if (password.value.length < 8) {
    error.value = 'Пароль должен содержать минимум 8 символов'
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
      successMessage.value = '✅ Регистрация успешна! Теперь вы можете войти.'
      error.value = ''
      username.value = ''
      email.value = ''
      password.value = ''
      password2.value = ''
      
      setTimeout(() => {
        router.push('/auth/login')
      }, 2000)
    } else {
      if (data.email) {
        error.value = `Email: ${data.email.join(', ')}`
      } else if (data.username) {
        error.value = `Имя пользователя: ${data.username.join(', ')}`
      } else if (data.password) {
        error.value = `Пароль: ${data.password.join(', ')}`
      } else if (data.password2) {
        error.value = `Подтверждение пароля: ${data.password2.join(', ')}`
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

#### `frontend/pages/posts/index.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">📝 Все публикации</h1>
    </div>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="posts.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">Нет публикаций</p>
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

#### `frontend/pages/posts/create.vue`

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
        <UiInput 
          v-model="title"
          label="Заголовок"
          placeholder="Введите заголовок поста"
          required
        />
        
        <UiInput 
          v-model="excerpt"
          label="Краткое описание"
          placeholder="Короткое описание..."
        />
        
        <UiTextarea 
          v-model="content"
          label="Содержание"
          placeholder="Текст поста..."
          rows="10"
          required
        />
        
        <UiFileInput
          v-model="imageFile"
          label="Изображение"
          accept="image/*"
          :max-size="5 * 1024 * 1024"
          hint="Рекомендуемый размер: 1920x1080px. Максимум 5MB."
        />
        
        <div class="mb-6">
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Статус публикации</label>
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
        
        <div class="flex flex-wrap gap-3">
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="submitting"
          >
            {{ submitting ? 'Создание...' : is_published ? 'Опубликовать' : 'Сохранить черновик' }}
          </UiButton>
          
          <NuxtLink to="/">
            <UiButton variant="secondary">
              Отменить
            </UiButton>
          </NuxtLink>
        </div>
        
        <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const router = useRouter()

const submitting = ref(false)
const error = ref('')

const title = ref('')
const excerpt = ref('')
const content = ref('')
const imageFile = ref(null)
const is_published = ref(true)

const createPost = async () => {
  if (!title.value || !content.value) {
    error.value = 'Заполните заголовок и содержание'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    let finalImageUrl = null
    
    if (imageFile.value) {
      if (imageFile.value instanceof File) {
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
          console.log('🖼️ Изображение загружено:', finalImageUrl)
        } else {
          const err = await uploadRes.json()
          error.value = err.detail || 'Ошибка загрузки изображения'
          submitting.value = false
          return
        }
      } else if (Array.isArray(imageFile.value) && imageFile.value.length > 0) {
        const firstFile = imageFile.value[0]
        if (firstFile instanceof File) {
          const formData = new FormData()
          formData.append('image', firstFile)
          
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
            console.log('🖼️ Изображение загружено из массива:', finalImageUrl)
          } else {
            const err = await uploadRes.json()
            error.value = err.detail || 'Ошибка загрузки изображения'
            submitting.value = false
            return
          }
        }
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
      console.error('Ошибка:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>
```

---

#### `frontend/pages/posts/[id].vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <NuxtLink to="/posts" class="text-blue-500 dark:text-blue-400 hover:underline mb-4 inline-block">
      ← Назад к списку
    </NuxtLink>

    <div v-if="post" class="bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden">
      <div v-if="post.display_image" class="w-full max-h-96 overflow-hidden">
        <img :src="post.display_image" :alt="post.title" class="w-full h-full object-cover">
      </div>
      
      <div class="p-8">
        <div class="flex justify-between items-start mb-2">
          <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">{{ post.title }}</h1>
          
          <div 
            v-if="authStore.isAuthenticated && (authStore.user?.username === post.author_name || authStore.isEditor)" 
            class="flex gap-2 flex-shrink-0 ml-4"
          >
            <NuxtLink :to="`/posts/edit-${post.id}`">
              <UiButton variant="warning" size="sm">
                ✏️ Редактировать
              </UiButton>
            </NuxtLink>
            
            <UiButton 
              @click="deletePost"
              variant="danger"
              size="sm"
              :disabled="deleting"
            >
              {{ deleting ? 'Удаление...' : '🗑️ Удалить' }}
            </UiButton>
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
        <UiButton 
          type="submit"
          variant="primary"
          :disabled="submitting"
          class="mt-2"
        >
          {{ submitting ? 'Отправка...' : replyToCommentId ? 'Ответить' : 'Отправить' }}
        </UiButton>
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
import UiButton from '~/components/ui/UiButton.vue'

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

#### `frontend/pages/posts/edit-[id].vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">✏️ Редактировать пост</h1>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="errorMessage" class="text-center py-10 text-red-500">
      {{ errorMessage }}
    </div>
    
    <form v-else @submit.prevent="updatePost" enctype="multipart/form-data">
      <UiInput 
        v-model="form.title"
        label="Заголовок"
        placeholder="Введите заголовок поста"
        required
      />
      
      <UiInput 
        v-model="form.excerpt"
        label="Краткое описание"
        placeholder="Короткое описание..."
      />
      
      <UiTextarea 
        v-model="form.content"
        label="Содержание"
        placeholder="Текст поста..."
        rows="10"
        required
      />
      
      <div class="mb-4">
        <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Изображение</label>
        
        <div v-if="form.image_url && !imageRemoved && !imagePreview" class="mb-3">
          <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее изображение:</p>
          <div class="relative inline-block">
            <img 
              :src="form.image_url" 
              alt="Изображение" 
              class="max-h-48 rounded-lg object-cover border border-gray-200 dark:border-gray-700"
            >
            <button 
              @click="removeImage"
              type="button"
              class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 transition text-sm"
            >
              ✕
            </button>
          </div>
        </div>
        
        <UiFileInput
          v-model="imageFile"
          label=""
          accept="image/*"
          :max-size="5 * 1024 * 1024"
          hint="Выберите новое изображение для замены"
        />
        
        <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 1920x1080px. Максимум 5MB.</p>
      </div>
      
      <div class="mb-6">
        <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Статус публикации</label>
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
      
      <div class="flex flex-wrap gap-3">
        <UiButton 
          type="submit" 
          variant="primary"
          :disabled="submitting"
        >
          {{ submitting ? 'Сохранение...' : form.is_published ? 'Опубликовать' : 'Сохранить черновик' }}
        </UiButton>
        
        <NuxtLink :to="`/posts/${postId}`">
          <UiButton variant="secondary">
            Отменить
          </UiButton>
        </NuxtLink>
        
        <UiButton 
          type="button"
          variant="danger"
          @click="deletePost"
        >
          🗑️ Удалить пост
        </UiButton>
      </div>
      
      <p v-if="submitError" class="mt-4 text-red-500 text-sm">{{ submitError }}</p>
    </form>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const postId = computed(() => {
  const id = route.params.id
  if (typeof id === 'string' && id.includes('edit-')) {
    return id.replace('edit-', '')
  }
  return id
})

const loading = ref(true)
const submitting = ref(false)
const errorMessage = ref('')
const submitError = ref('')

const imageFile = ref(null)
const imageRemoved = ref(false)

const form = ref({
  title: '',
  excerpt: '',
  content: '',
  image_url: '',
  is_published: true
})

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const id = postId.value
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
      console.log('📥 Загружен пост:', form.value)
    } else {
      errorMessage.value = 'Пост не найден'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    errorMessage.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})

const removeImage = () => {
  imageRemoved.value = true
  form.value.image_url = ''
  imageFile.value = null
  console.log('🖼️ Изображение помечено на удаление')
}

const updatePost = async () => {
  if (!form.value.title || !form.value.content) {
    submitError.value = 'Заполните заголовок и содержание'
    return
  }
  
  submitting.value = true
  submitError.value = ''
  
  try {
    let finalImageUrl = form.value.image_url || null
    
    if (imageFile.value) {
      if (imageFile.value instanceof File) {
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
          console.log('🖼️ Новое изображение загружено:', finalImageUrl)
        } else {
          const err = await uploadRes.json()
          submitError.value = err.detail || 'Ошибка загрузки изображения'
          submitting.value = false
          return
        }
      } else if (Array.isArray(imageFile.value) && imageFile.value.length > 0) {
        const firstFile = imageFile.value[0]
        if (firstFile instanceof File) {
          const formData = new FormData()
          formData.append('image', firstFile)
          
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
            console.log('🖼️ Новое изображение из массива загружено:', finalImageUrl)
          } else {
            const err = await uploadRes.json()
            submitError.value = err.detail || 'Ошибка загрузки изображения'
            submitting.value = false
            return
          }
        }
      }
    }
    
    if (imageRemoved.value) {
      finalImageUrl = null
      console.log('🖼️ Изображение удалено')
    }
    
    const id = postId.value
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
      console.log('✅ Пост обновлён:', post)
      router.push(`/posts/${post.id}`)
    } else {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
      console.error('Ошибка:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const deletePost = async () => {
  if (!confirm(`Вы уверены, что хотите удалить пост "${form.value.title}"?`)) return
  
  try {
    const id = postId.value
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

#### `frontend/pages/events/index.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">🎭 Афиша</h1>
    </div>
    
    <div v-if="loading" class="text-center py-10">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="events.length === 0" class="text-center py-10 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">Пока нет событий</p>
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <NuxtLink 
        v-for="event in events" 
        :key="event.id" 
        :to="`/events/${event.id}`" 
        class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-lg transition overflow-hidden flex flex-col"
      >
        <div v-if="event.display_image" class="h-48 overflow-hidden flex-shrink-0">
          <img :src="event.display_image" :alt="event.title" class="w-full h-full object-cover">
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

#### `frontend/pages/events/create.vue`

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
        <UiInput 
          v-model="title"
          label="Название события"
          placeholder="Введите название события"
          required
        />
        
        <UiInput 
          v-model="excerpt"
          label="Краткое описание"
          placeholder="Короткое описание..."
        />
        
        <UiTextarea 
          v-model="content"
          label="Полное описание"
          placeholder="Подробное описание события..."
          rows="8"
          required
        />
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <UiInput 
            v-model="event_date"
            label="Дата и время"
            type="datetime-local"
          />
          
          <UiInput 
            v-model="location"
            label="Место проведения"
            placeholder="Где пройдёт событие..."
          />
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <UiInput 
            v-model="price"
            label="Стоимость"
            placeholder="Бесплатно / 500 ₽..."
          />
          
          <UiFileInput
            v-model="imageFile"
            label="Изображение"
            accept="image/*"
            :max-size="5 * 1024 * 1024"
            hint="Рекомендуемый размер: 1920x1080px. Максимум 5MB."
          />
        </div>
        
        <div class="mb-6">
          <UiCheckbox v-model="is_published">
            Опубликовать сразу
          </UiCheckbox>
        </div>
        
        <div class="flex flex-wrap gap-3">
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="submitting"
          >
            {{ submitting ? 'Создание...' : '📸 Создать' }}
          </UiButton>
          
          <NuxtLink to="/events">
            <UiButton variant="secondary">
              Отмена
            </UiButton>
          </NuxtLink>
        </div>
        
        <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiCheckbox from '~/components/ui/UiCheckbox.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const router = useRouter()

const submitting = ref(false)
const error = ref('')

const title = ref('')
const excerpt = ref('')
const content = ref('')
const event_date = ref('')
const location = ref('')
const price = ref('')
const imageFile = ref(null)
const is_published = ref(true)

const createEvent = async () => {
  if (!title.value || !content.value) {
    error.value = 'Заполните название и описание'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', title.value)
    formData.append('excerpt', excerpt.value || '')
    formData.append('content', content.value)
    formData.append('event_date', event_date.value || '')
    formData.append('location', location.value || '')
    formData.append('price', price.value || '')
    formData.append('is_published', is_published.value ? 'true' : 'false')
    
    if (imageFile.value) {
      if (imageFile.value instanceof File) {
        formData.append('image', imageFile.value)
        console.log('🖼️ Добавлено изображение:', imageFile.value.name)
      } else if (Array.isArray(imageFile.value) && imageFile.value.length > 0) {
        const firstFile = imageFile.value[0]
        if (firstFile instanceof File) {
          formData.append('image', firstFile)
          console.log('🖼️ Добавлено изображение из массива:', firstFile.name)
        }
      }
    }
    
    console.log('📤 Отправка данных...')
    for (let pair of formData.entries()) {
      if (pair[1] instanceof File) {
        console.log(`  ${pair[0]}: ${pair[1].name} (${pair[1].size} байт)`)
      } else {
        console.log(`  ${pair[0]}: ${pair[1]}`)
      }
    }
    
    const res = await fetch(`${API_URL}/events/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const event = await res.json()
      console.log('✅ Событие создано:', event)
      router.push(`/events/${event.id}`)
    } else {
      const data = await res.json()
      console.error('❌ Ошибка:', data)
      error.value = data.detail || 'Ошибка создания события'
    }
  } catch (e) {
    console.error('❌ Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>
```

---

#### `frontend/pages/events/[id].vue`

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
      <div v-if="event.display_image || event.image_url" class="w-full h-96 overflow-hidden">
        <img 
          :src="event.display_image || event.image_url" 
          :alt="event.title" 
          class="w-full h-full object-cover"
        />
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
            <NuxtLink :to="`/events/edit-${event.id}`">
              <UiButton variant="warning" size="sm">
                ✏️ Редактировать
              </UiButton>
            </NuxtLink>
            <UiButton 
              @click="deleteEvent"
              variant="danger"
              size="sm"
              :disabled="deleting"
            >
              {{ deleting ? 'Удаление...' : '🗑️ Удалить' }}
            </UiButton>
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
import UiButton from '~/components/ui/UiButton.vue'

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

#### `frontend/pages/events/edit-[id].vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только главный редактор может редактировать события.</p>
      <NuxtLink to="/events" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        К афише
      </NuxtLink>
    </div>

    <template v-else>
      <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">✏️ Редактировать событие</h1>
      
      <div v-if="loading" class="text-center py-10">
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>
      
      <div v-else-if="errorMessage" class="text-center py-10 text-red-500">
        {{ errorMessage }}
      </div>
      
      <form v-else @submit.prevent="updateEvent" enctype="multipart/form-data">
        <UiInput 
          v-model="form.title"
          label="Название события"
          placeholder="Введите название события"
          required
        />
        
        <UiInput 
          v-model="form.excerpt"
          label="Краткое описание"
          placeholder="Короткое описание..."
        />
        
        <UiTextarea 
          v-model="form.content"
          label="Полное описание"
          placeholder="Подробное описание события..."
          rows="8"
          required
        />
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <UiInput 
            v-model="form.event_date"
            label="Дата и время"
            type="datetime-local"
          />
          
          <UiInput 
            v-model="form.location"
            label="Место проведения"
            placeholder="Где пройдёт событие..."
          />
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <UiInput 
            v-model="form.price"
            label="Стоимость"
            placeholder="Бесплатно / 500 ₽..."
          />
          
          <div class="mb-4">
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Изображение</label>
            
            <div v-if="form.image_url && !imageRemoved && !imagePreview" class="mb-3">
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущее изображение:</p>
              <div class="relative inline-block">
                <img 
                  :src="form.image_url" 
                  alt="Изображение" 
                  class="max-h-48 rounded-lg object-cover border border-gray-200 dark:border-gray-700"
                >
                <button 
                  @click="removeImage"
                  type="button"
                  class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 transition text-sm"
                >
                  ✕
                </button>
              </div>
            </div>
            
            <UiFileInput
              v-model="imageFile"
              label=""
              accept="image/*"
              :max-size="5 * 1024 * 1024"
              hint="Выберите новое изображение для замены"
            />
            
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 1920x1080px. Максимум 5MB.</p>
          </div>
        </div>
        
        <div class="mb-6">
          <UiCheckbox v-model="form.is_published">
            Опубликовано
          </UiCheckbox>
        </div>
        
        <div class="flex flex-wrap gap-3">
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="submitting"
          >
            {{ submitting ? 'Сохранение...' : '💾 Сохранить' }}
          </UiButton>
          
          <NuxtLink :to="`/events/${eventId}`">
            <UiButton variant="secondary">
              Отмена
            </UiButton>
          </NuxtLink>
          
          <UiButton 
            type="button"
            variant="danger"
            @click="deleteEvent"
          >
            🗑️ Удалить событие
          </UiButton>
        </div>
        
        <p v-if="submitError" class="mt-4 text-red-500 text-sm">{{ submitError }}</p>
        <p v-if="successMessage" class="mt-4 text-green-500 text-sm">{{ successMessage }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiCheckbox from '~/components/ui/UiCheckbox.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const eventId = computed(() => {
  const id = route.params.id
  if (typeof id === 'string' && id.includes('edit-')) {
    return id.replace('edit-', '')
  }
  return id
})

const loading = ref(true)
const submitting = ref(false)
const errorMessage = ref('')
const submitError = ref('')
const successMessage = ref('')

const imageFile = ref(null)
const imageRemoved = ref(false)

const form = ref({
  title: '',
  excerpt: '',
  content: '',
  event_date: '',
  location: '',
  price: '',
  image_url: '',
  is_published: false
})

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const res = await fetch(`${API_URL}/events/${eventId.value}/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const data = await res.json()
      form.value = {
        title: data.title || '',
        excerpt: data.excerpt || '',
        content: data.content || '',
        event_date: data.event_date || '',
        location: data.location || '',
        price: data.price || '',
        image_url: data.image_url || '',
        is_published: data.is_published || false
      }
      console.log('📥 Загружено событие:', form.value)
    } else {
      errorMessage.value = 'Событие не найдено'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    errorMessage.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})

const removeImage = () => {
  imageRemoved.value = true
  form.value.image_url = ''
  imageFile.value = null
  console.log('🖼️ Изображение помечено на удаление')
}

const updateEvent = async () => {
  if (!form.value.title || !form.value.content) {
    submitError.value = 'Заполните название и описание'
    return
  }
  
  submitting.value = true
  submitError.value = ''
  successMessage.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('excerpt', form.value.excerpt || '')
    formData.append('content', form.value.content)
    formData.append('event_date', form.value.event_date || '')
    formData.append('location', form.value.location || '')
    formData.append('price', form.value.price || '')
    formData.append('is_published', form.value.is_published ? 'true' : 'false')
    
    if (imageRemoved.value) {
      formData.append('image_url', '')
      console.log('🖼️ Отправляем запрос на удаление изображения')
    } else if (imageFile.value) {
      if (imageFile.value instanceof File) {
        formData.append('image', imageFile.value)
        console.log('🖼️ Новое изображение:', imageFile.value.name)
      } else if (Array.isArray(imageFile.value) && imageFile.value.length > 0) {
        const firstFile = imageFile.value[0]
        if (firstFile instanceof File) {
          formData.append('image', firstFile)
          console.log('🖼️ Новое изображение из массива:', firstFile.name)
        }
      }
    } else if (form.value.image_url) {
      formData.append('image_url', form.value.image_url)
      console.log('🖼️ Используем существующее изображение:', form.value.image_url)
    }
    
    console.log('📤 Отправка данных...')
    for (let pair of formData.entries()) {
      if (pair[1] instanceof File) {
        console.log(`  ${pair[0]}: ${pair[1].name} (${pair[1].size} байт)`)
      } else {
        console.log(`  ${pair[0]}: ${pair[1]}`)
      }
    }
    
    const res = await fetch(`${API_URL}/events/${eventId.value}/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const data = await res.json()
      console.log('✅ Событие обновлено:', data)
      successMessage.value = '✅ Событие обновлено!'
      
      form.value = {
        title: data.title,
        excerpt: data.excerpt || '',
        content: data.content,
        event_date: data.event_date || '',
        location: data.location || '',
        price: data.price || '',
        image_url: data.image_url || '',
        is_published: data.is_published
      }
      imageFile.value = null
      imageRemoved.value = false
      
      setTimeout(() => {
        router.push(`/events/${data.id}`)
      }, 1500)
    } else {
      const data = await res.json()
      console.error('❌ Ошибка:', data)
      submitError.value = data.detail || 'Ошибка обновления'
    }
  } catch (e) {
    console.error('❌ Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const deleteEvent = async () => {
  if (!confirm(`Вы уверены, что хотите удалить событие "${form.value.title}"?`)) return
  
  try {
    const res = await fetch(`${API_URL}/events/${eventId.value}/`, {
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
  }
}
</script>
```

---

#### `frontend/pages/gallery/index.vue`

```vue
<template>
  <div class="container mx-auto p-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">📸 Фотоальбомы</h1>
    </div>
    
    <div v-if="loading" class="text-center py-20">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <div v-else-if="albums.length === 0" class="text-center py-20 bg-white dark:bg-gray-800 rounded-lg shadow">
      <p class="text-gray-500 dark:text-gray-400">Пока нет альбомов</p>
    </div>
    
    <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <NuxtLink 
        v-for="album in albums" 
        :key="album.id" 
        :to="`/gallery/${album.id}`" 
        class="group"
      >
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-xl transition overflow-hidden">
          <div class="relative aspect-square overflow-hidden bg-gray-200 dark:bg-gray-700">
            <img 
              v-if="album.cover_image_url" 
              :src="album.cover_image_url" 
              :alt="album.title"
              class="w-full h-full object-cover group-hover:scale-105 transition duration-300"
            />
            <div v-else class="w-full h-full flex items-center justify-center text-4xl text-gray-400 dark:text-gray-500">
              📸
            </div>
            
            <div class="absolute bottom-2 right-2 bg-black bg-opacity-60 text-white text-xs px-2 py-1 rounded-full">
              {{ album.photos_count || 0 }} фото
            </div>
          </div>
          
          <div class="p-4">
            <h2 class="text-lg font-semibold text-gray-800 dark:text-gray-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">
              {{ album.title }}
            </h2>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-1 line-clamp-2">
              {{ album.description }}
            </p>
            <p class="text-xs text-gray-400 dark:text-gray-500 mt-2">
              📅 {{ formatDate(album.date) }}
            </p>
            <p v-if="!album.is_published && authStore.isEditor" class="text-xs text-yellow-600 dark:text-yellow-400 mt-1">
              ⚠️ Черновик
            </p>
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
const albums = ref([])
const loading = ref(true)

const formatDate = (dateString) => {
  if (!dateString) return ''
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
    const res = await fetch(`${API_URL}/albums/`, { headers })
    if (res.ok) {
      albums.value = await res.json()
    }
  } catch (e) {
    console.error('Ошибка загрузки альбомов:', e)
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

#### `frontend/pages/gallery/create.vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только редакторы могут создавать альбомы.</p>
      <NuxtLink to="/gallery" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        К альбомам
      </NuxtLink>
    </div>

    <template v-else>
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">📸 Создать альбом</h1>
        <NuxtLink to="/gallery" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition">
          ← К альбомам
        </NuxtLink>
      </div>
      
      <form @submit.prevent="createAlbum" enctype="multipart/form-data">
        <UiInput 
          v-model="form.title"
          label="Название альбома"
          placeholder="Введите название альбома"
          required
        />
        
        <UiTextarea 
          v-model="form.description"
          label="Описание"
          placeholder="Расскажите о событии..."
          rows="4"
        />
        
        <UiInput 
          v-model="form.date"
          label="Дата события"
          type="date"
          required
        />
        
        <UiFileInput
          v-model="coverFile"
          label="Обложка альбома"
          accept="image/*"
          :max-size="5 * 1024 * 1024"
          hint="Рекомендуемый размер: 800x800px. Максимум 5MB."
        />
        
        <UiFileInput
          v-model="photoFiles"
          label="Фотографии"
          multiple
          accept="image/*"
          :max-size="10 * 1024 * 1024"
          hint="Выберите несколько фотографий для альбома. Максимум 10MB на файл."
        />
        
        <div class="mb-6">
          <UiCheckbox v-model="form.is_published">
            Опубликовать сразу
          </UiCheckbox>
        </div>
        
        <div class="flex flex-wrap gap-3">
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="submitting"
          >
            {{ submitting ? 'Создание...' : '📸 Создать альбом' }}
          </UiButton>
          
          <NuxtLink to="/gallery">
            <UiButton variant="secondary">
              Отмена
            </UiButton>
          </NuxtLink>
        </div>
        
        <p v-if="error" class="mt-4 text-red-500 text-sm">{{ error }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiCheckbox from '~/components/ui/UiCheckbox.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const authStore = useAuthStore()
const router = useRouter()

const submitting = ref(false)
const error = ref('')

const form = ref({
  title: '',
  description: '',
  date: new Date().toISOString().split('T')[0],
  is_published: true
})

const coverFile = ref(null)
const photoFiles = ref([])

const createAlbum = async () => {
  if (!form.value.title) {
    error.value = 'Заполните название альбома'
    return
  }
  
  if (!form.value.date) {
    error.value = 'Укажите дату события'
    return
  }
  
  submitting.value = true
  error.value = ''
  
  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('description', form.value.description || '')
    formData.append('date', form.value.date)
    formData.append('is_published', form.value.is_published ? 'true' : 'false')
    
    if (coverFile.value) {
      if (coverFile.value instanceof File) {
        formData.append('cover_image', coverFile.value)
        console.log('🖼️ Добавлена обложка:', coverFile.value.name)
      } else if (Array.isArray(coverFile.value) && coverFile.value.length > 0) {
        const firstFile = coverFile.value[0]
        if (firstFile instanceof File) {
          formData.append('cover_image', firstFile)
          console.log('🖼️ Добавлена обложка из массива:', firstFile.name)
        }
      }
    }
    
    const res = await fetch(`${API_URL}/albums/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (!res.ok) {
      const data = await res.json()
      console.error('Ошибка создания альбома:', data)
      error.value = data.detail || JSON.stringify(data)
      submitting.value = false
      return
    }
    
    const album = await res.json()
    console.log('✅ Альбом создан:', album)
    
    if (photoFiles.value && photoFiles.value.length > 0) {
      const uploadFormData = new FormData()
      let hasFiles = false
      
      for (let i = 0; i < photoFiles.value.length; i++) {
        const file = photoFiles.value[i]
        if (file instanceof File) {
          uploadFormData.append('photos', file)
          console.log('📷 Добавлено фото:', file.name)
          hasFiles = true
        }
      }
      
      if (hasFiles) {
        console.log('📤 Отправка фотографий...')
        const uploadRes = await fetch(`${API_URL}/albums/${album.id}/upload-photos/`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${authStore.accessToken}`
          },
          body: uploadFormData
        })
        
        if (uploadRes.ok) {
          const result = await uploadRes.json()
          console.log('✅ Фотографии загружены:', result)
        } else {
          const err = await uploadRes.json()
          console.error('❌ Ошибка загрузки фото:', err)
        }
      }
    }
    
    router.push(`/gallery/${album.id}`)
    
  } catch (e) {
    console.error('❌ Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}
</script>
```

---

#### `frontend/pages/gallery/[id].vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-6xl">
    <div class="flex justify-between items-center mb-4">
      <NuxtLink to="/gallery" class="text-blue-500 dark:text-blue-400 hover:underline">
        ← Назад к альбомам
      </NuxtLink>
      
      <div v-if="authStore.isEditor && album" class="flex gap-2">
        <NuxtLink 
          :to="`/gallery/edit-${album.id}`" 
          class="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition text-sm"
        >
          ✏️ Редактировать
        </NuxtLink>
        <button 
          @click="deleteAlbum" 
          class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition text-sm"
          :disabled="deleting"
        >
          {{ deleting ? 'Удаление...' : '🗑️ Удалить' }}
        </button>
      </div>
    </div>
    
    <div v-if="loading" class="text-center py-20">
      <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
    </div>
    
    <template v-else-if="album">
      <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-8">
        <h1 class="text-3xl font-bold text-gray-800 dark:text-gray-200">{{ album.title }}</h1>
        <p class="text-gray-600 dark:text-gray-400 mt-2">{{ album.description }}</p>
        <div class="flex flex-wrap gap-4 mt-3 text-sm text-gray-500 dark:text-gray-400">
          <span>📅 {{ formatDate(album.date) }}</span>
          <span>📸 {{ album.photos_count || 0 }} фотографий</span>
          <span v-if="!album.is_published" class="text-yellow-600 dark:text-yellow-400">
            ⚠️ Черновик
          </span>
        </div>
      </div>
      
      <div v-if="album.photos && album.photos.length > 0" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
        <div 
          v-for="(photo, index) in album.photos" 
          :key="photo.id"
          class="relative aspect-square bg-gray-200 dark:bg-gray-700 rounded-lg overflow-hidden cursor-pointer group"
          @click="openLightbox(index)"
        >
          <img 
            :src="photo.thumbnail_url || photo.image_url" 
            :alt="photo.caption || 'Фотография'"
            class="w-full h-full object-cover group-hover:scale-105 transition duration-300"
            loading="lazy"
          />
          
          <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-2 opacity-0 group-hover:opacity-100 transition">
            <div class="flex items-center gap-3 text-white text-xs">
              <span>👁️ {{ photo.views || 0 }}</span>
              <span>❤️ {{ photo.likes_count || 0 }}</span>
              <span>💬 {{ photo.comments_count || 0 }}</span>
            </div>
          </div>
          
          <button 
            v-if="authStore.isEditor"
            @click.stop="deletePhoto(photo.id)"
            class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600 transition opacity-0 group-hover:opacity-100"
            title="Удалить фото"
          >
            ✕
          </button>
          
          <div v-if="photo.caption" class="absolute bottom-0 left-0 right-0 bg-black bg-opacity-60 text-white text-xs p-2 truncate">
            {{ photo.caption }}
          </div>
        </div>
      </div>
      
      <div v-else class="text-center py-20 bg-white dark:bg-gray-800 rounded-lg shadow">
        <p class="text-gray-500 dark:text-gray-400">В этом альбоме пока нет фотографий</p>
        
        <div v-if="authStore.isEditor" class="mt-4">
          <button 
            @click="triggerFileUpload"
            class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
          >
            📤 Загрузить фотографии
          </button>
          <input 
            ref="fileInput"
            type="file" 
            accept="image/*"
            multiple
            class="hidden"
            @change="uploadPhotos"
          />
        </div>
      </div>
      
      <div v-if="authStore.isEditor && album.photos && album.photos.length > 0" class="mt-6 text-center">
        <button 
          @click="triggerFileUpload"
          class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
        >
          📤 Добавить фотографии
        </button>
        <input 
          ref="fileInput"
          type="file" 
          accept="image/*"
          multiple
          class="hidden"
          @change="uploadPhotos"
        />
      </div>
    </template>
    
    <div v-else class="text-center py-20 text-red-500">
      Альбом не найден
    </div>
    
    <Lightbox 
      v-if="album && album.photos"
      :photos="album.photos"
      :album-id="album.id"
      :initial-index="lightboxIndex"
      :is-open="lightboxOpen"
      @close="closeLightbox"
      @photo-updated="onPhotoUpdated"
    />
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import Lightbox from '~/components/Lightbox.vue'

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const album = ref(null)
const loading = ref(true)
const deleting = ref(false)
const lightboxOpen = ref(false)
const lightboxIndex = ref(0)
const fileInput = ref(null)

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const loadAlbum = async () => {
  try {
    const id = route.params.id
    const headers = {}
    if (authStore.isAuthenticated) {
      headers['Authorization'] = `Bearer ${authStore.accessToken}`
    }
    
    const res = await fetch(`${API_URL}/albums/${id}/`, { headers })
    if (res.ok) {
      album.value = await res.json()
    } else {
      router.push('/gallery')
    }
  } catch (e) {
    console.error('Ошибка загрузки альбома:', e)
  } finally {
    loading.value = false
  }
}

const openLightbox = (index) => {
  lightboxIndex.value = index
  lightboxOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeLightbox = () => {
  lightboxOpen.value = false
  document.body.style.overflow = ''
}

const onPhotoUpdated = (updatedPhoto) => {
  const photoIndex = album.value.photos.findIndex(p => p.id === updatedPhoto.id)
  if (photoIndex !== -1) {
    album.value.photos[photoIndex] = updatedPhoto
  }
}

const triggerFileUpload = () => {
  if (fileInput.value) {
    fileInput.value.click()
  }
}

const uploadPhotos = async (event) => {
  const files = event.target.files
  if (!files || files.length === 0) return
  
  const formData = new FormData()
  for (let i = 0; i < files.length; i++) {
    formData.append('photos', files[i])
  }
  
  try {
    const res = await fetch(`${API_URL}/albums/${album.value.id}/upload-photos/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const data = await res.json()
      if (data.photos) {
        if (!album.value.photos) {
          album.value.photos = []
        }
        album.value.photos = [...album.value.photos, ...data.photos]
        album.value.photos_count = album.value.photos.length
      }
      if (fileInput.value) {
        fileInput.value.value = ''
      }
    } else {
      const error = await res.json()
      console.error('Ошибка загрузки:', error)
      alert('Ошибка при загрузке фотографий')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

const deletePhoto = async (photoId) => {
  if (!confirm('Удалить эту фотографию?')) return
  
  try {
    const res = await fetch(`${API_URL}/albums/${album.value.id}/photos/${photoId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      album.value.photos = album.value.photos.filter(p => p.id !== photoId)
      album.value.photos_count = album.value.photos.length
    } else {
      alert('Ошибка при удалении фотографии')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}

const deleteAlbum = async () => {
  if (!album.value) return
  if (!confirm(`Вы уверены, что хотите удалить альбом "${album.value.title}"?`)) return
  
  deleting.value = true
  
  try {
    const res = await fetch(`${API_URL}/albums/${album.value.id}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      router.push('/gallery')
    } else {
      alert('Ошибка при удалении альбома')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    deleting.value = false
  }
}

onMounted(async () => {
  authStore.restoreAuth()
  await loadAlbum()
})
</script>
```

---

#### `frontend/pages/gallery/edit-[id].vue`

```vue
<template>
  <div class="max-w-3xl mx-auto mt-10 bg-white dark:bg-gray-800 p-8 rounded-lg shadow transition-colors duration-200">
    <div v-if="!authStore.isEditor" class="text-center py-10">
      <div class="text-red-500 text-6xl mb-4">⛔</div>
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-2">Доступ запрещён</h2>
      <p class="text-gray-600 dark:text-gray-400">Только редакторы могут редактировать альбомы.</p>
      <NuxtLink to="/gallery" class="mt-4 inline-block bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition">
        К альбомам
      </NuxtLink>
    </div>

    <template v-else>
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">✏️ Редактировать альбом</h1>
        <NuxtLink :to="`/gallery/${albumId}`" class="text-blue-500 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition">
          ← Назад к альбому
        </NuxtLink>
      </div>
      
      <div v-if="loading" class="text-center py-10">
        <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
      </div>
      
      <div v-else-if="error" class="text-center py-10 text-red-500">
        {{ error }}
      </div>
      
      <form v-else @submit.prevent="updateAlbum" enctype="multipart/form-data">
        <UiInput 
          v-model="form.title"
          label="Название альбома"
          placeholder="Введите название альбома"
          required
        />
        
        <UiTextarea 
          v-model="form.description"
          label="Описание"
          placeholder="Расскажите о событии..."
          rows="4"
        />
        
        <UiInput 
          v-model="form.date"
          label="Дата события"
          type="date"
          required
        />
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Обложка альбома</label>
          
          <div v-if="form.cover_image_url && !coverRemoved && !coverPreview" class="mb-3">
            <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Текущая обложка:</p>
            <div class="relative inline-block">
              <img 
                :src="form.cover_image_url" 
                alt="Обложка" 
                class="max-h-48 rounded-lg object-cover border border-gray-200 dark:border-gray-700"
              >
              <button 
                @click="removeCover"
                type="button"
                class="absolute top-2 right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center hover:bg-red-600 transition text-sm"
              >
                ✕
              </button>
            </div>
          </div>
          
          <UiFileInput
            v-model="coverFile"
            label=""
            accept="image/*"
            :max-size="5 * 1024 * 1024"
            hint="Выберите новую обложку для замены"
          />
          
          <p class="text-xs text-gray-400 dark:text-gray-500 mt-1">Рекомендуемый размер: 800x800px. Максимум 5MB.</p>
        </div>
        
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Фотографии в альбоме</label>
          
          <div v-if="albumPhotos.length > 0" class="mb-3">
            <p class="text-sm text-gray-500 dark:text-gray-400 mb-2">Всего фотографий: {{ albumPhotos.length }}</p>
            <div class="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-6 gap-2">
              <div 
                v-for="photo in albumPhotos" 
                :key="photo.id"
                class="relative group"
              >
                <img 
                  :src="photo.image_url" 
                  :alt="photo.caption || 'Фото'"
                  class="w-20 h-20 object-cover rounded-lg border border-gray-200 dark:border-gray-600"
                />
                <button
                  type="button"
                  class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100"
                  @click="deletePhoto(photo.id)"
                  :disabled="deletingPhoto === photo.id"
                >
                  {{ deletingPhoto === photo.id ? '...' : '✕' }}
                </button>
                <p class="text-xs text-gray-500 dark:text-gray-400 mt-1 truncate max-w-[80px] text-center">
                  {{ photo.caption || 'Фото' }}
                </p>
              </div>
            </div>
          </div>
          <div v-else class="text-gray-500 dark:text-gray-400 text-sm py-2">
            В этом альбоме пока нет фотографий
          </div>
          
          <div class="mt-3">
            <label class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">Добавить фотографии</label>
            <UiFileInput
              v-model="newPhotos"
              label=""
              multiple
              accept="image/*"
              :max-size="10 * 1024 * 1024"
              hint="Выберите несколько фотографий для добавления. Максимум 10MB на файл."
            />
          </div>
        </div>
        
        <div class="mb-6">
          <UiCheckbox v-model="form.is_published">
            Опубликован
          </UiCheckbox>
        </div>
        
        <div class="flex flex-wrap gap-3">
          <UiButton 
            type="submit" 
            variant="primary"
            :disabled="submitting"
          >
            {{ submitting ? 'Сохранение...' : '💾 Сохранить' }}
          </UiButton>
          
          <NuxtLink :to="`/gallery/${albumId}`">
            <UiButton variant="secondary">
              Отмена
            </UiButton>
          </NuxtLink>
          
          <UiButton 
            type="button"
            variant="danger"
            @click="deleteAlbum"
          >
            🗑️ Удалить альбом
          </UiButton>
        </div>
        
        <p v-if="submitError" class="mt-4 text-red-500 text-sm">{{ submitError }}</p>
        <p v-if="success" class="mt-4 text-green-500 text-sm">{{ success }}</p>
      </form>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'
import UiTextarea from '~/components/ui/UiTextarea.vue'
import UiCheckbox from '~/components/ui/UiCheckbox.vue'
import UiFileInput from '~/components/ui/UiFileInput.vue'

definePageMeta({
  middleware: 'auth'
})

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'

const route = useRoute()
const authStore = useAuthStore()
const router = useRouter()

const albumId = computed(() => {
  const id = route.params.id
  if (typeof id === 'string' && id.includes('edit-')) {
    return id.replace('edit-', '')
  }
  return id
})

const loading = ref(true)
const submitting = ref(false)
const error = ref('')
const submitError = ref('')
const success = ref('')

const coverFile = ref(null)
const coverRemoved = ref(false)
const albumPhotos = ref([])
const newPhotos = ref([])
const deletingPhoto = ref(null)

const form = ref({
  title: '',
  description: '',
  date: '',
  cover_image_url: '',
  is_published: true
})

const originalForm = ref({})

onMounted(async () => {
  authStore.restoreAuth()
  
  try {
    const id = albumId.value
    const res = await fetch(`${API_URL}/albums/${id}/`, {
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      const album = await res.json()
      form.value = {
        title: album.title,
        description: album.description || '',
        date: album.date || '',
        cover_image_url: album.cover_image_url || '',
        is_published: album.is_published
      }
      originalForm.value = { ...form.value }
      albumPhotos.value = album.photos || []
    } else {
      error.value = 'Альбом не найден'
    }
  } catch (e) {
    console.error('Ошибка:', e)
    error.value = 'Ошибка подключения к серверу'
  } finally {
    loading.value = false
  }
})

const removeCover = () => {
  coverRemoved.value = true
  form.value.cover_image_url = ''
  coverFile.value = null
}

const deletePhoto = async (photoId) => {
  if (!confirm('Удалить эту фотографию?')) return
  
  deletingPhoto.value = photoId
  
  try {
    const res = await fetch(`${API_URL}/albums/${albumId.value}/photos/${photoId}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      albumPhotos.value = albumPhotos.value.filter(p => p.id !== photoId)
      console.log('✅ Фотография удалена')
    } else {
      const err = await res.json()
      console.error('Ошибка удаления фото:', err)
      alert('Ошибка при удалении фотографии')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  } finally {
    deletingPhoto.value = null
  }
}

const uploadNewPhotos = async () => {
  if (!newPhotos.value || newPhotos.value.length === 0) return true
  
  const uploadFormData = new FormData()
  let hasFiles = false
  
  for (let i = 0; i < newPhotos.value.length; i++) {
    const file = newPhotos.value[i]
    if (file instanceof File) {
      uploadFormData.append('photos', file)
      console.log('📷 Добавлено фото:', file.name)
      hasFiles = true
    }
  }
  
  if (!hasFiles) return true
  
  try {
    const res = await fetch(`${API_URL}/albums/${albumId.value}/upload-photos/`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: uploadFormData
    })
    
    if (res.ok) {
      const result = await res.json()
      console.log('✅ Новые фотографии загружены:', result)
      if (result.photos) {
        albumPhotos.value = [...albumPhotos.value, ...result.photos]
      }
      return true
    } else {
      const err = await res.json()
      console.error('❌ Ошибка загрузки фото:', err)
      alert('Ошибка при загрузке фотографий')
      return false
    }
  } catch (e) {
    console.error('❌ Ошибка:', e)
    alert('Ошибка подключения к серверу')
    return false
  }
}

const updateAlbum = async () => {
  if (!form.value.title) {
    submitError.value = 'Заполните название альбома'
    return
  }
  
  if (!form.value.date) {
    submitError.value = 'Укажите дату события'
    return
  }
  
  submitting.value = true
  submitError.value = ''
  success.value = ''
  
  try {
    const photosUploaded = await uploadNewPhotos()
    if (!photosUploaded) {
      submitting.value = false
      return
    }
    
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('description', form.value.description || '')
    formData.append('date', form.value.date)
    formData.append('is_published', form.value.is_published ? 'true' : 'false')
    
    if (coverRemoved.value) {
      formData.append('cover_image', '')
      console.log('🖼️ Обложка удалена')
    } else if (coverFile.value) {
      if (coverFile.value instanceof File) {
        formData.append('cover_image', coverFile.value)
        console.log('🖼️ Новая обложка:', coverFile.value.name)
      } else if (Array.isArray(coverFile.value) && coverFile.value.length > 0) {
        const firstFile = coverFile.value[0]
        if (firstFile instanceof File) {
          formData.append('cover_image', firstFile)
          console.log('🖼️ Новая обложка из массива:', firstFile.name)
        }
      }
    }
    
    const res = await fetch(`${API_URL}/albums/${albumId.value}/`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      },
      body: formData
    })
    
    if (res.ok) {
      const album = await res.json()
      success.value = '✅ Альбом обновлён!'
      
      form.value = {
        title: album.title,
        description: album.description || '',
        date: album.date || '',
        cover_image_url: album.cover_image_url || '',
        is_published: album.is_published
      }
      originalForm.value = { ...form.value }
      coverFile.value = null
      coverRemoved.value = false
      newPhotos.value = []
      
      setTimeout(() => {
        router.push(`/gallery/${album.id}`)
      }, 1500)
    } else {
      const data = await res.json()
      submitError.value = data.detail || 'Ошибка обновления'
      console.error('Ошибка:', data)
    }
  } catch (e) {
    console.error('Ошибка:', e)
    submitError.value = 'Ошибка подключения к серверу'
  } finally {
    submitting.value = false
  }
}

const deleteAlbum = async () => {
  if (!confirm(`Вы уверены, что хотите удалить альбом "${form.value.title}"?`)) return
  
  try {
    const res = await fetch(`${API_URL}/albums/${albumId.value}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.accessToken}`
      }
    })
    
    if (res.ok) {
      router.push('/gallery')
    } else {
      alert('Ошибка при удалении альбома')
    }
  } catch (e) {
    console.error('Ошибка:', e)
    alert('Ошибка подключения к серверу')
  }
}
</script>
```

---

#### `frontend/pages/authors/index.vue`

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

#### `frontend/pages/authors/[id].vue`

```vue
<template>
  <div class="container mx-auto p-4 max-w-4xl">
    <NuxtLink to="/" class="text-blue-500 dark:text-blue-400 hover:underline mb-4 inline-block">
      ← На главную
    </NuxtLink>

    <div v-if="author" class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg mb-8 transition-colors duration-200">
      <div class="flex items-center gap-6">
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
        <div v-if="post.display_image" class="h-24 w-24 rounded-lg overflow-hidden flex-shrink-0">
          <img :src="post.display_image" :alt="post.title" class="w-full h-full object-cover">
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

#### `frontend/pages/reset-password/[uidb64]/[token].vue`

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
        <UiInput 
          v-model="newPassword"
          label="Новый пароль"
          type="password"
          required
          hint="Минимум 8 символов"
        />
        
        <UiInput 
          v-model="newPassword2"
          label="Подтвердите пароль"
          type="password"
          required
        />
        
        <UiButton 
          type="submit"
          variant="primary"
          :disabled="submitting"
          full-width
        >
          {{ submitting ? 'Сохранение...' : 'Сохранить новый пароль' }}
        </UiButton>
        
        <p v-if="formError" class="mt-3 text-red-500 text-sm">{{ formError }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import UiButton from '~/components/ui/UiButton.vue'
import UiInput from '~/components/ui/UiInput.vue'

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

## УСТАНОВКА И ЗАПУСК

### Бэкенд:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Фронтенд:

```bash
cd frontend
npm install
npm run dev
```

---

## ЗАКЛЮЧЕНИЕ

Проект "Центр Культуры" — полнофункциональная платформа для публикации культурного контента с системой ролей, галереей, афишей, комментариями и лайками. Проект использует современный компонентный подход, где каждый элемент интерфейса вынесен в отдельный переиспользуемый компонент. Проект готов к использованию и может быть развёрнут как локально, так и на продакшн-сервере.