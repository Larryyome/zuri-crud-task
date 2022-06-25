from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class PostListView(ListView):
    model= Post
    
class PostCreateView(CreateView):
    model=Post
    field=Post.object.all()
    success_url=reverse_lazy('blog:all')
    
class PostDetailView(DetailView):
    model=Post
    
class PostUpdateView(UpdateView):
    model=Post
    field=Post.object.all()
    success_url=reverse_lazy('blog:all')
    
class PostDeleteView(DeleteView):
    model=Post
    field=Post.object.all()
    success_url=reverse_lazy('blog:all')
    