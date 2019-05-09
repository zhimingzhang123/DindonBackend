import django_filters
from django_filters.rest_framework import FilterSet

from Dishes.models import Dish


class DishFilter(FilterSet):
    dishPriceMin = django_filters.NumberFilter(field_name='dishPrice', lookup_expr='gte',)
    dishPriceMax = django_filters.NumberFilter(field_name='dishPrice', lookup_expr='lte')

    class Meta:
        model = Dish
        fields = ['dishId', 'dishName', 'dishPriceMin', 'dishPriceMax', 'dishType', 'dishPrice']
