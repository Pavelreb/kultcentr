from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterView,
    UserDetailView,
    UserListView,
    SubscribeView,
    CurrentUserView,
    CurrentUserUpdateView,
    ChangePasswordView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("users/<int:pk>/subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("users/me/", CurrentUserView.as_view(), name="current_user"),
    path(
        "users/me/update/", CurrentUserUpdateView.as_view(), name="current_user_update"
    ),
    path(
        "users/me/change-password/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path("password-reset/", PasswordResetRequestView.as_view(), name="password_reset"),
    path(
        "password-reset/<str:uidb64>/<str:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
