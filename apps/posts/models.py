from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User

# Create your models here.
class PostManager(models.Manager):
    def create_post(self, postData, user_id):
        self.create(content=postData['content'], user=User.objects.get(id=user_id))
    def get_all_data(self, user_id):
        user_data = User.objects.all()
        post_data = self.all()
        current_user = User.objects.get_user_data_from_session(user_id)
        all_data = {
            'users': user_data,
            'posts': post_data,
            'current_user': current_user
        }
        print all_data
        return all_data

    def get_post_data(self, post_id):
        post_data = self.get(id=post_id)
        print post_data
        return post_data

    def is_user(self, post_id, user_id):
        is_true = self.filter(id=post_id,user=User.objects.get(id=user_id))
        return is_true

    def update_post(self, postData, post_id):
        content=postData['content']
        self.filter(id=post_id).update(content=content)

    def delete_post(self, postData, post_id):
        self.filter(id=post_id).delete()


class Post(models.Model):
    content = models.CharField(max_length=450)
    user = models.ForeignKey(User, related_name='user_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()
