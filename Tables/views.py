from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView

from Tables.filters import TableFilter
from Tables.models import Table, BookTime
from Tables.serializers import TableListSerializer, BookTableSerializer


class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
    filter_class = TableFilter
    filter_backends = (DjangoFilterBackend,)


class BookTableView(CreateAPIView):
    queryset = BookTime.objects.all()
    serializer_class = BookTableSerializer

    def create(self, request, *args, **kwargs):
        pass