from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, UpdateAPIView

from Tables.filters import TableFilter
from Tables.models import DiningTable
from Tables.serializers import TableSerializer, TableUpdateSerializer


class TableListView(ListAPIView):
    queryset = DiningTable.objects.all()
    serializer_class = TableSerializer
    filter_class = TableFilter
    filter_backends = (DjangoFilterBackend,)


class TableUpdateView(UpdateAPIView):
    queryset = DiningTable.objects.all()
    serializer_class = TableUpdateSerializer
