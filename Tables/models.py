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


class Table(models.Model):
    table_id = models.AutoField(primary_key=True, verbose_name="餐桌编号")

    table_category = models.IntegerField(verbose_name="餐桌类别",
                                         choices=TableType.TypeChoice,
                                         default=TableType.MiddleTable
                                         )

    table_state = models.IntegerField(verbose_name="餐桌状态",
                                      choices=TableState.StateChoice,
                                      default=0
                                      )

    def __str__(self):
        description = "餐桌{}{}".format(self.table_id, TableType.type(self.table_category))
        return description

    class Meta:
        verbose_name = "餐桌"
        verbose_name_plural = verbose_name


class BookTime(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="餐桌", related_name="table")

    book_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="顾客", related_name="book_user")

    book_date = models.DateField(verbose_name="预定日期")

    time_choices = (
        (0, "上午"),
        (1, "中午"),
        (2, "下午"),
        (3, "晚上"),
    )

    book_time = models.IntegerField(verbose_name="预定时间段", choices=time_choices)

    class Meta:
        verbose_name = "餐桌预定记录"
        verbose_name_plural = verbose_name
