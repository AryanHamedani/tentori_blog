from django.urls import path
from .views import PostDetail,PostList
app_name = 'blog'
url_patterns = [
    path('',PostList.as_view(),name='home'),
    path('/<slug:slug>/',PostDetail.as_view(),name = 'post_detail')
]