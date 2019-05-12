from django.db import models


# Create your models here.
class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True, verbose_name="菜品编号")

    dish_name = models.CharField(max_length=50, verbose_name="菜品名称")

    dish_price = models.FloatField(verbose_name="菜品价格")

    dish_type = models.CharField(verbose_name="菜品分类", max_length=30, null=True)

    dish_stock = models.IntegerField(verbose_name="菜品库存", default=999)

    dish_picture = models.TextField(verbose_name="菜品图片", null=True)

    dish_description = models.TextField(verbose_name="菜品描述", null=True)

    dish_add_time = models.DateTimeField(verbose_name="菜品添加时间", auto_now_add=True, null=True)

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name = "菜品"
        verbose_name_plural = "菜品"
