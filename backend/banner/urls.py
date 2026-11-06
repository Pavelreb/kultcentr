from django.urls import path
from .views import BannerView, BannerUpdateView

urlpatterns = [
    path("", BannerView.as_view(), name="banner"),
    path("update/", BannerUpdateView.as_view(), name="banner_update"),
]
