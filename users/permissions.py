from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )