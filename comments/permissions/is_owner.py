from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_superuser
            or request.user == obj.writer
            or request.user == obj.tweet.author
        )
