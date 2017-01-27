from __future__ import unicode_literals
from django.db import models
from ..posts.models import Post


# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=150)
    # user = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = CommentManager()
