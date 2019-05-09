from django.contrib import admin

# Register your models here.
from Orders.models import Order

admin.site.register(Order)
