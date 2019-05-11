from django_filters.rest_framework import FilterSet

from Tables.models import Table


class TableFilter(FilterSet):
    class Meta:
        model = Table
        fields = ['table_id', 'table_category', 'table_state']
