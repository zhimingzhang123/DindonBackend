from django.urls import path

from Orders.views import OrderListView, OrderCreateView

urlpatterns = [
    path('', OrderListView.as_view(), name="orders"),
    path('submit', OrderCreateView.as_view(), name="submit"),
]
