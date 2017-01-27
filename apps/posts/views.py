from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Post
# Create your views here.
def index(request):
    print(request.session['user_id'])
    all_data = Post.objects.get_all_data(request.session['user_id'])
    context = {
        'data': all_data
    }
    print(all_data)
    return render(request, 'posts/index.html', context)
def create_post(request):
    Post.objects.create_post(request.POST, request.session['user_id'])
    return redirect('posts_ns:the_wall')
def delete_post(request):
    pass
def edit_post(request, post_id):
    if not Post.objects.is_user(post_id, request.session['user_id']):
        messages.add_message(request, messages.ERROR, 'You can only edit your own posts, fella.')
        return redirect('posts_ns:the_wall')
    post_info = Post.objects.get_post_data(post_id)
    context = {
        'post_data': post_info
    }
    return render(request, 'posts/post.html', context)
def update_post(request, post_id):
    Post.objects.update_post(request.POST, post_id)
    return redirect('/')

def delete_post(request, post_id):
    Post.objects.delete_post(request.POST, post_id)
    return redirect('/')
