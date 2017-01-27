from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_item$', views.create_item, name='create_item'),
    url(r'^edit_item/(?P<item_id>\d+)$', views.edit_item, name='edit_item'),
    url(r'^update_item/(?P<item_id>\d+)$', views.update_item, name='update_item'),
    url(r'^delete_item/(?P<item_id>\d+)$', views.delete_item, name='delete_item'),
    url(r'^display_add_item$', views.display_add_item, name='display_add_item')
]
