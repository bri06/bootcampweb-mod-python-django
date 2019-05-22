from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from posts import views as post_views
from users import views as users_views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', post_views.list_posts, name='feed'),
    path('posts/new/', post_views.create_post, name='create_post'),

    path('login/', users_views.login_view, name='login'),
    path('logout', users_views.logout_view, name='logout'),
    path('signup', users_views.signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
