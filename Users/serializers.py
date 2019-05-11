import re
from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from DinDonBackend.settings import REGEX_MOBILE
from Users.models import User, VerifyCode


class VerifyCodeSerializer(Serializer):
    phone_num = serializers.CharField(
        required=True,
        min_length=11,
        max_length=11,
        help_text="用户手机号码",
        error_messages={
            'required': "必须填写手机号",
            'min_length': "手机号格式错误",
            'max_length': "手机号格式错误",
        }
    )

    def validate_phone_num(self, phone_num):
        """
        验证手机号
        :param phone_num:
        :return phone_num:
        """
        if User.objects.filter(phone_number=phone_num):
            raise serializers.ValidationError("该手机号已注册")

        if not re.match(REGEX_MOBILE, phone_num):
            raise serializers.ValidationError("手机号格式错误")

        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, phone_num=phone_num).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return phone_num


class UserRegisterSerializer(ModelSerializer):
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
    code = serializers.CharField(
        required=True,
        min_length=4,
        max_length=4,
        help_text="验证码",
        write_only=True,
        error_messages={
            'required': "必须填写验证码",
            'blank': "必须填写验证码",
            'min_length': "验证码格式错误",
            'max_length': "验证码格式错误"
        }
    )

    password = serializers.CharField(
        required=True,
        max_length=64,
        help_text="密码",
        write_only=True,
        error_messages={
            "blank": "必须填写密码",
            "required": "必须填写密码",
            "max_length": "密码太长",
        }
    )

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number):
            raise serializers.ValidationError("该手机号已注册")

    def validate_code(self, code):

        verify_records = VerifyCode.objects.filter(phone_num=self.initial_data["phone_number"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
        else:
            raise serializers.ValidationError("验证码错误")

        five_minutes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
        if five_minutes_ago > last_record.add_time:
            raise serializers.ValidationError("验证码已过期")

        if last_record.code != code:
            raise serializers.ValidationError("验证码错误")

        return code

    def validate(self, attrs):
        attrs['username'] = "user" + attrs['phone_number']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('phone_number', 'code', 'password')

    # def save(self, **kwargs):
