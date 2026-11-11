from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from config.media_serve import serve_media_range

urlpatterns = [
    path("admin/", admin.site.urls),
    # Комментарии к постам - идут первыми
    path("api/", include("comments.urls")),
    # Остальные API
    path("api/", include("gallery.urls")),
    path("api/", include("posts.urls")),
    path("api/", include("events.urls")),
    path("api/", include("likes.urls")),
    path("api/auth/", include("users.urls")),
    path("api/contact-info/", include("contactinfo.urls")),
    path("api/banner/", include("banner.urls")),
    path("api/about/", include("about.urls")),
    path("api/", include("feedback.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/medialib/", include("medialib.urls")),
]

if settings.DEBUG:
    # Раздача медиа с поддержкой Range (перемотка видео/аудио в браузере)
    urlpatterns += [
        path(settings.MEDIA_URL.lstrip("/") + "<path:path>", serve_media_range)
    ]
