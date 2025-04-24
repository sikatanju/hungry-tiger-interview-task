from rest_framework import permissions


class IsVendorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.user and request.user.is_authenticated and request.user.is_vendor and not request.user.is_staff)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (request.user and request.user.is_authenticated and request.user.is_vendor and obj.vendor.user == request.user)
    

class IsVendorAndReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (request.user and request.user.is_authenticated and request.user.is_vendor)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (obj.user == request.user)
    

class IsCustomerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        elif request.method == 'POST' and request.user.is_customer:
            return True
        
        return False