from django.contrib import admin

# Register your models here.
from Orders.models import Order, OrderDetail, Transaction

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Transaction)
