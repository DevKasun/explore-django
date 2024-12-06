from django.urls import path
from app.views import (
    ArticleListView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("article/create/", ArticleCreateView.as_view(), name="article_create"),
    path("article/<int:pk>/update/", ArticleUpdateView.as_view(), name="update_article"),
    path("article/<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_article"),
]