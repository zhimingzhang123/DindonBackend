import django_filters
from django_filters.rest_framework import FilterSet

from Dishes.models import Dish


class DishFilter(FilterSet):
    dish_price_min = django_filters.NumberFilter(field_name='dish_price', lookup_expr='gte',)
    dish_price_max = django_filters.NumberFilter(field_name='dish_price', lookup_expr='lte')

    class Meta:
        model = Dish
        fields = ['dish_id', 'dish_name', 'dish_price_min', 'dish_price_max', 'dish_type', 'dish_price']
