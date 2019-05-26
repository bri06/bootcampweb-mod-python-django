"""Posts views."""
import datetime
# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


class PostsFeedView(LoginRequiredMixin, ListView):
  """Return all published posts"""
  template_name = 'posts/feed.html'
  model = Post
  ordering = ('-created',)
  paginate_by = 5
  context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
  """Create a new post"""
  template_name = 'posts/new.html'
  form_class = PostForm
  success_url = reverse_lazy('feed')

  def get_context_data(self, **kwargs):
    """Add user to context"""
    context = super().get_context_data(**kwargs)
    context['user'] = self.request.user
    return context


class PostDetailView(LoginRequiredMixin, DetailView):
  """Return post detail"""
  template_name = 'posts/detail.html'
  queryset = Post.objects.all()
  context_object_name = 'post'