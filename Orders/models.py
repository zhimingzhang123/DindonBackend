from django.db import models

# Create your models here.
from Dishes.models import Dish
from Tables.models import DiningTable
from Users.models import User


class OrderStatus:
    Ordered = 1
    Payed = 2
    Processing = 3
    Finished = 4
    Confirmed = 5


class Order(models.Model):
    orderId = models.AutoField(primary_key=True, verbose_name="订单编号")

    orderUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订单用户")

    orderTable = models.ForeignKey(DiningTable, on_delete=models.CASCADE, verbose_name="订单餐桌")

    orderTime = models.DateTimeField(verbose_name="下单时间")

    orderPayTime = models.DateTimeField(verbose_name="付款时间")

    orderProcessTime = models.DateTimeField(verbose_name="处理时间")

    orderFinishTime = models.DateTimeField(verbose_name="完成时间")

    orderConfirmTime = models.DateTimeField(verbose_name="确认时间")

    orderPrice = models.IntegerField(verbose_name="订单金额")

    orderStatus = models.IntegerField(verbose_name="订单状态", default=OrderStatus.Ordered)

    orderDishes = models.ManyToManyField(Dish, verbose_name="订单菜品", through="OrderDish")

    def __str__(self):
        description = "订单编号:{}\n".format(self.orderId)
        return description


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单编号")

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="菜品")

    dishNum = models.IntegerField(verbose_name="下单数量")
