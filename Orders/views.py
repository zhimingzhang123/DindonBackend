from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView

from Orders.models import Order, Transaction
from Orders.permissions import OrderBasePermission, CustomerPermission, SuperPermission
from Orders.serializers import OrderSerializer, TransactionSerializer, TransactionUpdateSerializer
from Users.models import UserType


class OrderListView(ListAPIView):
    """
    当前用户订单列表
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderBasePermission,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.user_type == UserType.Manager:
            return Order.objects.all()
        else:
            return Order.objects.filter(order_user=user)


class OrderRetrieveAPIView(RetrieveAPIView):
    """
    取回订单
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (SuperPermission | CustomerPermission,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.user_type == UserType.Manager:
            return Order.objects.all()
        else:
            return Order.objects.filter(order_user=user)


class OrderCreateView(CreateAPIView):
    """
    创建订单
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderBasePermission, CustomerPermission)


# TODO:支付API
class OrderPurchaseView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = TransactionSerializer


class OrderProcessView(UpdateAPIView):
    """
    订单处理
    """
    permission_classes = (OrderBasePermission,)
    lookup_field = 'order'
    queryset = Transaction.objects.all()
    serializer_class = TransactionUpdateSerializer
