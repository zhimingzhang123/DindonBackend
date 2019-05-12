import re
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Users.models import User, VerifyCode


class SmsCodeSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, min_length=11, required=True)
    is_register = serializers.BooleanField()

    def validate(self, attrs):
        mobile = attrs['mobile']
        is_register = attrs['is_register']

        # 验证手机号是否合法
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('无效的手机号')

        if is_register:
            # 判断手机号是否已经注册过
            if User.objects.filter(userPhoneNumber=mobile).count():
                raise serializers.ValidationError('该手机号已经被注册')

        # 设置60秒内不能重复发送验证码
        one_minute_ago = datetime.now() - timedelta(minutes=1)
        query = VerifyCode.objects.filter(mobile=mobile, add_time__gt=one_minute_ago, is_register=is_register).order_by('-add_time')
        if query.count():
            raise serializers.ValidationError('两次发送短信时间间隔小于60秒')

        return attrs


class LoginWithSmsCodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=6, min_length=6, write_only=True)
    userPhoneNumber = serializers.CharField(max_length=11, min_length=11, write_only=True)

    def validate(self, attrs):
        super().validate(attrs)

        mobile = attrs['userPhoneNumber']
        code = attrs.pop('code')
        # 验证码5分钟内有效
        five_minutes_ago = datetime.now() - timedelta(minutes=500)
        query = VerifyCode.objects.filter(add_time__gt=five_minutes_ago, mobile=mobile, is_register=False).order_by('-add_time')
        if query:
            if query.first().code != code:
                raise serializers.ValidationError('验证码错误')

        del code
        return attrs

    class Meta:
        model = User
        fields = ('userPhoneNumber', 'code')


class LoginWithPhonePasswordSerializer(TokenObtainPairSerializer):
    username_field = 'userPhoneNumber'

    def validate(self, attrs):
        userPhoneNumber = attrs['userPhoneNumber']
        user_obj = User.objects.filter(userPhoneNumber=userPhoneNumber).first()
        if user_obj:
            authenticate_kwargs = {
                'username': user_obj.username,
                'password': attrs['password'],
            }
            try:
                authenticate_kwargs['request'] = self.context['request']
            except KeyError:
                pass

            self.user = authenticate(**authenticate_kwargs)

            if self.user is None or not self.user.is_active:
                raise exceptions.AuthenticationFailed(
                    self.error_messages['no_active_account'],
                    'no_active_account',
                )
            data = {}
            refresh = self.get_token(self.user)


            data['username'] = user_obj.username
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            return data

        else:
            raise serializers.ValidationError('username or password error')


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=6, min_length=6, write_only=True)

    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    def validate(self, attrs):
        super().validate(attrs)

        mobile = attrs['userPhoneNumber']
        code = attrs.pop('code')

        # 验证码5分钟内有效
        five_minutes_ago = datetime.now() - timedelta(minutes=500)
        query = VerifyCode.objects.filter(add_time__gt=five_minutes_ago, mobile=mobile, is_register=True)
        if query:
            if query.first().code != code:
                raise serializers.ValidationError('验证码错误')

        del code
        return attrs

    class Meta:
        model = User
        fields = ('username', 'password', 'userPhoneNumber', 'code',)
        extra_kwargs = {
            'password': {'write_only': True},
            'userPhoneNumber': {'write_only': True},
        }
