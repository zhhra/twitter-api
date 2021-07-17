from django.urls import path
from .views.signup import Signup
from .views.account_info import AccountInfo
from .views.otp_validation import OtpValidation
from .views.follow_unfollow import follow_unfollow
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "auth"
urlpatterns = [
    path("info/api/<int:pk>", AccountInfo.as_view(), name="info"),
    path("follow_unfollow/api/<int:pk>", follow_unfollow, name="follow_unfollow"),
    path("signup/api", Signup.as_view(), name="signup"),
    path("signin/api", TokenObtainPairView.as_view(), name="signin"),
    path("signin/api/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("verification/api", OtpValidation.as_view(), name="email_verification"),
]
