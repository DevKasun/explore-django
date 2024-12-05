from django.urls import path
from app.views import home, ArticleCreateView

urlpatterns = [
    path('', home),
    path("article/create/", ArticleCreateView.as_view(), name="create_article")
]