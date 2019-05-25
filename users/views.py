"""Users views """

#django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post

# Forms
from users.forms import SignupForm


class LoginView(auth_views.LoginView):
  """Login view"""
  template_name = 'users/login.html'


class UserDetailView(LoginRequiredMixin, DetailView):
  template_name = 'users/blog.html'
  slug_field = 'username'
  slug_url_kwarg = 'username'
  queryset = User.objects.all()
  context_object_name = 'user'

  def get_context_data(self, **kwargs):
    """Add user's post to context"""
    context = super().get_context_data(**kwargs)
    user = self.get_object()
    context['posts'] = Post.objects.filter(user=user).order_by('-created')
    return context

class SignupView(FormView):
  """Users sign up view"""
  template_name = 'users/signup.html'
  form_class = SignupForm
  success_url = reverse_lazy('login')

  def form_valid(self, form):
    """Save form data"""
    form.save()
    return super().form_valid(form)

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
  """Logout view"""
  pass

@login_required
def logout_view(request):
  """Logout a user"""
  logout(request)
  return redirect('login')
