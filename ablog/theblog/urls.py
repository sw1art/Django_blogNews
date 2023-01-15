from django.urls import path
from .views import MainView, ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post')
]
