from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "You don't have the permission to update this object"

    def has_object_permission(self, request, view, obj):
        my_methods = ['GET','PUT']

        if request.method in my_methods and obj.user == request.user:
            return True

        return False