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
    search_fields = ('dishName', 'dishType', 'dishDescription')
    ordering_fields = "__all__"


class DishTypeView(APIView):

    def get(self, requset):
        dishes = Dish.objects.all()
        typeList = set()
        for dish in dishes:
            if dish.dishType:
                typeList.add(dish.dishType)
        return Response(typeList)
