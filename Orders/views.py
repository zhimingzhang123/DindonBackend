from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView

from Orders.filters import OrderFilter
from Orders.models import Order
from Orders.serializers import OrderListSerializer, OrderCreateSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer