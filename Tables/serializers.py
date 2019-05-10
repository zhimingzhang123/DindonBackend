from rest_framework import serializers, viewsets

from Tables.models import DiningTable


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = "__all__"


class TableUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = ('tableId', 'tableState')

