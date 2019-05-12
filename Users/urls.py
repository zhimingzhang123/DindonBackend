from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Users.views import SmsCodeView, LoginWithSmsCodeView, UserRegisterView
from Users.serializers import LoginWithPhonePasswordSerializer

urlpatterns = [
    # 用于手机号、密码登录
    path('loginpasswd/', TokenObtainPairView.as_view(serializer_class=LoginWithPhonePasswordSerializer), name='loginpasswd'),
    # 用于短信验证码登录
    path('loginsmscode/', LoginWithSmsCodeView.as_view(), name='loginsmscode'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    # 发送短信验证码
    path('smscode/', SmsCodeView.as_view(), name='smscode'),
    # 用户注册
    path('register/', UserRegisterView.as_view(), name='register')
]
