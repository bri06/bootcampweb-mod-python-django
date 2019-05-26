"""Posts api"""

# rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Posts
from posts.models import Post
from posts.serializers import PostListSerializer, PostSerializer
from posts.permissions import PostPermission


class PostsAPI(ListCreateAPIView):

  permission_classes = [PostPermission]

  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['title', 'photo', 'user__first_name', 'user__last_name']
  ordering_fields = ['title', 'created']

  queryset = Post.objects.all()

  serializer_class = PostSerializer

  def get_serializer_class(self):
    return PostListSerializer if self.request.method == 'GET' else PostSerializer


class PostsDetailAPI(RetrieveUpdateDestroyAPIView):

  permission_classes = [PostPermission]

  serializer_class = PostSerializer

  def perform_update(self, serializer):
    serializer.save(user=self.request.user)
