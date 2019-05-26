from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):


  class Meta:
    model = Post
    fields = ['id', 'title', 'description', 'photo', 'created']


class PostSerializer(ModelSerializer):

  class Meta:
    model = Post
    fields = ['id', 'user', 'title', 'text', 'description', 'photo', 'created', 'modified', 'categories']
    read_only_fields = ['id', 'created', 'modified', 'user']