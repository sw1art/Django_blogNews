from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm, EditForm

class MainView(ListView):
    model = Post
    template_name = 'main.html'
    ordering = ['-date_post']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(MainView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    try:
        category_name = Category.objects.filter(name=cats)
        category_posts = Post.objects.filter(category=category_name[0])
        return render(request, 'categoryies.html', {
            'cats': cats,
            'category_posts': category_posts
        })
    except:
        return render(request, 'categoryies.html', {
        })  
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostViews(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('main')