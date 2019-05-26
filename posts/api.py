from posts.models import Post
from posts.serializers import PostListSerializer, PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PostsAPI(ListCreateAPIView):

  queryset = Post.objects.all()
  serializer_class = PostSerializer


  def get_serializer_class(self):
    return PostListSerializer if self.request.method == 'GET' else PostSerializer

class PostsDetailAPI(RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
