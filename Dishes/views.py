from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Dishes.filters import DishFilter
from Dishes.models import Dish
from Dishes.serializers import DishSerializer


class DishListView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_class = DishFilter
    search_fields = ('dish_name', 'dish_type', 'dish_description')
    ordering_fields = "__all__"


class DishTypeView(APIView):

    def get(self, requset):
        dishes = Dish.objects.all()
        type_list = set()
        for dish in dishes:
            if dish.dish_type:
                type_list.add(dish.dish_type)
        return Response(type_list)
