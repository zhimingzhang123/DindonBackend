from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from Orders.models import Order, OrderDetail
from Orders.serializers import OrderDetailSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer


# class OrderCreateView(CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderCreateSerializer
