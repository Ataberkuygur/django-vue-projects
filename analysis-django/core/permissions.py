from rest_framework import permissions

class IsUserOfObjectOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_user_of_object = False
        if obj.user == request.user:
            is_user_of_object = True
        return request.method in permissions.SAFE_METHODS or is_user_of_object