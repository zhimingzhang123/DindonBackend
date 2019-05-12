import re
from datetime import datetime, timedelta

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from DinDonBackend.settings import REGEX_PHONE
from Users.models import User, VerifyCode


class SmsCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        required=True,
        min_length=11,
        max_length=11,
        help_text="用户手机号码",
        error_messages={
            'required': "必须填写手机号",
            'min_length': "手机号格式错误",
            'max_length': "手机号格式错误",
            'blank': "手机号不能为空"
        }
    )
    is_register = serializers.BooleanField()

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        is_register = attrs['is_register']

        # 验证手机号是否合法
        if not re.match(REGEX_PHONE, phone_number):
            raise serializers.ValidationError("手机号格式错误")

        user_count = User.objects.filter(phone_number=phone_number).count()
        if not user_count and not is_register:
            raise serializers.ValidationError('该手机号未进行注册')
        elif user_count and is_register:
            raise serializers.ValidationError('该手机号已经被注册')

        # 设置60秒内不能重复发送验证码
        one_minute_ago = datetime.now() - timedelta(minutes=1)
        query = VerifyCode.objects.filter(phone_number=phone_number, add_time__gt=one_minute_ago,
                                          is_register=is_register).order_by('-add_time')
        if query.count():
            raise serializers.ValidationError('两次发送短信时间间隔小于60秒')

        return attrs


class LoginWithSmsCodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=6, min_length=6, write_only=True)
    phone_number = serializers.CharField(max_length=11, min_length=11, write_only=True)

    def validate(self, attrs):
        super().validate(attrs)

        phone_number = attrs['phone_number']
        code = attrs.pop('code')
        # 验证码5分钟内有效
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        query = VerifyCode.objects.filter(add_time__gt=five_minutes_ago, phone_number=phone_number,
                                          is_register=False).order_by(
            '-add_time')
        if not query or query.first().code != code:
            raise serializers.ValidationError('验证码错误')

        attrs['username'] = phone_number
        del code
        return attrs

    class Meta:
        model = User
        fields = ('phone_number', 'code')


class LoginWithPhonePasswordSerializer(TokenObtainPairSerializer):
    username_field = 'phone_number'

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        user_obj = User.objects.filter(phone_number=phone_number).first()
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
                raise AuthenticationFailed(
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

    phone_number = serializers.CharField(required=True, allow_blank=False,
                                         validators=[UniqueValidator(queryset=User.objects.all(), message="手机号已经存在")], write_only=True)

    def validate(self, attrs):
        super().validate(attrs)

        phone_number = attrs['phone_number']
        attrs['username'] = phone_number
        code = attrs.pop('code')

        # 验证码5分钟内有效
        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        query = VerifyCode.objects.filter(add_time__gt=five_minutes_ago, phone_number=phone_number, is_register=True)
        if query:
            if query.first().code != code:
                raise serializers.ValidationError('验证码错误')

        del code
        return attrs

    class Meta:
        model = User
        fields = ('password', 'phone_number', 'code',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
