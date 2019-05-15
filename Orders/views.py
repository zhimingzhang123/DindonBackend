from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from Orders.models import Order, OrderDetail
from Orders.serializers import OrderDetailSerializer, OrderSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
