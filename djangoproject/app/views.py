from django.shortcuts import render
from app.models import Article

def home(request):
    article = Article.objects.all()
    return render(request, 'app/home.html', {'article': article})