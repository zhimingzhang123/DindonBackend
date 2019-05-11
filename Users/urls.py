from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Users.views import VerifyCodeAPIView, UserRegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('code/', VerifyCodeAPIView.as_view(), name="code"),
    path('register/', UserRegisterView.as_view(), name="code"),
]
