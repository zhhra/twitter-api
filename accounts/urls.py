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
    path("api/info/<int:pk>", AccountInfo.as_view(), name="info"),
    path("api/signup", Signup.as_view(), name="signup"),
    path("api/verification", OtpValidation.as_view(), name="email_verification"),
    path("api/signin", TokenObtainPairView.as_view(), name="signin"),
    path("api/signin/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/follow_unfollow/<int:pk>", follow_unfollow, name="follow_unfollow"),
]
