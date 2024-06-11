from django.urls import path
from .views import PostDeleteView, PostDetailView, PostListView, PostCreateView, PostUpdateView, UserPostListView

app_name = 'blog'

urlpatterns = [
    path('article/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('article/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('article/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('article/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<username>', UserPostListView.as_view(), name='user-posts'),
    path('', PostListView.as_view(), name='blog-home'),
]
