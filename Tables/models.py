from django.db import models

from Users.models import User


class TableType:
    BigTable = 0
    MiddleTable = 1
    SmallTable = 2

    TypeChoice = (
        (0, "大桌"),
        (1, "中桌"),
        (2, "小桌")
    )

    @staticmethod
    def type(type_id):
        return ["大桌", '中桌', '小桌'][type_id]


class TableState:
    Free = 0
    Used = 1

    StateChoice = (
        (0, "空闲"),
        (1, "占用"),
    )


# Create your models here.
class DiningTable(models.Model):
    tableId = models.AutoField(primary_key=True, verbose_name="餐桌编号")

    tableCategory = models.IntegerField(verbose_name="餐桌类别",
                                        choices=TableType.TypeChoice,
                                        default=1
                                        )

    tableState = models.IntegerField(verbose_name="餐桌状态",
                                     choices=TableState.StateChoice,
                                     default=0
                                     )

    bookUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="预定用户")

    bookTime = models.DateTimeField(null=True, blank=True, verbose_name="预定时间")

    def __str__(self):
        description = "餐桌编号:{} 餐桌类别:{}".format(self.tableId, TableType.type(self.tableCategory))
        return description

    class Meta:
        verbose_name = "餐桌"
        verbose_name_plural = verbose_name
