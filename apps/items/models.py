from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User

# Create your models here.
class ItemManager(models.Manager):
    def create_item(self, postData, user_id):
        user_name=User.objects.get(id=user_id)
        self.create(name=postData['content'], user=User.objects.get(id=user_id), added_by=user_name)
        item_id = self.filter().latest('id')
        self.add_to_wishlist(item_id.id, user_id)

    def add_to_wishlist(self, item_id, user_id):
        item_obj = self.get(id=item_id)
        item_obj.wishlist.add(user_id)

    def get_all_data(self, user_id):
        user_data = User.objects.all()
        items_data = self.all()
        current_user = User.objects.get_user_data_from_session(user_id)
        wishlist = self.get_wishlist(user_id)
        other_items = self.get_other_items(user_id)
        all_data = {
            'users': user_data,
            'items': items_data,
            'current_user': current_user,
            'wishlist': wishlist,
            'other_items': other_items
        }
        print all_data
        return all_data

    def get_wishlist(self, user_id):
        return self.filter(wishlist__id=user_id)

    def get_other_items(self, user_id):
        return self.all().exclude(wishlist__id=user_id)

    def remove_from_wl(self, item_id, user_id):
        item_obj = self.get(id=item_id)
        user_obj = User.objects.get(id=user_id)
        item_obj.wishlist.remove(user_obj)

    def get_item_wishers(self, item_id):
        users = User.objects.filter(in_wishlist=item_id)
        print users
        return users

    def get_item_data(self, item_id):
        item_data = self.get(id=item_id)
        print item_data
        return item_data

    def is_user(self, item_id, user_id):
        is_true = self.filter(id=item_id,user=User.objects.get(id=user_id))
        return is_true

    def update_item(self, postData, item_id):
        content=postData['content']
        self.filter(id=item_id).update(content=content)

    def delete_item(self, postData, item_id):
        self.filter(id=item_id).delete()


class Item(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, related_name='user_posts')
    added_by = models.ForeignKey(User, related_name='added_items', null=True)
    wishlist = models.ManyToManyField(User, related_name='in_wishlist', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
