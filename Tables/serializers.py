from rest_framework import serializers

from Tables.models import Table, BookTime


class BookTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTime
        fields = "__all__"


class TableListSerializer(serializers.ModelSerializer):
    book_counts = serializers.SerializerMethodField()
    book_times = serializers.SerializerMethodField()

    def get_book_counts(self, obj):
        books = BookTime.objects.filter(table_id=obj.table_id)
        return len(books)

    def get_book_times(self, obj):
        books = BookTime.objects.filter(table_id=obj.table_id)
        return BookTimeSerializer(books, many=True).data

    class Meta:
        model = Table
        fields = ("table_id", 'table_category', 'table_state', 'book_counts', 'book_times')


class BookTableSerializer(serializers.Serializer):
    table = serializers.IntegerField(
        required=True,
        help_text="餐桌编号"
    )

    book_date = serializers.DateField(
        required=True,
        help_text="预定时期"
    )

    book_time = serializers.IntegerField(
        required=True,
        help_text="预定时间段"
    )

    def validate_table(self, table):
        if Table.objects.filter(table_id=table):
            return table
        else:
            raise serializers.ValidationError("不存在此餐桌")

    # def validate_book_date(self, date):
    #     if
