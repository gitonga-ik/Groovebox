from rest_framework.permissions import BasePermission

class SongCreatePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.is_authenticated: 
            return request.user.role == "Artist"

class SongUpdatePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.artist == request.user

class PlaylistUpdatePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user