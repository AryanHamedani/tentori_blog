from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    query_set = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post-detail.html'