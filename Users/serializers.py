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
        if User.objects.filter(user_phone_number=phone_num):
            raise serializers.ValidationError("该手机号已注册")

        # if not re.match(REGEX_MOBILE, phone_num):
        #     raise serializers.ValidationError("手机号格式错误")

        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, phone_num=phone_num).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return phone_num


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
