"""Post models"""

from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
  """Category model"""
  name = models.CharField(max_length=30)

  def __str__(self):
    """Return name"""
    return self.name

class Post(models.Model):
  """Post model"""

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

  title = models.CharField(max_length=255)
  description = models.CharField(max_length=300, blank=True)
  text = models.TextField(blank=True)
  photo = models.ImageField(upload_to='post/photos')

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  categories = models.ManyToManyField(Category)

  def __str__(self):
    """Return title and username"""
    return '{} by @{}'.format(self.title, self.user.username)