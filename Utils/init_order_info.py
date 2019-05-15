import random

from Dishes.models import Dish
from Orders.models import Transaction, OrderDetail, Order

price = 0
order = Order.objects.get(order_id=random.randint(1, 10))
for i in range(4):
    id = random.randint(1, 100)
    dish = Dish.objects.get(dish_id=id)
    num = random.randint(1, 5)
    price += dish.dish_price * num
    d = OrderDetail.objects.create(
        order=order,
        dish_id=dish.dish_id,
        dish_name=dish.dish_name,
        dish_price=dish.dish_price,
        dish_picture=dish.dish_picture,
        dish_description=dish.dish_description,
        dish_num=num
    )
    d.save()
Transaction.objects.create(
    order=order,
    order_price=price,
    order_status=random.randint(1, 4),
    pay_method=random.randint(0, 1),
).save()
