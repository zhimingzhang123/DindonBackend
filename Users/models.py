from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class UserType:
    Customer = 1
    Manager = 2
    Chef = 3
    Waiter = 4


# Create your models here.
class User(AbstractBaseUser):
    userId = models.AutoField(primary_key=True, verbose_name="用户编号")

    userName = models.CharField(max_length=64, verbose_name="用户名")

    userPhoneNumber = models.CharField(max_length=20, verbose_name="用户手机号码", unique=True)

    userCreateTime = models.DateTimeField(auto_now_add=True, null=True, verbose_name="用户创建时间")

    userType = models.IntegerField(default=UserType.Customer, verbose_name="用户类型")

    def __str__(self):
        description = "用户编号: {} 用户手机号码: {}".format(self.userId, self.userPhoneNumber)
        return description

# class VerifyCode(models.Model):
#     """
#     短信验证码
#     """
#     code = models.CharField(max_length=10, verbose_name="验证码")
#     mobile = models.CharField(max_length=11, verbose_name="电话")
#     add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name = "短信验证码"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.code