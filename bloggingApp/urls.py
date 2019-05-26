from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from posts import views
from posts import views as post_views
from users import views as users_views
from users.api import UsersAPI, UserDetailAPI

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', post_views.PostsFeedView.as_view(), name='feed'),
    path('posts/new/', views.CreatePostView.as_view(), name='create_post'),
    path('posts/<str:username>/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    path('blogs/<str:username>', users_views.UserDetailView.as_view(), name='user_blog'),

    path('login/', users_views.LoginView.as_view(), name='login'),
    path('logout', users_views.LogoutView.as_view(), name='logout'),
    path('signup', users_views.SignupView.as_view(), name='signup'),

    # API
    path('api/users/', UsersAPI.as_view(), name='users_api'),
    path('api/users/<int:pk>', UserDetailAPI.as_view(), name='user_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
