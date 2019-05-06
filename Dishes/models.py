from django.db import models


# Create your models here.
class Dish(models.Model):
    dishId = models.AutoField(primary_key=True, verbose_name="菜品编号")

    dishName = models.CharField(max_length=50, verbose_name="菜品名称")

    dishPrice = models.IntegerField(verbose_name="菜品价格")

    dishStock = models.IntegerField(verbose_name="菜品库存", default=999)

    dishPicture = models.TextField(verbose_name="菜品图片", null=True)

    dishDescription = models.TextField(verbose_name="菜品描述", null=True)

    dishAddTime = models.DateTimeField(verbose_name="菜品添加时间", auto_now_add=True, null=True)

    def __str__(self):
        description = "菜品编号: {} 菜品名称: {}".format(self.dishId, self.dishName)
        return description

    class Meta:
        verbose_name = "菜品"
        verbose_name_plural = "菜品"
