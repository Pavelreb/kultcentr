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
- **GSAP** — анимации (опционально)

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
- Изображения (файл или ссылка) с превью
- Черновики
- Лайки с анимацией
- Комментарии (вложенные)
- Просмотры
- Автоудаление файлов
- Создание через единое меню "Создать" в шапке
- Главный пост на странице всех публикаций
- Пагинация на странице всех публикаций (9 постов на страницу)
- Полное имя автора (Имя + Фамилия)
- Хлебные крошки

### 🎭 Афиша (События)
- CRUD (только редакторы)
- Изображения (файл или ссылка) с превью
- Черновики
- Сортировка по дате (ближайшие первыми)
- Автоудаление файлов
- Создание через единое меню "Создать" в шапке
- Главное событие на странице афиши
- Пагинация на главной странице (5 событий на страницу)
- Хлебные крошки
- Детальная страница с полной информацией

### 📸 Галерея
- Альбомы с названием, описанием и датой события
- Фотографии в альбомах
- Обложка альбома (файл или ссылка)
- Просмотры фотографий
- Лайки фотографий
- Комментарии к фотографиям (вложенные)
- Lightbox с навигацией, лайками и комментариями
- Автоудаление файлов
- Создание через единое меню "Создать" в шапке
- Пагинация на странице галереи (15 альбомов на страницу)
- Карточки альбомов с информацией поверх изображения
- Хлебные крошки

### 💬 Комментарии
- **К постам**: `/api/comments/` с полем `post`
- **К фото**: `/api/photo-comments/` с полем `photo`
- Создание (только авторизованные)
- Редактирование (только свои)
- Удаление (свои, автор поста, редактор)
- Вложенность
- Лайки
- Аватарки авторов
- Отображение полного имени (Имя + Фамилия)

### ❤️ Лайки
- На посты, комментарии и фотографии
- Только авторизованные
- Анимация при нажатии на лайк

### 👤 Профиль
- Страница просмотра `/profile`
- Страница редактирования `/profile/edit`
- ФИО, дата рождения, аватарка
- Смена пароля
- Мои посты, Мои афиши, Мои комментарии (к постам и галерее)
- Современные SVG-иконки

### 📞 Контакты
- Страница `/contacts` (доступна всем)
- Редактирование в настройках `/settings` (только редакторы)
- Данные в футере (автообновление)
- Современные SVG-иконки

### 🎨 Баннер
- Управление Hero-баннером на главной
- Заголовок и подзаголовок
- Фоновое изображение (файл или ссылка) с превью
- Кнопка с текстом и ссылкой
- Включение/отключение кнопки
- Активность баннера
- Редактирование только для редакторов
- Сброс к дефолтным значениям

### ✍️ Авторы
- Блок на главной
- Страница всех авторов
- Страница автора с публикациями
- Карточки с аватаркой, именем, ролью, статистикой

### 🎨 Дизайн
- Адаптив (мобильные, планшеты, десктоп)
- Тёмная тема (переключение)
- Hero-баннер
- Семантические теги (header, main, footer)
- Компонентный подход
- Единое меню "Создать" в шапке
- Современные SVG-иконки вместо эмодзи
- Хлебные крошки на всех страницах
- Современные кнопки с градиентами и тенями

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
│   │   │   ├── CreateMenu.vue
│   │   │   └── Breadcrumbs.vue
│   │   ├── ui/                      # UI-компоненты
│   │   │   ├── UiButton.vue
│   │   │   ├── UiInput.vue
│   │   │   ├── UiTextarea.vue
│   │   │   ├── UiCheckbox.vue
│   │   │   ├── UiCard.vue
│   │   │   ├── UiFileInput.vue
│   │   │   ├── SkeletonCard.vue
│   │   │   └── Pagination.vue
│   │   ├── features/                # Компоненты функций
│   │   │   ├── banner/
│   │   │   │   └── HeroBanner.vue
│   │   │   ├── events/
│   │   │   │   ├── EventCard.vue
│   │   │   │   ├── EventSection.vue
│   │   │   │   ├── EventDetail.vue
│   │   │   │   ├── FeaturedEvent.vue
│   │   │   │   ├── EventList.vue
│   │   │   │   └── EventListItem.vue
│   │   │   ├── posts/
│   │   │   │   ├── PostCard.vue
│   │   │   │   ├── PostSection.vue
│   │   │   │   ├── PostDetail.vue
│   │   │   │   ├── FeaturedPost.vue
│   │   │   │   ├── PostComments.vue
│   │   │   │   ├── PostList.vue
│   │   │   │   └── PostListItem.vue
│   │   │   ├── albums/
│   │   │   │   ├── AlbumCard.vue
│   │   │   │   ├── AlbumSection.vue
│   │   │   │   ├── AlbumSkeleton.vue
│   │   │   │   ├── AlbumGrid.vue
│   │   │   │   ├── GalleryAlbumCard.vue
│   │   │   │   └── AlbumDetail.vue
│   │   │   └── authors/
│   │   │       ├── AuthorCard.vue
│   │   │       └── AuthorSection.vue
│   │   ├── CommentItem.vue
│   │   └── Lightbox.vue
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
from posts.models import Post

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
    posts_count = serializers.SerializerMethodField()
    subscribers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'patronymic', 'birth_date', 'bio', 'date_joined', 
            'role', 'role_display', 'full_name', 'is_active',
            'avatar', 'avatar_url', 'posts_count', 'subscribers_count'
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

    def get_posts_count(self, obj):
        return Post.objects.filter(author=obj, is_published=True).count()

    def get_subscribers_count(self, obj):
        return 0


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
        write-only=True
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
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_role = serializers.CharField(source='author.role', read_only=True)
    author_avatar = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user_has_liked = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'image', 'image_url', 'display_image',
            'author_name', 'author_first_name', 'author_last_name', 'author_full_name',
            'author_role', 'author_avatar', 'created_at', 'updated_at',
            'is_published', 'excerpt', 'comments', 'likes_count',
            'user_has_liked', 'views'
        ]
        read_only_fields = ['author', 'author_name', 'author_first_name', 'author_last_name', 
                           'author_full_name', 'author_role', 'author_avatar', 
                           'created_at', 'updated_at', 'views']

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

    def get_author_full_name(self, obj):
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        if obj.author.patronymic:
            parts.append(obj.author.patronymic)
        return ' '.join(parts) if parts else obj.author.username

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
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'author_name', 'author_first_name', 'author_last_name',
            'author_full_name', 'author_avatar', 'content', 'created_at',
            'updated_at', 'parent', 'replies', 'can_edit', 'can_delete',
            'likes_count', 'user_has_liked'
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

    def get_author_full_name(self, obj):
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        return ' '.join(parts) if parts else obj.author.username


class CommentForPostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_full_name = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()
    can_edit = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'author_name', 'author_first_name', 'author_last_name',
            'author_full_name', 'author_avatar', 'content', 'created_at',
            'updated_at', 'parent', 'replies', 'can_edit', 'can_delete',
            'likes_count', 'user_has_liked'
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

    def get_author_full_name(self, obj):
        parts = []
        if obj.author.last_name:
            parts.append(obj.author.last_name)
        if obj.author.first_name:
            parts.append(obj.author.first_name)
        return ' '.join(parts) if parts else obj.author.username
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
            'id', 'title', 'content', 'author_name', 'author_role',
            'event_date', 'location', 'price', 'image', 'image_url',
            'display_image', 'created_at', 'updated_at', 'is_published', 'excerpt'
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
            "id", "address", "phone", "email", "work_hours",
            "description", "instagram", "vk", "telegram", "updated_at"
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
            'id', 'title', 'subtitle', 'background_image',
            'background_image_url', 'background_image_url_display',
            'has_background', 'button_text', 'button_link',
            'button_enabled', 'is_active', 'updated_at'
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
        verbose_name='Обложка альбома (файл)'
    )
    cover_image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Обложка альбома (ссылка)'
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
    
    def get_cover_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        return self.cover_image_url
    
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
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Не авторизован'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        comments = PhotoComment.objects.filter(user=request.user).order_by('-created_at')
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
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
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
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
        ('Обложка', {
            'fields': ('cover_image', 'cover_image_url')
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
        fullName: (state) => {
            if (!state.user) return ''
            const parts = []
            if (state.user.last_name) parts.push(state.user.last_name)
            if (state.user.first_name) parts.push(state.user.first_name)
            if (state.user.patronymic) parts.push(state.user.patronymic)
            return parts.length > 0 ? parts.join(' ') : state.user.username
        },
        initials: (state) => {
            if (!state.user) return '?'
            const name = state.user.full_name || state.user.username
            const parts = name.split(' ')
            if (parts.length >= 2) {
                return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
            }
            return name.substring(0, 2).toUpperCase()
        }
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
  <header class="bg-white dark:bg-gray-800 shadow transition-colors duration-200 sticky top-0 z-50 border-b border-gray-200 dark:border-gray-700">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
      <div class="flex items-center gap-2">
        <AppLogo />
        <BurgerMenu />
      </div>
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
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
            </svg>
            Центр Культуры
          </h3>
          <p class="text-sm text-gray-400 leading-relaxed whitespace-pre-wrap">
            {{ contacts.description }}
          </p>
        </div>
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
            Контакты
          </h3>
          <ul class="space-y-2 text-sm">
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
              <span>{{ contacts.address }}</span>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              <a :href="`tel:${contacts.phone}`" class="text-gray-300 hover:text-blue-400 transition">
                {{ contacts.phone }}
              </a>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              <a :href="`mailto:${contacts.email}`" class="text-gray-300 hover:text-blue-400 transition">
                {{ contacts.email }}
              </a>
            </li>
            <li class="flex items-center gap-2 text-gray-300">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span>{{ contacts.work_hours }}</span>
            </li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
            Разделы
          </h3>
          <ul class="space-y-2 text-sm">
            <li>
              <NuxtLink to="/events" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
                </svg>
                Афиша
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/posts" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
                </svg>
                Публикации
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/gallery" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
                Галерея
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/authors" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
                </svg>
                Авторы
              </NuxtLink>
            </li>
            <li>
              <NuxtLink to="/contacts" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition">
                <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                </svg>
                Контакты
              </NuxtLink>
            </li>
            <li v-if="authStore.isEditor">
              <NuxtLink to="/settings" class="flex items-center gap-2 text-yellow-400 hover:text-yellow-300 transition">
                <svg class="w-4 h-4 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
                Настройки
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
.app-footer, .app-footer * { color: #d1d5db !important; }
.app-footer h3 { color: #ffffff !important; }
.app-footer a { color: #d1d5db !important; }
.app-footer a:hover { color: #60a5fa !important; }
:where(.dark) .app-footer { background-color: #111827 !important; }
:where(.dark) .app-footer, :where(.dark) .app-footer * { color: #d1d5db !important; }
:where(.dark) .app-footer h3 { color: #ffffff !important; }
:where(.dark) .app-footer a { color: #d1d5db !important; }
:where(.dark) .app-footer a:hover { color: #60a5fa !important; }
</style>
```

---

#### `frontend/components/layout/AppLogo.vue`

```vue
<template>
  <NuxtLink to="/" class="flex items-center gap-2 text-xl font-bold text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
    <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
    </svg>
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
    <button @click="toggleMenu" class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition text-gray-600 dark:text-gray-300 focus:outline-none" aria-label="Меню">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </button>
    <div v-if="isMenuOpen" class="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50" @click.stop>
      <div v-if="authStore.isAuthenticated" class="px-4 py-3 border-b border-gray-100 dark:border-gray-700">
        <div class="flex items-center gap-3">
          <img v-if="authStore.user?.avatar_url" :src="authStore.user?.avatar_url" :alt="displayName" class="w-10 h-10 rounded-full object-cover">
          <div v-else class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-sm font-bold">
            {{ authStore.initials }}
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-semibold text-gray-800 dark:text-gray-200 truncate">{{ displayName }}</p>
            <p class="text-xs text-gray-500 dark:text-gray-400 truncate">{{ authStore.user?.role_display || 'Пользователь' }}</p>
          </div>
        </div>
      </div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Навигация</div>
      <NuxtLink to="/" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
        </svg>
        Главная
      </NuxtLink>
      <NuxtLink to="/events" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
        </svg>
        Афиша
      </NuxtLink>
      <NuxtLink to="/posts" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        Публикации
      </NuxtLink>
      <NuxtLink to="/gallery" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        Галерея
      </NuxtLink>
      <NuxtLink to="/authors" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
        </svg>
        Авторы
      </NuxtLink>
      <NuxtLink to="/contacts" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
        </svg>
        Контакты
      </NuxtLink>
      <div v-if="authStore.isEditor" class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div v-if="authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Управление</div>
      <NuxtLink v-if="authStore.isEditor" to="/settings" class="flex items-center gap-3 px-4 py-2.5 text-sm text-yellow-600 dark:text-yellow-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-yellow-500 dark:text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
        </svg>
        Настройки сайта
      </NuxtLink>
      <div class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Аккаунт</div>
      <template v-if="authStore.isAuthenticated">
        <NuxtLink to="/profile" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
          <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
          Мой профиль
        </NuxtLink>
        <button @click="handleLogout" class="flex items-center gap-3 px-4 py-2.5 text-sm text-red-500 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition w-full text-left">
          <svg class="w-5 h-5 text-red-400 dark:text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4 4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
          </svg>
          Выйти
        </button>
      </template>
      <template v-else>
        <NuxtLink to="/auth/login" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
          <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
          </svg>
          Войти
        </NuxtLink>
        <NuxtLink to="/auth/register" class="flex items-center gap-3 px-4 py-2.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
          <svg class="w-5 h-5 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
          </svg>
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

const displayName = computed(() => authStore.fullName || authStore.username)

const toggleMenu = () => { isMenuOpen.value = !isMenuOpen.value }
const closeMenu = () => { isMenuOpen.value = false }

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

onMounted(() => { document.addEventListener('click', handleClickOutside) })
onUnmounted(() => { document.removeEventListener('click', handleClickOutside) })
</script>
```

---

#### `frontend/components/common/ThemeToggle.vue`

```vue
<template>
  <button @click="toggleTheme" class="p-2.5 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-700 transition-all duration-300 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:shadow-md" :title="themeStore.darkMode ? 'Светлая тема' : 'Тёмная тема'" aria-label="Переключить тему">
    <svg v-if="themeStore.darkMode" class="w-5 h-5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
    </svg>
    <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>
    </svg>
  </button>
</template>

<script setup>
import { useThemeStore } from '~/store/theme'

const themeStore = useThemeStore()
const toggleTheme = () => { themeStore.toggleTheme() }
</script>
```

---

#### `frontend/components/common/AuthButtons.vue`

```vue
<template>
  <div class="flex items-center gap-3">
    <template v-if="authStore.isAuthenticated">
      <NuxtLink to="/profile" class="hidden md:flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition font-medium group">
        <img v-if="authStore.user?.avatar_url" :src="authStore.user?.avatar_url" :alt="displayName" class="w-8 h-8 rounded-full object-cover border-2 border-blue-200 dark:border-blue-800 group-hover:border-blue-400 dark:group-hover:border-blue-600 transition">
        <div v-else class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-xs font-bold">
          {{ authStore.initials }}
        </div>
        <div class="flex flex-col leading-tight">
          <span class="font-medium text-gray-700 dark:text-gray-300">{{ displayName }}</span>
          <span class="text-xs text-gray-400 dark:text-gray-500">{{ roleDisplay }}</span>
        </div>
        <svg class="w-3 h-3 text-gray-400 dark:text-gray-500 group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </NuxtLink>
    </template>
    <template v-else>
      <NuxtLink to="/auth/login">
        <button class="inline-flex items-center gap-1.5 px-4 py-2 bg-transparent border-2 border-blue-500 text-blue-600 dark:text-blue-400 rounded-xl hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:border-blue-600 dark:hover:border-blue-300 transition-all duration-300 text-sm font-medium hover:-translate-y-0.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
          </svg>
          Войти
        </button>
      </NuxtLink>
      <NuxtLink to="/auth/register">
        <button class="inline-flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 text-sm font-medium shadow-blue-500/25 hover:shadow-lg hover:shadow-blue-500/40 hover:-translate-y-0.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
          </svg>
          Регистрация
        </button>
      </NuxtLink>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()

const displayName = computed(() => authStore.fullName || authStore.username)

const roleDisplay = computed(() => {
  if (!authStore.user) return ''
  const roleMap = { 'admin': 'Администратор', 'editor': 'Главный редактор', 'author': 'Автор', 'subscriber': 'Подписчик' }
  return roleMap[authStore.user.role] || authStore.user.role_display || 'Пользователь'
})
</script>
```

---

#### `frontend/components/common/CreateMenu.vue`

```vue
<template>
  <div v-if="canCreate" class="relative" ref="menuRef">
    <button @click="toggleMenu" class="flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-violet-500 to-purple-600 text-white rounded-xl hover:from-violet-600 hover:to-purple-700 transition-all duration-300 text-sm font-medium shadow-md shadow-violet-500/25 hover:shadow-lg hover:shadow-violet-500/40 hover:-translate-y-0.5" aria-label="Создать">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
      </svg>
      <span class="hidden sm:inline">Создать</span>
      <svg class="w-4 h-4 transition-transform duration-300 ml-1" :class="isMenuOpen ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>
    <div v-if="isMenuOpen" class="absolute right-0 top-full mt-2 w-56 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50" @click.stop>
      <div v-if="authStore.isAuthor || authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Контент</div>
      <NuxtLink v-if="authStore.isAuthor || authStore.isEditor" to="/posts/create" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        Новый пост
      </NuxtLink>
      <NuxtLink v-if="authStore.isEditor" to="/events/create" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
        </svg>
        Новое событие
      </NuxtLink>
      <div v-if="authStore.isEditor" class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div v-if="authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Галерея</div>
      <NuxtLink v-if="authStore.isEditor" to="/gallery/create" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-pink-500 dark:text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
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

const canCreate = computed(() => authStore.isAuthor || authStore.isEditor)

const toggleMenu = () => { isMenuOpen.value = !isMenuOpen.value }
const closeMenu = () => { isMenuOpen.value = false }

const handleClickOutside = (event) => {
  if (menuRef.value && !menuRef.value.contains(event.target)) {
    isMenuOpen.value = false
  }
}

onMounted(() => { document.addEventListener('click', handleClickOutside) })
onUnmounted(() => { document.removeEventListener('click', handleClickOutside) })
</script>
```

---

#### `frontend/components/common/Breadcrumbs.vue`

```vue
<template>
  <nav class="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400" aria-label="Хлебные крошки">
    <NuxtLink to="/" class="flex items-center gap-1.5 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
      </svg>
      <span class="hidden sm:inline">Главная</span>
    </NuxtLink>
    <template v-if="items && items.length > 0">
      <template v-for="(item, index) in items" :key="index">
        <svg v-if="index === 0" class="w-4 h-4 flex-shrink-0 text-gray-400 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
        <NuxtLink v-if="item.to" :to="item.to" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors truncate">
          {{ item.label }}
        </NuxtLink>
        <span v-else class="truncate">{{ item.label }}</span>
        <svg v-if="index < items.length - 1 || (index === items.length - 1 && currentPageName)" class="w-4 h-4 flex-shrink-0 text-gray-400 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </template>
    </template>
    <span v-if="currentPageName" class="text-gray-700 dark:text-gray-300 font-medium truncate">
      {{ currentPageName }}
    </span>
  </nav>
</template>

<script setup>
const props = defineProps({
  items: { type: Array, default: () => [] },
  currentPageName: { type: String, default: '' }
})
</script>
```

---

### КОМПОНЕНТЫ FEATURES

#### EVENTS

`frontend/components/features/events/EventCard.vue`

```vue
<template>
  <NuxtLink :to="`/events/${event.id}`" class="group relative block bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden hover:-translate-y-1 aspect-[9/16]">
    <div class="absolute inset-0">
      <img v-if="event.display_image" :src="event.display_image" :alt="event.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" loading="lazy"/>
      <div v-else class="w-full h-full bg-gradient-to-br from-purple-400 via-pink-400 to-blue-500 flex items-center justify-center">
        <svg class="w-16 h-16 text-white/50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
        </svg>
      </div>
      <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 via-50% to-transparent"></div>
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black/20"></div>
    </div>
    <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
      <div v-if="isToday || isSoon" class="px-3 py-1 rounded-full text-xs font-semibold shadow-lg backdrop-blur-md" :class="isToday ? 'bg-gradient-to-r from-rose-500 to-red-600 text-white' : 'bg-gradient-to-r from-amber-400 to-orange-500 text-white'">
        <span class="flex items-center gap-1.5">
          <svg v-if="isToday" class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <svg v-else class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
          {{ isToday ? 'Сегодня' : 'Скоро' }}
        </span>
      </div>
      <div v-if="!event.is_published" class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-yellow-400 to-yellow-500 text-black shadow-lg backdrop-blur-md">
        <span class="flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
          Черновик
        </span>
      </div>
    </div>
    <div class="absolute bottom-0 left-0 right-0 p-5 z-10">
      <h3 class="text-lg md:text-xl font-bold text-white leading-tight line-clamp-2 group-hover:text-blue-300 transition-colors drop-shadow-lg">{{ event.title }}</h3>
      <p class="text-sm text-white/80 mt-1.5 line-clamp-2 drop-shadow-md font-light">{{ event.excerpt || event.content?.substring(0, 80) }}...</p>
      <div class="my-3 h-px bg-gradient-to-r from-white/30 via-white/10 to-transparent"></div>
      <div class="flex flex-wrap items-center gap-2 text-xs text-white/80">
        <span v-if="event.event_date" class="flex items-center gap-1.5 bg-white/10 backdrop-blur-md px-3 py-1 rounded-full border border-white/10">
          <svg class="w-3.5 h-3.5 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          {{ formatDate(event.event_date) }}
        </span>
        <span v-if="event.location" class="flex items-center gap-1.5 bg-white/10 backdrop-blur-md px-3 py-1 rounded-full border border-white/10">
          <svg class="w-3.5 h-3.5 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
          </svg>
          {{ event.location.length > 15 ? event.location.substring(0, 15) + '…' : event.location }}
        </span>
      </div>
      <div class="mt-3 flex items-center gap-2 text-xs font-medium text-white/60 group-hover:text-white transition-all duration-300 opacity-0 group-hover:opacity-100 translate-y-1 group-hover:translate-y-0">
        <span>Подробнее</span>
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({ event: { type: Object, required: true } })

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' })
}

const isToday = computed(() => {
  if (!props.event.event_date) return false
  const eventDate = new Date(props.event.event_date)
  const today = new Date()
  return eventDate.toDateString() === today.toDateString()
})

const isSoon = computed(() => {
  if (!props.event.event_date || isToday.value) return false
  const eventDate = new Date(props.event.event_date)
  const today = new Date()
  const diffDays = Math.ceil((eventDate - today) / (1000 * 60 * 60 * 24))
  return diffDays > 0 && diffDays <= 3
})
</script>

<style scoped>
.line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
</style>
```

---

#### `frontend/components/features/events/EventSection.vue`

```vue
<template>
  <section class="py-4">
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-blue-500 rounded-full"></div>
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
          </svg>
          Афиша
        </h2>
        <span v-if="totalItems > 0" class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">{{ totalItems }}</span>
      </div>
      <NuxtLink to="/events" class="group inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20 rounded-xl hover:bg-blue-100 dark:hover:bg-blue-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5">
        <span>Все события</span>
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </NuxtLink>
    </div>
    <div v-if="loading" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
      <SkeletonCard v-for="i in itemsPerPage" :key="i" />
    </div>
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет событий</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    <div v-else>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 md:gap-5">
        <EventCard v-for="event in currentPageItems" :key="event.id" :event="event" />
      </div>
      <Pagination :current-page="currentPage" :total-pages="totalPages" :max-visible="5" @page-change="onPageChange" />
    </div>
  </section>
</template>

<script setup>
import EventCard from './EventCard.vue'
import SkeletonCard from '~/components/ui/SkeletonCard.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  events: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  itemsPerPage: { type: Number, default: 5 }
})

const currentPage = ref(1)

const totalItems = computed(() => props.events.length)
const totalPages = computed(() => Math.ceil(totalItems.value / props.itemsPerPage))
const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return props.events.slice(start, end)
})

const onPageChange = (page) => {
  if (page === currentPage.value) return
  currentPage.value = page
}

watch(() => props.events, () => { currentPage.value = 1 }, { deep: true })
</script>
```

---

#### `frontend/components/features/events/EventDetail.vue`

```vue
<template>
  <div v-if="event" class="max-w-6xl mx-auto">
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <div class="relative aspect-[9/16] md:aspect-auto md:min-h-[400px] lg:min-h-[500px] overflow-hidden bg-gradient-to-br from-blue-600 to-purple-700">
          <img v-if="event.display_image" :src="event.display_image" :alt="event.title" class="w-full h-full object-cover"/>
          <div v-else class="w-full h-full flex items-center justify-center">
            <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
            </svg>
          </div>
          <div v-if="!event.is_published" class="absolute top-3 left-3 px-3 py-1 rounded-full text-xs font-semibold bg-yellow-500 text-black shadow-lg backdrop-blur-md">Черновик</div>
        </div>
        <div class="p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-4 leading-tight">{{ event.title }}</h1>
          <div class="prose prose-sm dark:prose-invert max-w-none mb-6">
            <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">{{ event.content }}</p>
          </div>
          <div class="space-y-4 mb-6">
            <div v-if="event.event_date" class="flex items-center gap-4 text-base text-gray-700 dark:text-gray-200">
              <div class="w-12 h-12 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Дата и время</span>
                <p class="font-semibold text-lg">{{ formatDateTime(event.event_date) }}</p>
              </div>
            </div>
            <div v-if="event.location" class="flex items-center gap-4 text-base text-gray-700 dark:text-gray-200">
              <div class="w-12 h-12 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-emerald-600 dark:text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Место проведения</span>
                <p class="font-semibold text-lg">{{ event.location }}</p>
              </div>
            </div>
            <div v-if="event.price" class="flex items-center gap-4 text-base text-gray-700 dark:text-gray-200">
              <div class="w-12 h-12 rounded-full bg-amber-100 dark:bg-amber-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-6 h-6 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Стоимость</span>
                <p class="font-semibold text-lg text-green-600 dark:text-green-400">{{ event.price }}</p>
              </div>
            </div>
          </div>
          <div class="flex flex-wrap gap-3">
            <NuxtLink v-if="event.button_link" :to="event.button_link" class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/>
              </svg>
              Купить билет
            </NuxtLink>
            <button v-if="canEdit" @click="editEvent" class="inline-flex items-center gap-2 px-4 py-2.5 text-sm font-medium text-gray-600 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 hover:text-gray-900 dark:hover:text-white transition-all duration-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
              </svg>
              Редактировать
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else-if="loading" class="text-center py-20">
    <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
  </div>
  <div v-else class="text-center py-20">
    <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Событие не найдено</p>
    <NuxtLink to="/events" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
      </svg>
      Вернуться к афише
    </NuxtLink>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()
const props = defineProps({ event: { type: Object, default: null }, loading: { type: Boolean, default: false } })
const emit = defineEmits(['delete'])
const router = useRouter()

const formatDateTime = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}

const canEdit = computed(() => {
  if (!props.event) return false
  const user = authStore.user
  if (!user) return false
  return user.role === 'editor' || user.username === props.event.author_name
})

const editEvent = () => { router.push(`/events/edit-${props.event.id}`) }
</script>
```

---

#### `frontend/components/features/events/FeaturedEvent.vue`

```vue
<template>
  <div v-if="event" class="mb-10">
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <div class="relative aspect-[9/16] md:aspect-auto md:min-h-[400px] overflow-hidden bg-gradient-to-br from-blue-600 to-purple-700">
          <img v-if="event.display_image" :src="event.display_image" :alt="event.title" class="w-full h-full object-cover"/>
          <div v-else class="w-full h-full flex items-center justify-center">
            <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
            </svg>
          </div>
          <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
            <div class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-amber-400 to-yellow-500 text-black shadow-lg backdrop-blur-md">
              <span class="flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/>
                </svg>
                ГЛАВНОЕ СОБЫТИЕ
              </span>
            </div>
          </div>
        </div>
        <div class="p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <h2 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-3 leading-tight">{{ event.title }}</h2>
          <p class="text-gray-600 dark:text-gray-300 text-sm md:text-base leading-relaxed mb-4">{{ event.excerpt || event.content?.substring(0, 200) }}...</p>
          <div class="space-y-3 mb-6">
            <div v-if="event.event_date" class="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-8 h-8 rounded-full bg-blue-100 dark:bg-blue-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-4 h-4 text-blue-600 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Дата и время</span>
                <p class="font-medium">{{ formatDate(event.event_date) }}</p>
              </div>
            </div>
            <div v-if="event.location" class="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-8 h-8 rounded-full bg-emerald-100 dark:bg-emerald-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-4 h-4 text-emerald-600 dark:text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Место проведения</span>
                <p class="font-medium">{{ event.location }}</p>
              </div>
            </div>
            <div v-if="event.price" class="flex items-center gap-3 text-sm text-gray-600 dark:text-gray-300">
              <div class="w-8 h-8 rounded-full bg-amber-100 dark:bg-amber-900/30 flex items-center justify-center flex-shrink-0">
                <svg class="w-4 h-4 text-amber-600 dark:text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div>
                <span class="text-xs text-gray-400 dark:text-gray-500">Стоимость</span>
                <p class="font-medium text-green-600 dark:text-green-400">{{ event.price }}</p>
              </div>
            </div>
          </div>
          <div class="flex flex-wrap gap-3">
            <NuxtLink :to="`/events/${event.id}`" class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
              Подробнее о событии
              <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </NuxtLink>
            <NuxtLink v-if="event.button_link" :to="event.button_link" class="inline-flex items-center gap-2 px-6 py-3 bg-transparent border-2 border-blue-500 text-blue-600 dark:text-blue-400 rounded-xl hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-all duration-300 font-medium hover:-translate-y-0.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/>
              </svg>
              Купить билет
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ event: { type: Object, default: null } })

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}
</script>
```

---

#### `frontend/components/features/events/EventList.vue`

```vue
<template>
  <div>
    <h2 class="text-xl font-semibold text-gray-700 dark:text-gray-300 mb-4 flex items-center gap-2">
      <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/>
      </svg>
      <span>Все события</span>
      <span class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">{{ events.length }}</span>
    </h2>
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div v-for="i in 4" :key="i" class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden">
        <div class="h-48 bg-gray-300 dark:bg-gray-600"></div>
        <div class="p-5 space-y-3">
          <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded w-3/4"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-full"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-2/3"></div>
        </div>
      </div>
    </div>
    <div v-else-if="events.length === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Остальные события скоро появятся</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <EventListItem v-for="event in events" :key="event.id" :event="event" :show-draft-badge="showDraftBadge" />
    </div>
  </div>
</template>

<script setup>
import EventListItem from './EventListItem.vue'

const props = defineProps({
  events: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  showDraftBadge: { type: Boolean, default: true }
})
</script>
```

---

#### `frontend/components/features/events/EventListItem.vue`

```vue
<template>
  <NuxtLink :to="`/events/${event.id}`" class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden block">
    <div class="grid grid-cols-1 sm:grid-cols-3">
      <div class="relative aspect-[9/16] sm:aspect-auto sm:min-h-[280px] md:min-h-[320px] lg:min-h-[360px] overflow-hidden bg-gradient-to-br from-blue-600 to-purple-700">
        <img v-if="event.display_image" :src="event.display_image" :alt="event.title" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy"/>
        <div v-else class="w-full h-full flex items-center justify-center">
          <svg class="w-16 h-16 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
          </svg>
        </div>
        <div class="absolute top-2 left-2 right-2 flex flex-wrap gap-1.5 z-10">
          <span v-if="!event.is_published && showDraftBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-yellow-400 text-black shadow-lg backdrop-blur-md">Черновик</span>
        </div>
      </div>
      <div class="col-span-2 p-5 flex flex-col justify-center">
        <h2 class="text-xl font-bold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition line-clamp-2">{{ event.title }}</h2>
        <p class="text-gray-600 dark:text-gray-300 text-sm mt-1.5 line-clamp-2">{{ event.excerpt || event.content?.substring(0, 120) }}...</p>
        <div class="flex flex-wrap gap-2 mt-3 text-sm text-gray-500 dark:text-gray-400">
          <span v-if="event.event_date" class="flex items-center gap-1.5 bg-gray-50 dark:bg-gray-700/50 px-2.5 py-1 rounded-full">
            <svg class="w-3.5 h-3.5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            {{ formatDate(event.event_date) }}
          </span>
          <span v-if="event.location" class="flex items-center gap-1.5 bg-gray-50 dark:bg-gray-700/50 px-2.5 py-1 rounded-full">
            <svg class="w-3.5 h-3.5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
            {{ event.location }}
          </span>
          <span v-if="event.price" class="flex items-center gap-1.5 bg-green-50 dark:bg-green-900/20 px-2.5 py-1 rounded-full text-green-600 dark:text-green-400">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            {{ event.price }}
          </span>
        </div>
        <div class="mt-3 flex items-center gap-2 text-sm font-medium text-blue-600 dark:text-blue-400 opacity-0 group-hover:opacity-100 transition-all duration-300">
          <span>Подробнее</span>
          <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  event: { type: Object, required: true },
  showDraftBadge: { type: Boolean, default: true }
})

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}
</script>

<style scoped>
.line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
</style>
```

---

### POSTS

#### `frontend/components/features/posts/PostCard.vue`

```vue
<template>
  <NuxtLink :to="`/posts/${post.id}`" class="group bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden flex flex-col h-full hover:-translate-y-1">
    <div class="relative aspect-video overflow-hidden flex-shrink-0 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-600 dark:to-gray-700">
      <img v-if="post.display_image" :src="post.display_image" :alt="post.title" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/>
      <div v-else class="w-full h-full flex items-center justify-center">
        <span class="text-4xl text-gray-400 dark:text-gray-500">📝</span>
      </div>
      <div v-if="isNew" class="absolute top-3 left-3 px-2.5 py-1 rounded-full text-xs font-medium bg-blue-500 text-white shadow-lg">
        <span class="flex items-center gap-1">
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          Новое
        </span>
      </div>
      <div v-if="!post.is_published && showDraftBadge" class="absolute top-3 right-3 px-2.5 py-1 rounded-full text-xs font-medium bg-yellow-500 text-white shadow-lg">
        <span class="flex items-center gap-1">
          <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
          Черновик
        </span>
      </div>
    </div>
    <div class="p-4 flex flex-col flex-1">
      <div class="flex-1">
        <h3 class="text-base font-semibold text-gray-800 dark:text-gray-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors line-clamp-2">{{ post.title }}</h3>
        <p class="text-gray-500 dark:text-gray-400 text-sm mt-1.5 line-clamp-3">{{ post.excerpt || post.content?.substring(0, 100) }}...</p>
      </div>
      <div class="mt-3 pt-3 border-t border-gray-100 dark:border-gray-700">
        <div class="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400">
          <div class="flex items-center gap-1.5">
            <img v-if="post.author_avatar" :src="post.author_avatar" :alt="post.author_name" class="w-5 h-5 rounded-full object-cover">
            <div v-else class="w-5 h-5 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-[8px] font-bold">
              {{ getInitials(post.author_name) }}
            </div>
            <span class="font-medium text-gray-700 dark:text-gray-300">{{ getAuthorFullName(post) }}</span>
          </div>
          <span>{{ formatDate(post.created_at) }}</span>
        </div>
        <div class="flex items-center gap-3 mt-2 text-xs text-gray-400 dark:text-gray-500">
          <span class="flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            {{ post.views || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            {{ post.comments?.length || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            {{ post.likes_count || 0 }}
          </span>
        </div>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  post: { type: Object, required: true },
  showDraftBadge: { type: Boolean, default: true }
})

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', year: 'numeric' })
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return name.substring(0, 2).toUpperCase()
}

const getAuthorFullName = (post) => {
  if (post.author_first_name || post.author_last_name) {
    const parts = []
    if (post.author_last_name) parts.push(post.author_last_name)
    if (post.author_first_name) parts.push(post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (post.author_full_name) return post.author_full_name
  return post.author_name || post.author?.username || 'Автор'
}

const isNew = computed(() => {
  if (!props.post.created_at) return false
  const postDate = new Date(props.post.created_at)
  const today = new Date()
  return postDate.toDateString() === today.toDateString()
})
</script>

<style scoped>
.line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.line-clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
</style>
```

---

#### `frontend/components/features/posts/PostSection.vue`

```vue
<template>
  <section class="py-4">
    <div class="flex justify-between items-center mb-6">
      <div class="flex items-center gap-3">
        <div class="w-1 h-8 bg-green-500 rounded-full"></div>
        <h2 class="text-2xl md:text-3xl font-bold text-gray-800 dark:text-gray-200 flex items-center gap-2">
          <svg class="w-8 h-8 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
          </svg>
          Публикации
        </h2>
        <span v-if="posts.length > 0" class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">{{ posts.length }}</span>
      </div>
      <NuxtLink to="/posts" class="group inline-flex items-center gap-2 px-4 py-2 text-sm font-medium text-green-600 dark:text-green-400 bg-green-50 dark:bg-green-900/20 rounded-xl hover:bg-green-100 dark:hover:bg-green-900/30 transition-all duration-300 hover:shadow-md hover:-translate-y-0.5">
        <span>Все публикации</span>
        <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
        </svg>
      </NuxtLink>
    </div>
    <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-5">
      <SkeletonCard v-for="i in limit" :key="i" />
    </div>
    <div v-else-if="posts.length === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет публикаций</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    <div v-else>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-5">
        <PostCard v-for="post in displayedPosts" :key="post.id" :post="post" :show-draft-badge="showDraftBadge" />
      </div>
      <div v-if="posts.length > limit" class="text-center mt-6">
        <button v-if="!showAll" @click="showAll = true" class="inline-flex items-center gap-2 px-6 py-2.5 bg-green-50 dark:bg-green-900/20 text-green-600 dark:text-green-400 rounded-xl hover:bg-green-100 dark:hover:bg-green-900/30 transition-all duration-300 text-sm font-medium hover:shadow-md hover:-translate-y-0.5">
          <span>Показать ещё {{ posts.length - limit }} публикаций</span>
          <svg class="w-4 h-4 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
          </svg>
        </button>
        <button v-else @click="showAll = false" class="inline-flex items-center gap-2 px-6 py-2.5 bg-gray-50 dark:bg-gray-700/50 text-gray-600 dark:text-gray-400 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-700 transition-all duration-300 text-sm font-medium hover:shadow-md">
          <svg class="w-4 h-4 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/>
          </svg>
          <span>Скрыть</span>
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import PostCard from './PostCard.vue'
import SkeletonCard from '~/components/ui/SkeletonCard.vue'

const props = defineProps({
  posts: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  limit: { type: Number, default: 4 },
  showDraftBadge: { type: Boolean, default: true }
})

const showAll = ref(false)

const displayedPosts = computed(() => {
  if (showAll.value || props.posts.length <= props.limit) return props.posts
  return props.posts.slice(0, props.limit)
})

watch(() => props.posts, () => { showAll.value = false }, { deep: true })
</script>
```

---

#### `frontend/components/features/posts/FeaturedPost.vue`

```vue
<template>
  <div v-if="post" class="mb-10">
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-0">
        <div class="relative aspect-[9/16] md:aspect-auto md:min-h-[320px] lg:min-h-[400px] overflow-hidden bg-gradient-to-br from-blue-600 to-purple-700">
          <img v-if="post.display_image" :src="post.display_image" :alt="post.title" class="w-full h-full object-cover"/>
          <div v-else class="w-full h-full flex items-center justify-center">
            <svg class="w-24 h-24 text-white/30" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
            </svg>
          </div>
          <div class="absolute top-3 left-3 right-3 flex flex-wrap gap-2 z-10">
            <div class="px-3 py-1 rounded-full text-xs font-semibold bg-gradient-to-r from-amber-400 to-yellow-500 text-black shadow-lg backdrop-blur-md">
              <span class="flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/>
                </svg>
                ГЛАВНАЯ ПУБЛИКАЦИЯ
              </span>
            </div>
          </div>
        </div>
        <div class="p-6 md:p-8 lg:p-10 flex flex-col justify-center">
          <h2 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-3 leading-tight">{{ post.title }}</h2>
          <div class="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-3">
            <img v-if="post.author_avatar" :src="post.author_avatar" :alt="post.author_name" class="w-6 h-6 rounded-full object-cover border border-gray-200 dark:border-gray-600">
            <div v-else class="w-6 h-6 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-[10px] font-bold flex-shrink-0">{{ getInitials(getAuthorFullName()) }}</div>
            <span>{{ getAuthorFullName() }}</span>
            <span class="text-gray-300 dark:text-gray-600">•</span>
            <span class="flex items-center gap-1">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              {{ formatDate(post.created_at) }}
            </span>
          </div>
          <p class="text-gray-600 dark:text-gray-300 text-sm md:text-base leading-relaxed mb-4 line-clamp-3">{{ post.excerpt || post.content?.substring(0, 200) }}...</p>
          <div class="flex flex-wrap gap-4 mb-6 text-sm text-gray-500 dark:text-gray-400">
            <span class="flex items-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
              </svg>
              {{ post.views || 0 }} просмотров
            </span>
            <span class="flex items-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
              </svg>
              {{ post.comments?.length || 0 }} комментариев
            </span>
            <span class="flex items-center gap-1.5">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
              {{ post.likes_count || 0 }} лайков
            </span>
          </div>
          <NuxtLink :to="`/posts/${post.id}`" class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
            Читать публикацию
            <svg class="w-4 h-4 transition-transform duration-300 group-hover:translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
            </svg>
          </NuxtLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ post: { type: Object, default: null } })

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

const getAuthorFullName = () => {
  if (!props.post) return 'Автор'
  if (props.post.author_first_name || props.post.author_last_name) {
    const parts = []
    if (props.post.author_last_name) parts.push(props.post.author_last_name)
    if (props.post.author_first_name) parts.push(props.post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (props.post.author_full_name) return props.post.author_full_name
  return props.post.author_name || 'Автор'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return name.substring(0, 2).toUpperCase()
}
</script>

<style scoped>
.line-clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
</style>
```

---

#### `frontend/components/features/posts/PostDetail.vue`

```vue
<template>
  <div v-if="post" class="max-w-4xl mx-auto">
    <div class="bg-white dark:bg-gray-800 rounded-2xl overflow-hidden shadow-xl border border-gray-100 dark:border-gray-700">
      <div class="relative aspect-video overflow-hidden bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-600 group/image">
        <img v-if="post.display_image" :src="post.display_image" :alt="post.title" class="w-full h-full object-cover transition-transform duration-700 group-hover/image:scale-105"/>
        <div v-else class="w-full h-full flex items-center justify-center">
          <svg class="w-24 h-24 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
          </svg>
        </div>
        <button v-if="authStore.isAuthenticated" @click="toggleLike" class="absolute inset-0 flex items-center justify-center opacity-0 group-hover/image:opacity-100 transition-all duration-300">
          <div class="p-5 rounded-full bg-white/10 backdrop-blur-sm hover:bg-white/20 transition-all duration-300 scale-90 group-hover/image:scale-100" :class="{ 'animate-like': isLiking }">
            <svg class="w-14 h-14 transition-all duration-300 drop-shadow-lg" :class="post.user_has_liked ? 'text-red-500 fill-red-500' : 'text-white fill-none hover:text-red-400'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
        </button>
        <div v-if="!post.is_published" class="absolute top-3 left-3 px-3 py-1 rounded-full text-xs font-semibold bg-yellow-500 text-black shadow-lg backdrop-blur-md">Черновик</div>
        <div v-if="isNew" class="absolute top-3 right-3 px-3 py-1 rounded-full text-xs font-semibold bg-blue-500 text-white shadow-lg backdrop-blur-md">Новое</div>
        <div class="absolute bottom-3 right-3 px-3 py-1.5 rounded-full bg-black/50 backdrop-blur-md text-white text-sm flex items-center gap-1.5">
          <svg class="w-4 h-4" :class="post.user_has_liked ? 'text-red-500 fill-red-500' : 'text-white'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
          </svg>
          <span>{{ post.likes_count || 0 }}</span>
        </div>
      </div>
      <div class="p-6 md:p-8 lg:p-10">
        <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-4 leading-tight">{{ post.title }}</h1>
        <div class="flex flex-wrap items-center gap-3 text-sm text-gray-500 dark:text-gray-400 mb-6 pb-6 border-b border-gray-100 dark:border-gray-700">
          <div class="flex items-center gap-2">
            <img v-if="post.author_avatar" :src="post.author_avatar" :alt="post.author_name" class="w-8 h-8 rounded-full object-cover border border-gray-200 dark:border-gray-600">
            <div v-else class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-xs font-bold flex-shrink-0">{{ getInitials(getAuthorFullName()) }}</div>
            <div class="flex flex-col">
              <span class="font-medium text-gray-700 dark:text-gray-300">{{ getAuthorFullName() }}</span>
              <span class="text-xs text-gray-400 dark:text-gray-500">{{ post.author_role === 'editor' ? 'Главный редактор' : 'Автор' }}</span>
            </div>
          </div>
          <span class="text-gray-300 dark:text-gray-600">•</span>
          <div class="flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <span>{{ formatDate(post.created_at) }}</span>
          </div>
          <span class="text-gray-300 dark:text-gray-600">•</span>
          <div class="flex items-center gap-1">
            <svg class="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            <span>{{ post.views || 0 }} просмотров</span>
          </div>
        </div>
        <div class="prose prose-lg dark:prose-invert max-w-none">
          <div class="text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-wrap">{{ post.content }}</div>
        </div>
        <div class="mt-6 pt-6 border-t border-gray-100 dark:border-gray-700 flex flex-wrap gap-4 text-sm text-gray-500 dark:text-gray-400">
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            {{ post.comments?.length || 0 }} комментариев
          </span>
          <span class="flex items-center gap-1.5">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            {{ post.likes_count || 0 }} лайков
          </span>
        </div>
        <div v-if="canEdit" class="mt-6 pt-6 border-t border-gray-100 dark:border-gray-700">
          <button @click="editPost" class="inline-flex items-center gap-2 px-4 py-2.5 text-sm font-medium text-gray-600 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 rounded-xl hover:bg-gray-200 dark:hover:bg-gray-600 hover:text-gray-900 dark:hover:text-white transition-all duration-300">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
            </svg>
            Редактировать
          </button>
        </div>
      </div>
    </div>
    <PostComments :post-id="post.id" :comments="post.comments || []" @comment-added="onCommentAdded" @comment-deleted="onCommentDeleted" @comment-updated="onCommentUpdated" />
    <div class="mt-6">
      <NuxtLink to="/posts" class="inline-flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
        </svg>
        Назад к публикациям
      </NuxtLink>
    </div>
  </div>
  <div v-else-if="loading" class="text-center py-20">
    <svg class="w-12 h-12 mx-auto text-gray-300 dark:text-gray-600 animate-spin mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Загрузка...</p>
  </div>
  <div v-else class="text-center py-20">
    <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
    </svg>
    <p class="text-gray-500 dark:text-gray-400">Пост не найден</p>
    <NuxtLink to="/posts" class="mt-4 inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 font-medium shadow-lg shadow-blue-500/25 hover:shadow-xl hover:shadow-blue-500/40 hover:-translate-y-0.5">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
      </svg>
      Вернуться к публикациям
    </NuxtLink>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import PostComments from '~/components/features/posts/PostComments.vue'

const authStore = useAuthStore()
const props = defineProps({
  post: { type: Object, default: null },
  loading: { type: Boolean, default: false }
})
const emit = defineEmits(['delete', 'like-updated'])
const router = useRouter()
const config = useRuntimeConfig()
const isLiking = ref(false)

const getAuthorFullName = () => {
  if (!props.post) return 'Автор'
  if (props.post.author_first_name || props.post.author_last_name) {
    const parts = []
    if (props.post.author_last_name) parts.push(props.post.author_last_name)
    if (props.post.author_first_name) parts.push(props.post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (props.post.author_full_name) return props.post.author_full_name
  return props.post.author_name || 'Автор'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

const isNew = computed(() => {
  if (!props.post?.created_at) return false
  const postDate = new Date(props.post.created_at)
  const today = new Date()
  return postDate.toDateString() === today.toDateString()
})

const toggleLike = async () => {
  if (!authStore.isAuthenticated) { router.push('/auth/login'); return }
  isLiking.value = true
  try {
    const res = await fetch(`${config.public.apiBase}/likes/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${authStore.accessToken}` },
      body: JSON.stringify({ post: props.post.id })
    })
    if (res.ok) {
      const data = await res.json()
      if (data.action === 'liked') { props.post.likes_count = (props.post.likes_count || 0) + 1; props.post.user_has_liked = true }
      else if (data.action === 'unliked') { props.post.likes_count = (props.post.likes_count || 0) - 1; props.post.user_has_liked = false }
      emit('like-updated', { likesCount: props.post.likes_count, isLiked: props.post.user_has_liked })
      setTimeout(() => { isLiking.value = false }, 600)
    }
  } catch (e) { console.error('Ошибка:', e); isLiking.value = false }
}

const canEdit = computed(() => {
  if (!props.post) return false
  const user = authStore.user
  if (!user) return false
  return user.role === 'editor' || user.username === props.post.author_name
})

const editPost = () => { router.push(`/posts/edit-${props.post.id}`) }
const onCommentAdded = (comment) => { console.log('Комментарий добавлен:', comment) }
const onCommentDeleted = (commentId) => { console.log('Комментарий удалён:', commentId) }
const onCommentUpdated = (comment) => { console.log('Комментарий обновлён:', comment) }
</script>

<style scoped>
@keyframes likeAnimation {
  0% { transform: scale(1); }
  25% { transform: scale(1.3); }
  50% { transform: scale(0.9); }
  75% { transform: scale(1.15); }
  100% { transform: scale(1); }
}
.animate-like { animation: likeAnimation 0.6s ease forwards; }
</style>
```

---

#### `frontend/components/features/posts/PostComments.vue`

```vue
<template>
  <div class="mt-8 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700">
    <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-4 flex items-center gap-2">
      <svg class="w-6 h-6 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
      </svg>
      Комментарии ({{ totalCommentsCount }})
    </h2>
    <div v-if="comments?.length === 0" class="text-gray-500 dark:text-gray-400 text-center py-8">Пока нет комментариев. Будьте первым!</div>
    <div v-else>
      <CommentItem v-for="comment in comments" :key="comment.id" :comment="comment" :editing-id="editingCommentId" :saving-edit="savingEdit"
        @start-edit="startEditComment" @start-reply="(commentId, authorName) => startReplyComment(commentId, authorName)"
        @save-edit="saveEditComment" @cancel-edit="cancelEditComment" @delete-comment="deleteComment" />
    </div>
  </div>
  <div class="mt-6 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700">
    <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">{{ replyToCommentId ? 'Ответ на комментарий' : 'Добавить комментарий' }}</h3>
    <div v-if="replyToCommentId" class="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg mb-3 border border-gray-200 dark:border-gray-600">
      <p class="text-sm text-gray-600 dark:text-gray-300">Ответ для <span class="font-semibold">{{ replyToAuthorName }}</span>:</p>
      <button @click="cancelReply" class="text-red-500 text-sm hover:text-red-700 transition">Отменить ответ</button>
    </div>
    <form v-if="isAuthenticated" @submit.prevent="submitComment">
      <textarea v-model="newComment" class="w-full border border-gray-300 dark:border-gray-600 rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" rows="3" placeholder="Напишите ваш комментарий..." required></textarea>
      <UiButton type="submit" variant="primary" :disabled="submitting" class="mt-2">{{ submitting ? 'Отправка...' : replyToCommentId ? 'Ответить' : 'Отправить' }}</UiButton>
    </form>
    <div v-else class="text-center py-3 text-gray-500 dark:text-gray-400">
      <NuxtLink to="/auth/login" class="text-blue-500 dark:text-blue-400 hover:underline">Войдите</NuxtLink>, чтобы оставить комментарий
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
import UiButton from '~/components/ui/UiButton.vue'
import CommentItem from '~/components/CommentItem.vue'

const authStore = useAuthStore()
const props = defineProps({
  postId: { type: Number, required: true },
  comments: { type: Array, default: () => [] }
})
const emit = defineEmits(['comment-added', 'comment-deleted', 'comment-updated'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const isAuthenticated = computed(() => authStore.isAuthenticated)

const newComment = ref('')
const submitting = ref(false)
const replyToCommentId = ref(null)
const replyToAuthorName = ref('')
const editingCommentId = ref(null)
const savingEdit = ref(false)

const totalCommentsCount = computed(() => {
  if (!props.comments || props.comments.length === 0) return 0
  let count = 0
  const countComments = (comments) => {
    comments.forEach(c => {
      count++
      if (c.replies && c.replies.length > 0) countComments(c.replies)
    })
  }
  countComments(props.comments)
  return count
})

const findComment = (comments, id) => {
  if (!comments) return null
  for (const comment of comments) {
    if (comment.id === id) return comment
    if (comment.replies && comment.replies.length > 0) {
      const found = findComment(comment.replies, id)
      if (found) return found
    }
  }
  return null
}

const submitComment = async () => {
  if (!newComment.value.trim()) return
  submitting.value = true
  try {
    const body = { post: props.postId, content: newComment.value.trim() }
    if (replyToCommentId.value) body.parent = replyToCommentId.value
    const res = await fetch(`${API_URL}/comments/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${authStore.accessToken}` },
      body: JSON.stringify(body)
    })
    if (res.ok) {
      const comment = await res.json()
      if (replyToCommentId.value) {
        const parentComment = findComment(props.comments, replyToCommentId.value)
        if (parentComment) { if (!parentComment.replies) parentComment.replies = []; parentComment.replies.push(comment) }
      } else {
        if (props.comments) props.comments.push(comment)
      }
      newComment.value = ''
      cancelReply()
      emit('comment-added', comment)
    }
  } catch (e) { console.error('Ошибка:', e); alert('Ошибка при отправке комментария') }
  finally { submitting.value = false }
}

const startReplyComment = (commentId, authorName) => { replyToCommentId.value = commentId; replyToAuthorName.value = authorName }
const cancelReply = () => { replyToCommentId.value = null; replyToAuthorName.value = '' }
const startEditComment = (comment) => { editingCommentId.value = comment.id; editCommentContent.value = comment.content }
const cancelEditComment = () => { editingCommentId.value = null; editCommentContent.value = '' }

const saveEditComment = async (commentId, content) => {
  if (!content.trim()) return
  savingEdit.value = true
  try {
    const res = await fetch(`${API_URL}/comments/${commentId}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${authStore.accessToken}` },
      body: JSON.stringify({ content: content.trim() })
    })
    if (res.ok) {
      const updatedComment = await res.json()
      const updateCommentInTree = (comments) => {
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].id === commentId) { comments[i] = updatedComment; return true }
          if (comments[i].replies && comments[i].replies.length > 0) {
            if (updateCommentInTree(comments[i].replies)) return true
          }
        }
        return false
      }
      updateCommentInTree(props.comments)
      cancelEditComment()
      emit('comment-updated', updatedComment)
    }
  } catch (e) { console.error('Ошибка:', e); alert('Ошибка при редактировании комментария') }
  finally { savingEdit.value = false }
}

const deleteComment = async (commentId) => {
  if (!confirm('Вы уверены, что хотите удалить этот комментарий?')) return
  try {
    const res = await fetch(`${API_URL}/comments/${commentId}/`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${authStore.accessToken}` }
    })
    if (res.ok) {
      const removeCommentFromTree = (comments) => {
        for (let i = 0; i < comments.length; i++) {
          if (comments[i].id === commentId) { comments.splice(i, 1); return true }
          if (comments[i].replies && comments[i].replies.length > 0) {
            if (removeCommentFromTree(comments[i].replies)) return true
          }
        }
        return false
      }
      removeCommentFromTree(props.comments)
      emit('comment-deleted', commentId)
    }
  } catch (e) { console.error('Ошибка:', e); alert('Ошибка при удалении комментария') }
}
</script>
```

---

#### `frontend/components/features/posts/PostList.vue`

```vue
<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-semibold text-gray-700 dark:text-gray-300 flex items-center gap-2">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"/>
        </svg>
        <span>Все публикации</span>
        <span class="text-sm text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 px-2.5 py-0.5 rounded-full">{{ totalItems }}</span>
      </h2>
    </div>
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="i in itemsPerPage" :key="i" class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden">
        <div class="aspect-video bg-gray-300 dark:bg-gray-600"></div>
        <div class="p-5 space-y-3">
          <div class="h-6 bg-gray-300 dark:bg-gray-600 rounded w-3/4"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-full"></div>
          <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-2/3"></div>
        </div>
      </div>
    </div>
    <div v-else-if="totalItems === 0" class="text-center py-12 bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700">
      <svg class="w-20 h-20 mx-auto text-gray-300 dark:text-gray-600 mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11v4m0 0h-2m2 0h2"/>
      </svg>
      <p class="text-gray-500 dark:text-gray-400">Пока нет публикаций</p>
      <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">Следите за обновлениями!</p>
    </div>
    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <PostListItem v-for="post in currentPageItems" :key="post.id" :post="post" :show-draft-badge="showDraftBadge" />
      </div>
      <Pagination :current-page="currentPage" :total-pages="totalPages" :max-visible="5" @page-change="onPageChange" />
    </div>
  </div>
</template>

<script setup>
import PostListItem from './PostListItem.vue'
import Pagination from '~/components/ui/Pagination.vue'

const props = defineProps({
  posts: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  itemsPerPage: { type: Number, default: 9 },
  showDraftBadge: { type: Boolean, default: true }
})

const currentPage = ref(1)
const totalItems = computed(() => props.posts.length)
const totalPages = computed(() => Math.ceil(totalItems.value / props.itemsPerPage))
const currentPageItems = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage
  const end = start + props.itemsPerPage
  return props.posts.slice(start, end)
})

const onPageChange = (page) => {
  if (page === currentPage.value) return
  currentPage.value = page
}

watch(() => props.posts, () => { currentPage.value = 1 }, { deep: true })
</script>
```

---

#### `frontend/components/features/posts/PostListItem.vue`

```vue
<template>
  <NuxtLink :to="`/posts/${post.id}`" class="bg-white dark:bg-gray-800 rounded-xl shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden flex flex-col group hover:-translate-y-1">
    <div class="relative aspect-video overflow-hidden flex-shrink-0 bg-gradient-to-r from-gray-200 to-gray-300 dark:from-gray-700 dark:to-gray-600">
      <img v-if="post.display_image" :src="post.display_image" :alt="post.title" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" loading="lazy"/>
      <div v-else class="w-full h-full flex items-center justify-center">
        <svg class="w-16 h-16 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9"/>
        </svg>
      </div>
      <div v-if="!post.is_published && showDraftBadge" class="absolute top-3 right-3 px-2.5 py-1 rounded-full text-xs font-semibold bg-yellow-400 text-black shadow-lg backdrop-blur-md">Черновик</div>
    </div>
    <div class="p-5 flex flex-col flex-1">
      <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-200 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition line-clamp-2">{{ post.title }}</h2>
      <div class="flex items-center gap-2 mt-2 text-sm text-gray-500 dark:text-gray-400">
        <img v-if="post.author_avatar" :src="post.author_avatar" :alt="post.author_name" class="w-6 h-6 rounded-full object-cover border border-gray-200 dark:border-gray-600">
        <div v-else class="w-6 h-6 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-[10px] font-bold flex-shrink-0">{{ getInitials(getAuthorFullName()) }}</div>
        <span>{{ getAuthorFullName() }}</span>
      </div>
      <p class="text-gray-600 dark:text-gray-400 text-sm mt-2 line-clamp-3">{{ post.excerpt || post.content?.substring(0, 120) }}...</p>
      <div class="flex justify-between items-center mt-4 pt-4 border-t border-gray-100 dark:border-gray-700">
        <div class="flex items-center gap-3 text-sm text-gray-400 dark:text-gray-500">
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
            </svg>
            {{ post.views || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            {{ post.comments?.length || 0 }}
          </span>
          <span class="flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            {{ post.likes_count || 0 }}
          </span>
        </div>
        <span class="text-xs text-gray-400 dark:text-gray-500 flex items-center gap-1">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          {{ formatDate(post.created_at) }}
        </span>
      </div>
    </div>
  </NuxtLink>
</template>

<script setup>
const props = defineProps({
  post: { type: Object, required: true },
  showDraftBadge: { type: Boolean, default: true }
})

const getAuthorFullName = () => {
  if (props.post.author_first_name || props.post.author_last_name) {
    const parts = []
    if (props.post.author_last_name) parts.push(props.post.author_last_name)
    if (props.post.author_first_name) parts.push(props.post.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (props.post.author_full_name) return props.post.author_full_name
  return props.post.author_name || 'Автор'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', year: 'numeric' })
}
</script>

<style scoped>
.line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.line-clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
</style>
```


---

### UI

#### `frontend/components/ui/UiButton.vue`

```vue
<!-- frontend/components/ui/UiButton.vue -->
<template>
  <button :type="type" :disabled="disabled" class="px-6 py-2.5 rounded-xl transition-all duration-300 font-medium inline-flex items-center justify-center gap-2 shadow-sm hover:shadow-md active:scale-95" :class="[variantClasses, sizeClasses, widthClass]" @click="$emit('click')">
    <slot />
  </button>
</template>

<script setup>
const props = defineProps({
  variant: { type: String, default: 'primary', validator: (value) => ['primary', 'secondary', 'danger', 'warning', 'outline', 'success', 'ghost'].includes(value) },
  type: { type: String, default: 'button' },
  disabled: { type: Boolean, default: false },
  size: { type: String, default: 'md', validator: (value) => ['sm', 'md', 'lg'].includes(value) },
  fullWidth: { type: Boolean, default: false }
})
const emit = defineEmits(['click'])

const variantClasses = computed(() => {
  const variants = {
    primary: 'bg-gradient-to-r from-blue-500 to-blue-600 text-white hover:from-blue-600 hover:to-blue-700 disabled:from-blue-300 disabled:to-blue-400 dark:disabled:from-blue-800 dark:disabled:to-blue-900 shadow-blue-500/25 hover:shadow-blue-500/40',
    secondary: 'bg-gradient-to-r from-gray-500 to-gray-600 text-white hover:from-gray-600 hover:to-gray-700 disabled:from-gray-300 disabled:to-gray-400 dark:disabled:from-gray-700 dark:disabled:to-gray-800 shadow-gray-500/25 hover:shadow-gray-500/40',
    success: 'bg-gradient-to-r from-emerald-500 to-green-600 text-white hover:from-emerald-600 hover:to-green-700 disabled:from-emerald-300 disabled:to-green-400 dark:disabled:from-emerald-800 dark:disabled:to-green-900 shadow-emerald-500/25 hover:shadow-emerald-500/40',
    danger: 'bg-gradient-to-r from-red-500 to-red-600 text-white hover:from-red-600 hover:to-red-700 disabled:from-red-300 disabled:to-red-400 dark:disabled:from-red-800 dark:disabled:to-red-900 shadow-red-500/25 hover:shadow-red-500/40',
    warning: 'bg-gradient-to-r from-amber-500 to-yellow-600 text-white hover:from-amber-600 hover:to-yellow-700 disabled:from-amber-300 disabled:to-yellow-400 dark:disabled:from-amber-800 dark:disabled:to-yellow-900 shadow-amber-500/25 hover:shadow-amber-500/40',
    outline: 'bg-transparent border-2 border-blue-500 text-blue-600 dark:text-blue-400 hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:border-blue-600 dark:hover:border-blue-300 disabled:opacity-50 disabled:cursor-not-allowed',
    ghost: 'bg-transparent text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white disabled:opacity-50 disabled:cursor-not-allowed'
  }
  return variants[props.variant] || variants.primary
})
const sizeClasses = computed(() => {
  const sizes = { sm: 'px-3.5 py-2 text-sm', md: 'px-6 py-2.5 text-base', lg: 'px-8 py-3.5 text-lg' }
  return sizes[props.size] || sizes.md
})
const widthClass = computed(() => props.fullWidth ? 'w-full' : '')
</script>
```

---

#### `frontend/components/ui/UiInput.vue`

```vue
<!-- frontend/components/ui/UiInput.vue -->
<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <input :type="type" :value="modelValue" :placeholder="placeholder" :required="required" :disabled="disabled" class="w-full border rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" :class="inputClasses" @input="$emit('update:modelValue', $event.target.value)" @blur="$emit('blur')" @focus="$emit('focus')" />
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { type: [String, Number], default: '' },
  label: { type: String, default: '' },
  type: { type: String, default: 'text' },
  placeholder: { type: String, default: '' },
  required: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  error: { type: String, default: '' },
  hint: { type: String, default: '' },
  variant: { type: String, default: 'default', validator: (value) => ['default', 'success', 'error'].includes(value) }
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
<!-- frontend/components/ui/UiTextarea.vue -->
<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <textarea :value="modelValue" :placeholder="placeholder" :rows="rows" :required="required" :disabled="disabled" class="w-full border rounded-xl p-3 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 transition bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" :class="inputClasses" @input="$emit('update:modelValue', $event.target.value)" @blur="$emit('blur')" @focus="$emit('focus')"></textarea>
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { type: String, default: '' },
  label: { type: String, default: '' },
  placeholder: { type: String, default: '' },
  rows: { type: Number, default: 3 },
  required: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  error: { type: String, default: '' },
  hint: { type: String, default: '' },
  variant: { type: String, default: 'default', validator: (value) => ['default', 'success', 'error'].includes(value) }
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
<!-- frontend/components/ui/UiCheckbox.vue -->
<template>
  <label class="flex items-center gap-2 cursor-pointer group">
    <div class="relative">
      <input type="checkbox" :checked="modelValue" :disabled="disabled" class="w-4 h-4 text-blue-500 rounded focus:ring-2 focus:ring-blue-500 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed" @change="$emit('update:modelValue', $event.target.checked)" />
    </div>
    <span class="text-gray-700 dark:text-gray-300 select-none" :class="disabled ? 'opacity-50' : ''"><slot /></span>
  </label>
</template>

<script setup>
defineProps({ modelValue: { type: Boolean, default: false }, disabled: { type: Boolean, default: false } })
defineEmits(['update:modelValue'])
</script>
```

---

#### `frontend/components/ui/UiCard.vue`

```vue
<!-- frontend/components/ui/UiCard.vue -->
<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow" :class="paddingClass"><slot /></div>
</template>

<script setup>
const props = defineProps({ padding: { type: String, default: 'md', validator: (value) => ['none', 'sm', 'md', 'lg'].includes(value) } })
const paddingClass = computed(() => {
  const paddings = { none: 'p-0', sm: 'p-3', md: 'p-6', lg: 'p-8' }
  return paddings[props.padding] || paddings.md
})
</script>
```

---

#### `frontend/components/ui/UiFileInput.vue`

```vue
<!-- frontend/components/ui/UiFileInput.vue -->
<template>
  <div class="mb-4">
    <label v-if="label" class="block text-gray-700 dark:text-gray-300 mb-2 text-sm font-medium">
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>
    <div class="relative border-2 border-dashed rounded-xl p-6 transition bg-white dark:bg-gray-700" :class="[isDragging ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20' : 'border-gray-300 dark:border-gray-600', disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer hover:border-blue-400']" @dragover.prevent="isDragging = true" @dragleave.prevent="isDragging = false" @drop.prevent="handleDrop" @click="triggerFileInput">
      <div class="text-center">
        <div class="text-4xl mb-2">{{ multiple ? '📁' : '📄' }}</div>
        <p class="text-gray-600 dark:text-gray-300">{{ multiple ? 'Перетащите файлы сюда или кликните для выбора' : 'Перетащите файл сюда или кликните для выбора' }}</p>
        <p class="text-sm text-gray-400 dark:text-gray-500 mt-1">{{ accept ? `Поддерживаемые форматы: ${accept}` : 'Любые форматы' }}{{ maxSize ? ` • Максимум: ${formatFileSize(maxSize)}` : '' }}</p>
        <p v-if="multiple" class="text-sm text-gray-400 dark:text-gray-500">Можно выбрать несколько файлов</p>
      </div>
      <input ref="fileInputRef" type="file" :accept="accept" :multiple="multiple" :disabled="disabled" class="absolute inset-0 opacity-0 cursor-pointer" @change="handleFileSelect" />
    </div>
    <div v-if="filePreviews.length > 0" class="mt-3">
      <div class="flex flex-wrap gap-2">
        <div v-for="(file, index) in filePreviews" :key="index" class="relative group">
          <div v-if="file.preview" class="relative">
            <img :src="file.preview" :alt="file.name" class="w-20 h-20 object-cover rounded-lg border border-gray-200 dark:border-gray-600" />
            <button v-if="!disabled && removable" type="button" class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100" @click="removeFile(index)">✕</button>
          </div>
          <div v-else class="relative">
            <div class="w-20 h-20 bg-gray-100 dark:bg-gray-600 rounded-lg border border-gray-200 dark:border-gray-600 flex items-center justify-center"><span class="text-3xl">📄</span></div>
            <button v-if="!disabled && removable" type="button" class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-5 h-5 flex items-center justify-center hover:bg-red-600 transition text-xs opacity-0 group-hover:opacity-100" @click="removeFile(index)">✕</button>
          </div>
          <p class="text-xs text-gray-500 dark:text-gray-400 mt-1 truncate max-w-[80px] text-center">{{ file.name }}</p>
        </div>
      </div>
      <p v-if="multiple && filePreviews.length > 0" class="text-xs text-gray-400 dark:text-gray-500 mt-2">Выбрано файлов: {{ filePreviews.length }}</p>
    </div>
    <p v-if="error" class="text-red-500 text-sm mt-1">{{ error }}</p>
    <p v-if="hint" class="text-gray-400 dark:text-gray-500 text-sm mt-1">{{ hint }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { type: [File, Array, null], default: null },
  label: { type: String, default: '' },
  hint: { type: String, default: '' },
  error: { type: String, default: '' },
  required: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  multiple: { type: Boolean, default: false },
  accept: { type: String, default: '' },
  maxSize: { type: Number, default: 5 * 1024 * 1024 },
  removable: { type: Boolean, default: true }
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
    return { valid: false, message: `Файл "${file.name}" слишком большой. Максимум: ${formatFileSize(props.maxSize)}` }
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
        const fileData = { file: file, preview: e.target.result, name: file.name, type: file.type, size: file.size }
        callback(fileData)
      }
      reader.readAsDataURL(file)
    } catch (e) { console.error('Ошибка создания превью:', e); callback(file) }
  } else { callback(file) }
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
  if (!props.multiple) filePreviews.value = []
  let processedCount = 0
  for (const file of filesArray) {
    const sizeCheck = validateFileSize(file)
    if (!sizeCheck.valid) { errors.push(sizeCheck.message); continue }
    createPreview(file, (fileData) => {
      if (props.multiple) { filePreviews.value = [...filePreviews.value, fileData] }
      else { filePreviews.value = [fileData] }
      processedCount++
      if (processedCount === filesArray.length) { updateModel(); emit('change', filePreviews.value) }
    })
  }
  if (errors.length > 0) alert(errors.join('\n'))
  if (filesArray.length === 0) { updateModel(); emit('change', filePreviews.value) }
}

const updateModel = () => {
  if (props.multiple) {
    const files = filePreviews.value.map(f => f.file || f)
    emit('update:modelValue', files)
  } else {
    const first = filePreviews.value[0]
    if (first) { const fileData = first.file || first; emit('update:modelValue', fileData) }
    else { emit('update:modelValue', null) }
  }
}

const triggerFileInput = () => { if (!props.disabled && fileInputRef.value) fileInputRef.value.click() }
const removeFile = (index) => { filePreviews.value.splice(index, 1); updateModel(); emit('remove', index); emit('change', filePreviews.value) }
const reset = () => { filePreviews.value = []; updateModel() }

defineExpose({ filePreviews, reset })
</script>
```

---

#### `frontend/components/ui/SkeletonCard.vue`

```vue
<!-- frontend/components/ui/SkeletonCard.vue -->
<template>
  <div class="bg-gray-200 dark:bg-gray-700 rounded-xl animate-pulse overflow-hidden">
    <div class="aspect-[4/3] bg-gray-300 dark:bg-gray-600"></div>
    <div class="p-4 space-y-3">
      <div class="h-4 bg-gray-300 dark:bg-gray-600 rounded w-3/4"></div>
      <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-full"></div>
      <div class="h-3 bg-gray-300 dark:bg-gray-600 rounded w-2/3"></div>
    </div>
  </div>
</template>
```

---

#### `frontend/components/ui/Pagination.vue`

```vue
<!-- frontend/components/ui/Pagination.vue -->
<template>
  <div v-if="totalPages > 1" class="flex items-center justify-center gap-1 mt-6">
    <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1" class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 disabled:opacity-40 disabled:cursor-not-allowed" :class="currentPage === 1 ? 'text-gray-400 dark:text-gray-600 bg-gray-100 dark:bg-gray-800' : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
      </svg>
    </button>
    <div class="flex gap-1">
      <button v-if="showFirstDots" @click="goToPage(1)" class="px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white">1</button>
      <span v-if="showFirstDots" class="px-2 py-2 text-gray-400 dark:text-gray-600">…</span>
      <button v-for="page in visiblePages" :key="page" @click="goToPage(page)" class="px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200" :class="page === currentPage ? 'bg-gradient-to-r from-blue-500 to-blue-600 text-white shadow-lg shadow-blue-500/25 scale-105' : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'">{{ page }}</button>
      <span v-if="showLastDots" class="px-2 py-2 text-gray-400 dark:text-gray-600">…</span>
      <button v-if="showLastDots" @click="goToPage(totalPages)" class="px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white">{{ totalPages }}</button>
    </div>
    <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages" class="px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 disabled:opacity-40 disabled:cursor-not-allowed" :class="currentPage === totalPages ? 'text-gray-400 dark:text-gray-600 bg-gray-100 dark:bg-gray-800' : 'text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-white'">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
const props = defineProps({ currentPage: { type: Number, required: true, default: 1 }, totalPages: { type: Number, required: true, default: 1 }, maxVisible: { type: Number, default: 5 } })
const emit = defineEmits(['page-change'])

const showFirstDots = computed(() => props.currentPage > Math.ceil(props.maxVisible / 2) + 1)
const showLastDots = computed(() => props.currentPage < props.totalPages - Math.ceil(props.maxVisible / 2))
const visiblePages = computed(() => {
  const total = props.totalPages, current = props.currentPage, maxVisible = props.maxVisible
  if (total <= maxVisible) return Array.from({ length: total }, (_, i) => i + 1)
  let start = Math.max(1, current - Math.floor(maxVisible / 2))
  let end = Math.min(total, start + maxVisible - 1)
  if (end - start + 1 < maxVisible) start = Math.max(1, end - maxVisible + 1)
  return Array.from({ length: end - start + 1 }, (_, i) => start + i)
})
const goToPage = (page) => { if (page < 1 || page > props.totalPages || page === props.currentPage) return; emit('page-change', page) }
</script>
```

---

### LAYOUT & COMMON

#### `frontend/components/layout/AppHeader.vue`

```vue
<!-- frontend/components/layout/AppHeader.vue -->
<template>
  <header class="bg-white dark:bg-gray-800 shadow transition-colors duration-200 sticky top-0 z-50 border-b border-gray-200 dark:border-gray-700">
    <div class="container mx-auto px-4 py-3 flex justify-between items-center">
      <div class="flex items-center gap-2">
        <AppLogo />
        <BurgerMenu />
      </div>
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
<!-- frontend/components/layout/AppFooter.vue -->
<template>
  <footer class="app-footer text-gray-300 mt-10">
    <div class="container mx-auto px-4">
      <div v-if="contactsLoading" class="text-center py-4 text-gray-400">Загрузка контактов...</div>
      <div v-else-if="contacts" class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
            </svg>
            Центр Культуры
          </h3>
          <p class="text-sm text-gray-400 leading-relaxed whitespace-pre-wrap">{{ contacts.description }}</p>
        </div>
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
            Контакты
          </h3>
          <ul class="space-y-2 text-sm">
            <li class="flex items-center gap-2 text-gray-300"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg><span>{{ contacts.address }}</span></li>
            <li class="flex items-center gap-2 text-gray-300"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg><a :href="`tel:${contacts.phone}`" class="text-gray-300 hover:text-blue-400 transition">{{ contacts.phone }}</a></li>
            <li class="flex items-center gap-2 text-gray-300"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg><a :href="`mailto:${contacts.email}`" class="text-gray-300 hover:text-blue-400 transition">{{ contacts.email }}</a></li>
            <li class="flex items-center gap-2 text-gray-300"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg><span>{{ contacts.work_hours }}</span></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-lg font-semibold mb-3 flex items-center gap-2">
            <svg class="w-6 h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
            Разделы
          </h3>
          <ul class="space-y-2 text-sm">
            <li><NuxtLink to="/events" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/></svg>Афиша</NuxtLink></li>
            <li><NuxtLink to="/posts" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg>Публикации</NuxtLink></li>
            <li><NuxtLink to="/gallery" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>Галерея</NuxtLink></li>
            <li><NuxtLink to="/authors" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>Авторы</NuxtLink></li>
            <li><NuxtLink to="/contacts" class="flex items-center gap-2 text-gray-300 hover:text-blue-400 transition"><svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>Контакты</NuxtLink></li>
            <li v-if="authStore.isEditor"><NuxtLink to="/settings" class="flex items-center gap-2 text-yellow-400 hover:text-yellow-300 transition"><svg class="w-4 h-4 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>Настройки</NuxtLink></li>
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
    if (res.ok) contacts.value = await res.json()
  } catch (e) { console.error('Ошибка загрузки контактов:', e) } finally { contactsLoading.value = false }
}

onMounted(async () => { await loadContacts(); window.addEventListener('contacts-updated', loadContacts) })
onUnmounted(() => { window.removeEventListener('contacts-updated', loadContacts) })
</script>

<style scoped>
.app-footer { background-color: #111827 !important; padding-top: 40px !important; padding-bottom: 40px !important; }
.app-footer, .app-footer * { color: #d1d5db !important; }
.app-footer h3 { color: #ffffff !important; }
.app-footer a { color: #d1d5db !important; }
.app-footer a:hover { color: #60a5fa !important; }
:where(.dark) .app-footer { background-color: #111827 !important; }
:where(.dark) .app-footer, :where(.dark) .app-footer * { color: #d1d5db !important; }
:where(.dark) .app-footer h3 { color: #ffffff !important; }
:where(.dark) .app-footer a { color: #d1d5db !important; }
:where(.dark) .app-footer a:hover { color: #60a5fa !important; }
</style>
```

---

#### `frontend/components/layout/AppLogo.vue`

```vue
<!-- frontend/components/layout/AppLogo.vue -->
<template>
  <NuxtLink to="/" class="flex items-center gap-2 text-xl font-bold text-gray-800 dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
    <svg class="w-8 h-8 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21H5a2 2 0 01-2-2V5a2 2 0 012-2h11l5 5v11a2 2 0 01-2 2z"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 21v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4"/>
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v4a2 2 0 002 2h2a2 2 0 002-2V3"/>
    </svg>
    <span class="hidden sm:inline">Центр Культуры</span>
    <span class="sm:hidden">ЦК</span>
  </NuxtLink>
</template>
```

---

#### `frontend/components/common/BurgerMenu.vue`

```vue
<!-- frontend/components/common/BurgerMenu.vue -->
<template>
  <div class="relative" ref="menuRef">
    <button @click="toggleMenu" class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition text-gray-600 dark:text-gray-300 focus:outline-none" aria-label="Меню">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </button>
    <div v-if="isMenuOpen" class="absolute right-0 top-full mt-2 w-64 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50" @click.stop>
      <div v-if="authStore.isAuthenticated" class="px-4 py-3 border-b border-gray-100 dark:border-gray-700">
        <div class="flex items-center gap-3">
          <img v-if="authStore.user?.avatar_url" :src="authStore.user?.avatar_url" :alt="displayName" class="w-10 h-10 rounded-full object-cover">
          <div v-else class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-sm font-bold">{{ authStore.initials }}</div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-semibold text-gray-800 dark:text-gray-200 truncate">{{ displayName }}</p>
            <p class="text-xs text-gray-500 dark:text-gray-400 truncate">{{ authStore.user?.role_display || 'Пользователь' }}</p>
          </div>
        </div>
      </div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Навигация</div>
      <NuxtLink to="/" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
        </svg>
        Главная
      </NuxtLink>
      <NuxtLink to="/events" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
        </svg>
        Афиша
      </NuxtLink>
      <NuxtLink to="/posts" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        Публикации
      </NuxtLink>
      <NuxtLink to="/gallery" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
        Галерея
      </NuxtLink>
      <NuxtLink to="/authors" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
        </svg>
        Авторы
      </NuxtLink>
      <NuxtLink to="/contacts" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
        </svg>
        Контакты
      </NuxtLink>
      <div v-if="authStore.isEditor" class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div v-if="authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Управление</div>
      <NuxtLink v-if="authStore.isEditor" to="/settings" class="flex items-center gap-3 px-4 py-2.5 text-sm text-yellow-600 dark:text-yellow-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-yellow-500 dark:text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
        </svg>
        Настройки сайта
      </NuxtLink>
      <div class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Аккаунт</div>
      <template v-if="authStore.isAuthenticated">
        <NuxtLink to="/profile" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
          <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
          Мой профиль
        </NuxtLink>
        <button @click="handleLogout" class="flex items-center gap-3 px-4 py-2.5 text-sm text-red-500 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition w-full text-left">
          <svg class="w-5 h-5 text-red-400 dark:text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4 4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
          </svg>
          Выйти
        </button>
      </template>
      <template v-else>
        <NuxtLink to="/auth/login" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
          <svg class="w-5 h-5 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
          </svg>
          Войти
        </NuxtLink>
        <NuxtLink to="/auth/register" class="flex items-center gap-3 px-4 py-2.5 text-sm text-blue-600 dark:text-blue-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
          <svg class="w-5 h-5 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
          </svg>
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
const displayName = computed(() => authStore.fullName || authStore.username)

const toggleMenu = () => { isMenuOpen.value = !isMenuOpen.value }
const closeMenu = () => { isMenuOpen.value = false }
const handleLogout = () => { authStore.logout(); closeMenu(); navigateTo('/') }
const handleClickOutside = (event) => { if (menuRef.value && !menuRef.value.contains(event.target)) isMenuOpen.value = false }

onMounted(() => { document.addEventListener('click', handleClickOutside) })
onUnmounted(() => { document.removeEventListener('click', handleClickOutside) })
</script>
```

---

#### `frontend/components/common/ThemeToggle.vue`

```vue
<!-- frontend/components/common/ThemeToggle.vue -->
<template>
  <button @click="toggleTheme" class="p-2.5 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-700 transition-all duration-300 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white hover:shadow-md" :title="themeStore.darkMode ? 'Светлая тема' : 'Тёмная тема'" aria-label="Переключить тему">
    <svg v-if="themeStore.darkMode" class="w-5 h-5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>
    </svg>
    <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>
    </svg>
  </button>
</template>

<script setup>
import { useThemeStore } from '~/store/theme'
const themeStore = useThemeStore()
const toggleTheme = () => { themeStore.toggleTheme() }
</script>
```

---

#### `frontend/components/common/AuthButtons.vue`

```vue
<!-- frontend/components/common/AuthButtons.vue -->
<template>
  <div class="flex items-center gap-3">
    <template v-if="authStore.isAuthenticated">
      <NuxtLink to="/profile" class="hidden md:flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition font-medium group">
        <img v-if="authStore.user?.avatar_url" :src="authStore.user?.avatar_url" :alt="displayName" class="w-8 h-8 rounded-full object-cover border-2 border-blue-200 dark:border-blue-800 group-hover:border-blue-400 dark:group-hover:border-blue-600 transition">
        <div v-else class="w-8 h-8 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-xs font-bold">{{ authStore.initials }}</div>
        <div class="flex flex-col leading-tight">
          <span class="font-medium text-gray-700 dark:text-gray-300">{{ displayName }}</span>
          <span class="text-xs text-gray-400 dark:text-gray-500">{{ roleDisplay }}</span>
        </div>
        <svg class="w-3 h-3 text-gray-400 dark:text-gray-500 group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </NuxtLink>
    </template>
    <template v-else>
      <NuxtLink to="/auth/login">
        <button class="inline-flex items-center gap-1.5 px-4 py-2 bg-transparent border-2 border-blue-500 text-blue-600 dark:text-blue-400 rounded-xl hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:border-blue-600 dark:hover:border-blue-300 transition-all duration-300 text-sm font-medium hover:-translate-y-0.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/>
          </svg>
          Войти
        </button>
      </NuxtLink>
      <NuxtLink to="/auth/register">
        <button class="inline-flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 text-sm font-medium shadow-blue-500/25 hover:shadow-lg hover:shadow-blue-500/40 hover:-translate-y-0.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
          </svg>
          Регистрация
        </button>
      </NuxtLink>
    </template>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'
const authStore = useAuthStore()

const displayName = computed(() => authStore.fullName || authStore.username)
const roleDisplay = computed(() => {
  if (!authStore.user) return ''
  const roleMap = { 'admin': 'Администратор', 'editor': 'Главный редактор', 'author': 'Автор', 'subscriber': 'Подписчик' }
  return roleMap[authStore.user.role] || authStore.user.role_display || 'Пользователь'
})
</script>
```

---

#### `frontend/components/common/CreateMenu.vue`

```vue
<!-- frontend/components/common/CreateMenu.vue -->
<template>
  <div v-if="canCreate" class="relative" ref="menuRef">
    <button @click="toggleMenu" class="flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-violet-500 to-purple-600 text-white rounded-xl hover:from-violet-600 hover:to-purple-700 transition-all duration-300 text-sm font-medium shadow-md shadow-violet-500/25 hover:shadow-lg hover:shadow-violet-500/40 hover:-translate-y-0.5" aria-label="Создать">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
      </svg>
      <span class="hidden sm:inline">Создать</span>
      <svg class="w-4 h-4 transition-transform duration-300 ml-1" :class="isMenuOpen ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>
    <div v-if="isMenuOpen" class="absolute right-0 top-full mt-2 w-56 bg-white dark:bg-gray-800 rounded-lg shadow-xl border border-gray-200 dark:border-gray-700 py-2 z-50" @click.stop>
      <div v-if="authStore.isAuthor || authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Контент</div>
      <NuxtLink v-if="authStore.isAuthor || authStore.isEditor" to="/posts/create" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-green-500 dark:text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        Новый пост
      </NuxtLink>
      <NuxtLink v-if="authStore.isEditor" to="/events/create" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-blue-500 dark:text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 5v2m0 4v2m0 4v2M5 5a2 2 0 00-2 2v3a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2H5zM3 19a2 2 0 002 2h14a2 2 0 002-2v-3a2 2 0 00-2-2H5a2 2 0 00-2 2v3z"/>
        </svg>
        Новое событие
      </NuxtLink>
      <div v-if="authStore.isEditor" class="border-t border-gray-200 dark:border-gray-700 my-1"></div>
      <div v-if="authStore.isEditor" class="px-3 py-1.5 text-xs font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Галерея</div>
      <NuxtLink v-if="authStore.isEditor" to="/gallery/create" class="flex items-center gap-3 px-4 py-2.5 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 transition" @click="closeMenu">
        <svg class="w-5 h-5 text-pink-500 dark:text-pink-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
        </svg>
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
const canCreate = computed(() => authStore.isAuthor || authStore.isEditor)

const toggleMenu = () => { isMenuOpen.value = !isMenuOpen.value }
const closeMenu = () => { isMenuOpen.value = false }
const handleClickOutside = (event) => { if (menuRef.value && !menuRef.value.contains(event.target)) isMenuOpen.value = false }

onMounted(() => { document.addEventListener('click', handleClickOutside) })
onUnmounted(() => { document.removeEventListener('click', handleClickOutside) })
</script>
```

---

#### `frontend/components/common/Breadcrumbs.vue`

```vue
<!-- frontend/components/common/Breadcrumbs.vue -->
<template>
  <nav class="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400" aria-label="Хлебные крошки">
    <NuxtLink to="/" class="flex items-center gap-1.5 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>
      </svg>
      <span class="hidden sm:inline">Главная</span>
    </NuxtLink>
    <template v-if="items && items.length > 0">
      <template v-for="(item, index) in items" :key="index">
        <svg v-if="index === 0" class="w-4 h-4 flex-shrink-0 text-gray-400 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
        <NuxtLink v-if="item.to" :to="item.to" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors truncate">{{ item.label }}</NuxtLink>
        <span v-else class="truncate">{{ item.label }}</span>
        <svg v-if="index < items.length - 1 || (index === items.length - 1 && currentPageName)" class="w-4 h-4 flex-shrink-0 text-gray-400 dark:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </template>
    </template>
    <span v-if="currentPageName" class="text-gray-700 dark:text-gray-300 font-medium truncate">{{ currentPageName }}</span>
  </nav>
</template>

<script setup>
const props = defineProps({ items: { type: Array, default: () => [] }, currentPageName: { type: String, default: '' } })
</script>
```

---

#### `frontend/components/CommentItem.vue`

```vue
<!-- frontend/components/CommentItem.vue -->
<template>
  <div class="comment-item py-4 border-b border-gray-100 dark:border-gray-700 last:border-0">
    <div class="flex gap-3">
      <NuxtLink :to="`/authors/${comment.author_id || 0}`" class="flex-shrink-0">
        <img v-if="comment.author_avatar" :src="comment.author_avatar" :alt="getAuthorFullName(comment)" class="w-10 h-10 rounded-full object-cover"/>
        <div v-else class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-white text-sm font-bold">{{ getInitials(getAuthorFullName(comment)) }}</div>
      </NuxtLink>
      <div class="flex-1 min-w-0">
        <div class="flex items-center gap-2 flex-wrap">
          <NuxtLink :to="`/authors/${comment.author_id || 0}`" class="font-semibold text-gray-800 dark:text-gray-200 hover:text-blue-600 dark:hover:text-blue-400 transition">{{ getAuthorFullName(comment) }}</NuxtLink>
          <span class="text-xs text-gray-400 dark:text-gray-500">{{ formatDate(comment.created_at) }}</span>
          <span v-if="comment.updated_at !== comment.created_at" class="text-xs text-gray-400 dark:text-gray-500">(изменено)</span>
        </div>
        <div v-if="editingId === comment.id" class="mt-2">
          <textarea v-model="editContent" class="w-full border border-gray-300 dark:border-gray-600 rounded-lg p-2 resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200" rows="3"></textarea>
          <div class="flex gap-2 mt-2">
            <button @click="saveEdit" :disabled="savingEdit" class="px-3 py-1.5 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition text-sm">{{ savingEdit ? 'Сохранение...' : 'Сохранить' }}</button>
            <button @click="cancelEdit" class="px-3 py-1.5 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition text-sm">Отмена</button>
          </div>
        </div>
        <p v-else class="text-gray-700 dark:text-gray-300 mt-1 leading-relaxed break-words">{{ comment.content }}</p>
        <div class="flex items-center gap-4 mt-2 text-xs">
          <button v-if="authStore.isAuthenticated" @click="toggleLike" class="flex items-center gap-1 text-gray-400 dark:text-gray-500 hover:text-red-500 dark:hover:text-red-400 transition">
            <svg class="w-4 h-4 transition" :class="comment.user_has_liked ? 'text-red-500 fill-red-500' : 'fill-none'" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span>{{ comment.likes_count || 0 }}</span>
          </button>
          <span v-else class="flex items-center gap-1 text-gray-400 dark:text-gray-500">
            <svg class="w-4 h-4 fill-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span>{{ comment.likes_count || 0 }}</span>
          </span>
          <button v-if="authStore.isAuthenticated" @click="startReply" class="text-gray-400 dark:text-gray-500 hover:text-blue-600 dark:hover:text-blue-400 transition">Ответить</button>
          <button v-if="comment.can_edit" @click="startEdit" class="text-gray-400 dark:text-gray-500 hover:text-blue-600 dark:hover:text-blue-400 transition">Редактировать</button>
          <button v-if="comment.can_delete" @click="deleteComment" class="text-gray-400 dark:text-gray-500 hover:text-red-600 dark:hover:text-red-400 transition">Удалить</button>
        </div>
        <div v-if="comment.replies && comment.replies.length > 0" class="mt-4 pl-4 border-l-2 border-gray-200 dark:border-gray-700 space-y-4">
          <CommentItem v-for="reply in comment.replies" :key="reply.id" :comment="reply" :editing-id="editingId" :saving-edit="savingEdit"
            @start-edit="startEdit" @start-reply="startReply" @save-edit="saveEdit" @cancel-edit="cancelEdit" @delete-comment="deleteComment" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '~/store/auth'

const authStore = useAuthStore()
const props = defineProps({ comment: { type: Object, required: true }, editingId: { type: Number, default: null }, savingEdit: { type: Boolean, default: false } })
const emit = defineEmits(['start-edit', 'start-reply', 'save-edit', 'cancel-edit', 'delete-comment'])

const config = useRuntimeConfig()
const API_URL = config.public.apiBase || 'http://127.0.0.1:8000/api'
const editContent = ref('')

const getAuthorFullName = (comment) => {
  if (!comment) return 'Пользователь'
  if (comment.author_first_name || comment.author_last_name) {
    const parts = []
    if (comment.author_last_name) parts.push(comment.author_last_name)
    if (comment.author_first_name) parts.push(comment.author_first_name)
    if (parts.length > 0) return parts.join(' ')
  }
  if (comment.author_full_name) return comment.author_full_name
  return comment.author_name || 'Пользователь'
}

const getInitials = (name) => {
  if (!name) return '?'
  const parts = name.split(' ')
  if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase()
  return name.substring(0, 2).toUpperCase()
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
}

const startReply = () => emit('start-reply', props.comment.id, getAuthorFullName(props.comment))
const startEdit = () => { editContent.value = props.comment.content; emit('start-edit', props.comment) }
const cancelEdit = () => { editContent.value = ''; emit('cancel-edit') }
const saveEdit = () => { if (!editContent.value.trim()) return; emit('save-edit', props.comment.id, editContent.value.trim()) }
const deleteComment = () => emit('delete-comment', props.comment.id)

const toggleLike = async () => {
  if (!authStore.isAuthenticated) return
  try {
    const res = await fetch(`${API_URL}/likes/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${authStore.accessToken}` },
      body: JSON.stringify({ comment: props.comment.id })
    })
    if (res.ok) {
      const data = await res.json()
      if (data.action === 'liked') { props.comment.likes_count = (props.comment.likes_count || 0) + 1; props.comment.user_has_liked = true }
      else if (data.action === 'unliked') { props.comment.likes_count = (props.comment.likes_count || 0) - 1; props.comment.user_has_liked = false }
    }
  } catch (e) { console.error('Ошибка:', e) }
}
</script>
```

---
