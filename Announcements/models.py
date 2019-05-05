from django.db import models

# Create your models here.
from Users.models import User


class Announcement(models.Model):
    announcementId = models.AutoField(verbose_name="公告编号", primary_key=True)

    announcementContent = models.TextField(verbose_name="公告内容", null=True)

    announcementPublishTime = models.DateTimeField(auto_now_add=True, verbose_name="公告发布时间")

    announcementModifyTime = models.DateTimeField(auto_now=True, verbose_name="公告修改时间")

    announcementModifyUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        description = "公告编号:{}\n".format(self.announcementId)
        return description
