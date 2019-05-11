from django.db import models
from Dishes.models import Dish
from Tables.models import Table
from Users.models import User


class OrderStatus:
    Canceled = 0
    Ordered = 1
    Payed = 2
    Processing = 3
    Finished = 4
    Confirmed = 5

    OrderStatusChoices = (
        (0, "已取消"),
        (1, "已下单"),
        (2, "已支付"),
        (3, "处理中"),
        (4, "已完成"),
        (5, "已确认"),
    )

    @staticmethod
    def status(status_code):
        return (
            '已取消',
            '已下单',
            '已支付',
            '处理中',
            '已完成',
            '已确认',
        )[status_code]


class Order(models.Model):
    orderId = models.AutoField(primary_key=True, verbose_name="订单编号")

    orderUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订单用户")

    orderTable = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="订单餐桌")

    orderTime = models.DateTimeField(verbose_name="下单时间", auto_now_add=True)

    orderPayTime = models.DateTimeField(verbose_name="付款时间")

    orderProcessTime = models.DateTimeField(verbose_name="处理时间")

    orderFinishTime = models.DateTimeField(verbose_name="完成时间")

    orderConfirmTime = models.DateTimeField(verbose_name="确认时间")

    orderPrice = models.FloatField(verbose_name="订单金额")

    orderScript = models.TextField(verbose_name="订单留言", null=True)

    orderStatus = models.IntegerField(verbose_name="订单状态", choices=OrderStatus.OrderStatusChoices)

    orderDishes = models.ManyToManyField(Dish, verbose_name="订单菜品", through="OrderDish")

    def __str__(self):
        description = "订单编号:{}\n".format(self.orderId)
        return description

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单编号")

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="菜品")

    dishNum = models.IntegerField(verbose_name="下单数量")
