import django_filters
from django_filters.rest_framework import FilterSet

from Orders.models import Order


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = ['order_id', 'order_price', 'order_status']
