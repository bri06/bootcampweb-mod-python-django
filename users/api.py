"""Api of users"""

# Django
from django.contrib.auth.models import User

# rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework import status


# users
from users.serializers import UserListSerializer, UserSerializer, WriteUserSerializer
from users.permissions import UserPermission

class UsersAPI(GenericAPIView):

  permission_classes = [UserPermission]

  def get(self, request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = WriteUserSerializer(data=request.data)
    if serializer.is_valid():
      new_user = serializer.save()
      user_serializer = UserSerializer(new_user)
      return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

  permission_classes = [UserPermission]

  def get(self, request, pk):
    """Get user detail"""
    user = get_object_or_404(User, pk=pk)
    self.check_object_permissions(request, user)
    serializer = UserSerializer(user)
    return Response(serializer.data)

  def delete(self, request, pk):
    user = get_object_or_404(User, pk=pk)
    self.check_object_permissions(request, user)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def put(self, request, pk):
    user = get_object_or_404(User, pk=pk)
    self.check_object_permissions(request, user)
    serializer = WriteUserSerializer(user, data=request.data)
    if serializer.is_valid():
      updated_user = serializer.save()
      user_serializer = UserSerializer(updated_user)
      return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)