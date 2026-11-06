from django.urls import path
from .views import ContactInfoView, ContactInfoUpdateView

urlpatterns = [
    path("", ContactInfoView.as_view(), name="contact_info"),
    path("update/", ContactInfoUpdateView.as_view(), name="contact_info_update"),
]
