from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
