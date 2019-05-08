from rest_framework import serializers

from Dishes.models import Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        # fields = '__all__'
        exclude = ('dishAddTime',)


class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("dishType",)
