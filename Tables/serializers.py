from rest_framework import serializers

from Tables.models import Table, BookTime


class BookTimeSerializer(serializers.ModelSerializer):
    table = serializers.StringRelatedField()
    book_user = serializers.StringRelatedField()

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


class BookTableSerializer(serializers.ModelSerializer):
    table = serializers.PrimaryKeyRelatedField(
        required=True,
        help_text="餐桌编号",
        queryset=Table.objects.all()
    )

    book_date = serializers.DateField(
        required=True,
        help_text="预定时期"
    )

    book_time = serializers.IntegerField(
        required=True,
        help_text="预定时间段"
    )

    def validate(self, attrs):
        table_id = attrs['table']
        book_date = attrs['book_date']
        book_time = attrs['book_time']

        if BookTime.objects.filter(table_id=table_id, book_date=book_date, book_time=book_time):
            raise serializers.ValidationError('该餐桌此时间段已被预定')

        attrs['book_user'] = self.context['request'].user
        return attrs

    class Meta:
        model = BookTime
        fields = ('table', 'book_time', 'book_date')
