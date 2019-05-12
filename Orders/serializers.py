from rest_framework import serializers

from Orders.models import Order, OrderDish
from Tables.models import Table
from Users.models import User


class OrderDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDish
        fields = ("dish", "dish_num")


class OrderListSerializer(serializers.ModelSerializer):
    order_dish_num = serializers.SerializerMethodField()
    order_dishes = serializers.SerializerMethodField()

    def get_order_dishes(self, obj):
        dishes = OrderDish.objects.filter(order=obj.order_id)
        return OrderDishSerializer(dishes, many=True).data

    def get_order_dish_num(self, obj):
        dishes = OrderDish.objects.filter(order=obj.order_id)
        cnt = 0
        for dish in dishes:
            cnt += dish.dish_num
        return cnt

    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.Serializer):
    order_table = serializers.IntegerField(required=True)
    pay_method = serializers.IntegerField(required=True)
    order_script = serializers.CharField(required=True)
    order_dishes = OrderDishSerializer(many=True)
    order_price = serializers.FloatField(required=True)
    table_ware_num = serializers.IntegerField(required=True)

    # order_user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        order_dishes = validated_data.pop('order_dishes')

        table = validated_data.pop('order_table')
        # 调试用
        user = User.objects.get(username="zwlin")

        table = Table.objects.get(table_id=table)
        order = Order.objects.create(**validated_data, order_user=user, order_table=table)
        for dish in order_dishes:
            OrderDish.objects.create(order=order, **dish)
        return order
