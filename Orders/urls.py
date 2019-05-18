from django.urls import path

from Orders.views import OrderListView, OrderCreateView, OrderProcessView, OrderRetrieveAPIView, \
    AlipayProcessView

urlpatterns = [
    path('', OrderListView.as_view(), name="order_list"),
    path('create', OrderCreateView.as_view(), name="order_create"),
    path('<int:pk>', OrderRetrieveAPIView.as_view(), name="order_info"),
    path('<int:order>/process/', OrderProcessView.as_view(), name="order_process"),
    path('notify', AlipayProcessView.as_view(), name="alipay_notify")
]
