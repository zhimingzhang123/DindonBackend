from rest_framework import permissions

from Users.models import UserType


class OrderBasePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous


class OrderCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == UserType.Customer
