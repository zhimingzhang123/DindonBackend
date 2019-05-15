from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from DinDonBackend.permissions import UserBasePermission, CustomerPermission, SuperPermission
from Tables.filters import TableFilter
from Tables.models import Table, BookTime
from Tables.serializers import TableListSerializer, BookTableSerializer, BookTimeSerializer
from Users.models import UserType


class TableListView(ListAPIView):
    """
    餐桌预定记录
    """
    queryset = Table.objects.all()
    serializer_class = TableListSerializer
    filter_class = TableFilter
    filter_backends = (DjangoFilterBackend,)


class BookTimeListView(ListAPIView):
    """
    用户预订记录
    """
    queryset = BookTime.objects.all()
    serializer_class = BookTimeSerializer
    permission_classes = (UserBasePermission,)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.user_type == UserType.Manager:
            return BookTime.objects.all()
        else:
            return BookTime.objects.filter(book_user=user)


class BookTableView(CreateAPIView):
    """创建预约"""
    queryset = BookTime.objects.all()
    serializer_class = BookTableSerializer
    permission_classes = (CustomerPermission | SuperPermission,)


class BookUpdateView(UpdateAPIView):
    """更新预约"""
    queryset = BookTime.objects.all()
    serializer_class = BookTableSerializer
    permission_classes = (CustomerPermission | SuperPermission,)


class BookDestroyView(DestroyAPIView):
    """删除预约"""
    queryset = BookTime.objects.all()
    serializer_class = None
    permission_classes = (CustomerPermission | SuperPermission,)
