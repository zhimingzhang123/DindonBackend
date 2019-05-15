from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from Tables.filters import TableFilter
from Tables.models import Table, BookTime
from Tables.serializers import TableListSerializer, BookTableSerializer


class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
    filter_class = TableFilter
    filter_backends = (DjangoFilterBackend,)


class BookTableView(CreateAPIView):
    """创建预约"""
    queryset = BookTime.objects.all()
    serializer_class = BookTableSerializer


class BookUpdateView(UpdateAPIView):
    """更新预约"""
    queryset = BookTime.objects.all()
    serializer_class = BookTableSerializer


class BookDestoryView(DestroyAPIView):
    """删除预约"""
    queryset = BookTime.objects.all()
    serializer_class = None
