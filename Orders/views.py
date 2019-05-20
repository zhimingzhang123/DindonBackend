from alipay import AliPay
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from DinDonBackend.permissions import UserBasePermission, SuperPermission, CustomerPermission
from Orders.models import Order, Transaction, OrderStatus
from Orders.serializers import OrderSerializer, TransactionSerializer, TransactionUpdateSerializer
from Users.models import UserType
from Utils.keys.Key import AliPayKey


class OrderListView(ListAPIView):
    """
    当前用户订单列表
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (UserBasePermission,)

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
    创建订单并生成支付链接
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (CustomerPermission,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        price = serializer.validated_data['order_price']

        Host = "120.24.91.195:8000"
        ret_url = "http://" + Host + "/orders/notify"

        app_private_key = AliPayKey.app_private_key()
        alipay_public_key = AliPayKey.alipay_public_key()
        alipay = AliPay(
            appid=AliPayKey.APP_ID,
            app_notify_url=ret_url,  # 默认回调url
            app_private_key_string=app_private_key,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=alipay_public_key,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False
        )
        order_id = serializer.data['order_id']
        order_id = str(order_id)
        order_string = alipay.api_alipay_trade_wap_pay(
            out_trade_no=order_id,
            total_amount=price,
            subject="支付订单",
            return_url=ret_url,
            notify_url=ret_url  # 可选, 不填则使用默认notify url
        )

        pay_url = AliPayKey.GATEWAY_DEV + "?" + order_string

        ret_data = {
            "pay_url": pay_url
        }

        ret_data.update(serializer.data)

        return Response(ret_data, status=status.HTTP_201_CREATED, headers=headers)


class AlipayProcessView(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class OrderProcessView(UpdateAPIView):
    """
    订单处理
    """
    permission_classes = (UserBasePermission,)
    lookup_field = 'order'
    queryset = Transaction.objects.all()
    serializer_class = TransactionUpdateSerializer
