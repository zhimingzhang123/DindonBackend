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
    order_id = models.AutoField(primary_key=True, verbose_name="订单编号")

    order_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订单用户")

    order_table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="订单餐桌")

    order_time = models.DateTimeField(verbose_name="下单时间", auto_now_add=True)

    order_pay_time = models.DateTimeField(verbose_name="付款时间", null=True, blank=True)

    order_process_time = models.DateTimeField(verbose_name="处理时间", null=True, blank=True)

    order_finish_time = models.DateTimeField(verbose_name="完成时间", null=True, blank=True)

    order_confirm_time = models.DateTimeField(verbose_name="确认时间", null=True, blank=True)

    order_price = models.FloatField(verbose_name="订单金额")

    order_script = models.TextField(verbose_name="订单留言", null=True)

    order_status = models.IntegerField(verbose_name="订单状态", choices=OrderStatus.OrderStatusChoices)

    order_dishes = models.ManyToManyField(Dish, verbose_name="订单菜品", through="OrderDish")

    PAY_CHOICES = (
        (0, "支付宝"),
        (1, '微信支付')
    )

    pay_method = models.IntegerField(choices=PAY_CHOICES, verbose_name="支付方式")

    table_ware_num = models.IntegerField(verbose_name="餐具份数")

    check_info = models.TextField(null=True, blank=True, verbose_name="发票信息")

    trade_info = models.TextField(null=True, blank=True, verbose_name='交易信息')

    def __str__(self):
        description = "订单编号:{}\n".format(self.order_id)
        return description

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单编号")

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="菜品")

    dish_num = models.IntegerField(verbose_name="点餐数量")
