from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("password-change", views.ChangePasswordAPIView.as_view(), name="change_password_api", ),
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token_login_api"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token_logout_api"),
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair", ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("user/profile/", views.ProfileApiView.as_view(), name="profile"),
]
