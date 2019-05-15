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
    order_id = models.AutoField(verbose_name="订单编号", primary_key=True)

    order_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订单用户")

    order_table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="订单餐桌")

    order_script = models.TextField(verbose_name="订单留言", null=True)

    table_ware_num = models.IntegerField(verbose_name="餐具份数")

    def __str__(self):
        description = "编号:{}".format(self.order_id)
        return description

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单编号", on_delete=models.CASCADE, related_name='order_detail')

    dish_id = models.IntegerField(verbose_name="菜品编号")

    dish_name = models.CharField(verbose_name="菜品名称", max_length=128)

    dish_price = models.FloatField(verbose_name="菜品价格")

    dish_picture = models.TextField(verbose_name="菜品图片", null=True, blank=True)

    dish_description = models.TextField(verbose_name="菜品描述", null=True, blank=True)

    dish_num = models.IntegerField(verbose_name="菜品数量")

    created_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    def __str__(self):
        return "订单{}详情".format(self.order_id)

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name


class Transaction(models.Model):
    order = models.ForeignKey(Order, related_name="transaction", verbose_name="订单编号", on_delete=models.CASCADE)
    order_time = models.DateTimeField(verbose_name="下单时间", auto_now_add=True)
    order_price = models.FloatField(verbose_name="订单金额")
    PAY_CHOICES = (
        (0, "支付宝"),
        (1, '微信支付')
    )
    pay_method = models.IntegerField(choices=PAY_CHOICES, verbose_name="支付方式")
    order_pay_time = models.DateTimeField(verbose_name="付款时间", null=True, blank=True)
    order_process_time = models.DateTimeField(verbose_name="处理时间", null=True, blank=True)
    order_finish_time = models.DateTimeField(verbose_name="完成时间", null=True, blank=True)
    order_confirm_time = models.DateTimeField(verbose_name="确认时间", null=True, blank=True)
    order_status = models.IntegerField(verbose_name="订单状态",
                                       choices=OrderStatus.OrderStatusChoices,
                                       default=OrderStatus.Ordered)
    check_info = models.TextField(null=True, blank=True, verbose_name="发票信息")
    trade_info = models.TextField(null=True, blank=True, verbose_name='交易信息')
