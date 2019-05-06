from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from Dishes.models import Dish
from Dishes.serializers import DishSerializer


class DishListView(APIView):

    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
