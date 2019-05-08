from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Dishes.models import Dish
from Dishes.serializers import DishSerializer, DishTypeSerializer
from rest_framework import generics


class DishListView(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishTypeView(APIView):

    def get(self, requset):
        dishes = Dish.objects.all()
        typeList = set()
        for dish in dishes:
            if dish.dishType:
                typeList.add(dish.dishType)
        return Response(typeList)