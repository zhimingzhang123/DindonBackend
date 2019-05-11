from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
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
    queryset = BookTime.objects.all()
    serializer_class = BookTableSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        table_id = serializer.validated_data['table']
        book_date = serializer.validated_data['book_date']
        book_time = serializer.validated_data['book_time']
        book_user = request.user

        if not book_user:
            return Response(
                {"error": "用户未登录或登录失效"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if BookTime.objects.filter(table_id=table_id, book_date=book_date, book_time=book_time):
            return Response(
                {"error": "该餐桌此时间段已被预定"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if len(BookTime.objects.filter(table_id=table_id, book_date=book_date)) >= 4:
            return Response(
                {"error": "该餐桌无法预定"},
                status=status.HTTP_400_BAD_REQUEST
            )

        book_time_record = BookTime(
            table_id=table_id,
            book_date=book_date,
            book_time=book_time,
            book_user=book_user
        )

        book_time_record.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
