from rest_framework.permissions import BasePermission
from .models import Partner, Director, Accountant


class IsPartner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return user.is_superuser or Partner.objects.filter(user=user).exists()
        return False


class IsDirector(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return user.is_superuser or Director.objects.filter(user=user).exists()
        return False


class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return user.is_superuser or Accountant.objects.filter(user=user).exists()
        return False
