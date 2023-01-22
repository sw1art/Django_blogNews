from django.urls import path
from .views import MainView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostViews, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/delete/<int:pk>', DeletePostViews.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
]
