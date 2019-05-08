from rest_framework import serializers

from Tables.models import DiningTable


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = '__all__'
