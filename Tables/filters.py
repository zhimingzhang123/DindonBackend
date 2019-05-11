from django_filters.rest_framework import FilterSet

from Tables.models import DiningTable


class TableFilter(FilterSet):
    class Meta:
        model = DiningTable
        fields = ['tableId', 'tableCategory', 'tableState']
