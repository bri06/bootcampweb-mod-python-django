"""Post forms"""

#django
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
  """Post model form"""

  class Meta:
    """Form settings"""
    model=Post
    fields=('user', 'title', 'photo', 'description', 'text')