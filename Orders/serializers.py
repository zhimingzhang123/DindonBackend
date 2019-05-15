from rest_framework import serializers

from Dishes.models import Dish
from Orders.models import Order, OrderDetail, Transaction
from Tables.models import Table
from Users.models import User


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    订单详情的序列化，从前端获得的只有dish_id 和 dish_num
    """

    def validate_dish_id(self, data):
        if Dish.objects.filter(dish_id=data):
            return data
        else:
            raise serializers.ValidationError("菜品不存在")

    class Meta:
        model = OrderDetail
        exclude = ('id', 'order', 'created_at', 'update_at')
        extra_kwargs = {
            "dish_name": {"read_only": True},
            "dish_price": {"read_only": True},
            "dish_picture": {"read_only": True},
            "dish_description": {"read_only": True},
        }


class TransactionSerializer(serializers.ModelSerializer):
    """
    交易信息的序列化
    """

    class Meta:
        model = Transaction
        exclude = ('id', 'order')


class OrderSerializer(serializers.ModelSerializer):
    """
    订单的序列化
    """
    order_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    order_table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())
    order_detail = OrderDetailSerializer(many=True)
    order_price = serializers.FloatField(required=True, write_only=True)
    pay_method = serializers.IntegerField(write_only=True)
    order_status = serializers.IntegerField(required=True, write_only=True)
    # 交易信息时自动创建的，故只能读取
    transaction = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'order_id',
            'order_user',
            'order_table',
            'order_price',
            'order_script',
            'order_status',
            'order_detail',
            'table_ware_num',
            'pay_method',
            'transaction'
        )
        extra_kwargs = {
            "order_script": {"write_only": True}
        }

    def validate_pay_method(self, data):
        if data == 0 or data == 1:
            return data
        else:
            raise serializers.ValidationError("支付方式异常")

    def validate(self, attrs):
        order_details = attrs["order_detail"]
        price = 0
        # 验证价格计算正确
        for detail in order_details:
            dish = Dish.objects.filter(dish_id=detail['dish_id'])
            if not dish:
                raise serializers.ValidationError("菜品信息错误")
            else:
                price += dish[0].dish_price * int(detail['dish_num'])
        if price != attrs['order_price']:
            raise serializers.ValidationError("价格异常")
        return attrs

    def create(self, validated_data):
        order_details = validated_data.pop("order_detail")
        order_price = validated_data.pop('order_price')
        order_status = validated_data.pop('order_status')
        pay_method = validated_data.pop('pay_method')
        order = Order.objects.create(
            **validated_data
        )
        validated_data['order_user'] = User.objects.get(username="admin")
        for detail in order_details:
            dish = Dish.objects.get(dish_id=detail['dish_id'])
            OrderDetail.objects.create(
                **detail,
                order=order,
                dish_name=dish.dish_name,
                dish_price=dish.dish_price,
                dish_picture=dish.dish_picture,
                dish_description=dish.dish_description,
            )
        Transaction.objects.create(
            order=order,
            order_price=order_price,
            order_status=order_status,
            pay_method=pay_method,
        )
        return order
