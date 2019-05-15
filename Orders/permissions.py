from rest_framework import permissions

from Users.models import UserType


class SuperPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == UserType.Manager or request.user.is_superuser


class OrderBasePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous


class CustomerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == UserType.Customer


class ChefPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == UserType.Chef
