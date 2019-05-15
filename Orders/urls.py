from django.urls import path

from Orders.views import OrderListView, OrderCreateView, OrderProcessView

urlpatterns = [
    path('', OrderListView.as_view(), name="orders"),
    path('create', OrderCreateView.as_view(), name="order_create"),
    path('<int:order>/process/', OrderProcessView.as_view(), name="order_process"),
]
