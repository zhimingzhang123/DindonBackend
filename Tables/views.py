from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from Tables.models import DiningTable
from Tables.serializers import TableSerializer


class TableListView(APIView):
    def get(self, request):
        tables = DiningTable.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)
