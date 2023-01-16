from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, EditForm

class MainView(ListView):
    model = Post
    template_name = 'main.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostViews(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('main')