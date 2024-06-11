from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from .models import Post

# Using CBV
class PostListView(ListView):
    
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' #ini sama aja posts = Post.objects.all() dan return Queryset, kalau gk di kasih ini defaultnya bukan 'posts' tapi 'objects'/'object' (lupa)
    ordering = ['-date_posted']
    paginate_by = 6



class UserPostListView(ListView):
    
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    
    model = Post
    template_name = 'blog/article.html'
    context_object_name = 'post'



class PostCreateView(LoginRequiredMixin, CreateView):
    
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/create.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/create.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False
    
 
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Post
    template_name = 'blog/delete.html'
    ontext_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False



def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'blog/about.html', context)