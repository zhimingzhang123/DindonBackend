from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Users.views import SmsCodeView, LoginWithSmsCodeView, UserRegisterView, UserChangePasswordView
from Users.serializers import LoginWithPhonePasswordSerializer

from Users.views import UserRegisterView

urlpatterns = [
    path('login/password/', TokenObtainPairView.as_view(serializer_class=LoginWithPhonePasswordSerializer),
         name='login_password'),
    path('login/code/', LoginWithSmsCodeView.as_view(), name='login_smscode'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    # 发送短信验证码
    path('code/', SmsCodeView.as_view(), name='code'),
    # 用户注册
    path('register/', UserRegisterView.as_view(), name='register'),
    # 修改密码
    re_path(r'changepassword/(?P<pk>\d+)/', UserChangePasswordView.as_view(), name='change_password')
]
