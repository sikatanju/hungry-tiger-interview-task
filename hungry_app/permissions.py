from rest_framework import permissions
from .models import Vendor


class IsVendorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.user and request.user.is_authenticated and request.user.is_vendor and not request.user.is_staff)
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user.is_vendor and obj.vendor.user == request.user)
    

class IsAdminAndReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff and request.method in permissions.SAFE_METHODS:
            return True
        
        return False