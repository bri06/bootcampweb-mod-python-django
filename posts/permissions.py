from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):

  def has_permission(self, request, view):
    from posts.api import PostsDetailAPI
    if request.method == 'POST' or request.user.is_superuser:
      return True

    return request.user.is_authenticated and isinstance(view, PostsDetailAPI)

  def has_object_permission(self, request, view, obj):
    if request.method == 'GET':
      return obj.user == request.user or request.user.is_superuser

    return obj.user == request.user or request.user.is_superuser


