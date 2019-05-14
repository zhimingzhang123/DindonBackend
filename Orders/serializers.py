from rest_framework import serializers

from Dishes.models import Dish
from Orders.models import Order, OrderDetail
from Tables.models import Table
from Users.models import User


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"
        # extra_kwargs = {
        #     ""
        # }


class OrderSerializer(serializers.ModelSerializer):
    OrderDetail = OrderDetailSerializer()
    class Meta:
        model = Order
        fields = "__all__"

# class OrderDishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDish
#         fields = ("dish", "dish_num")
#
#
# class OrderListSerializer(serializers.ModelSerializer):
#     order_dish_num = serializers.SerializerMethodField()
#     order_dishes = serializers.SerializerMethodField()
#
#     def get_order_dishes(self, obj):
#         dishes = OrderDish.objects.filter(order=obj.order_id)
#         return OrderDishSerializer(dishes, many=True).data
#
#     def get_order_dish_num(self, obj):
#         dishes = OrderDish.objects.filter(order=obj.order_id)
#         cnt = 0
#         for dish in dishes:
#             cnt += dish.dish_num
#         return cnt
#
#     class Meta:
#         model = Order
#         fields = "__all__"
#
#
# class OrderDishSerializer(serializers.ModelSerializer):
#     dish_num = serializers.IntegerField(write_only=True, required=True)
#
#     class Meta:
#         model = Dish
#         fields = (
#             'dish_id',
#             'dish_num',
#         )
#
#
# class OrderCreateSerializer(serializers.ModelSerializer):
#     order_dishes = OrderDishSerializer(many=True)
#
#     order_user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Order
#         fields = (
#             'order_table',
#             'pay_method',
#             'order_script',
#             'order_dishes',
#             'order_price',
#             'table_ware_num',
#             'order_user'
#         )
#
#     # order_table = serializers.IntegerField(required=True)
#     # pay_method = serializers.IntegerField(required=True)
#     # order_script = serializers.CharField(required=True)
#     # order_dishes = OrderDishSerializer(many=True)
#     # order_price = serializers.FloatField(required=True)
#     # table_ware_num = serializers.IntegerField(required=True)
#     #
#
#     def create(self, validated_data):
#         order_dishes = validated_data.pop('order_dishes')
#
#         # table = validated_data.pop('order_table')
#         # 调试用
#         user = User.objects.get(username="zwlin")
#
#         # table = Table.objects.get(table_id=table)
#         order = Order.objects.create(**validated_data, order_user=user)
#         for dish in order_dishes:
#             OrderDish.objects.create(order=order, **dish)
#         return order
