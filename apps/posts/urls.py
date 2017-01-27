from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='the_wall'),
    url(r'^create_post$', views.create_post, name='create_post'),
    url(r'^edit_post/(?P<post_id>\d+)$', views.edit_post, name='edit_post'),
    url(r'^update_post/(?P<post_id>\d+)$', views.update_post, name='update_post'),
    url(r'^delete_post/(?P<post_id>\d+)$', views.delete_post, name='delete_post')
]
