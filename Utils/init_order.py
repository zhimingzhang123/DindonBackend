import random

from Orders.models import Order
from Tables.models import Table
from Users.models import User

for i in range(10):
    order = Order.objects.create(
        order_user=User.objects.get(username="admin"),
        order_table=Table.objects.get(table_id=random.randint(1, 9)),
        order_script="不加辣，少点盐，谢谢",
        table_ware_num=random.randint(1, 8)
    )
    order.save()
