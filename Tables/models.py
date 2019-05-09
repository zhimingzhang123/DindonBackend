from django.db import models


# Create your models here.
class DiningTable(models.Model):
    tableId = models.AutoField(primary_key=True, verbose_name="餐桌编号")

    tableCategory = models.IntegerField(verbose_name="餐桌类别")

    tableState = models.IntegerField(verbose_name="餐桌状态")

    def __str__(self):
        description = "餐桌编号:{}\n餐桌类别{}\n".format(self.tableId, self.tableCategory)
        return description

    class Meta:
        verbose_name = "餐桌"
        verbose_name_plural = verbose_name
