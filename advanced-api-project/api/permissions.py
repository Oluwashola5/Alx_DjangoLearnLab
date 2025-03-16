from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to create, update, or delete books.
    Others can only view them.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Read-only access for everyone
        return request.user and request.user.is_staff  # Only admins can modify
