from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView

def home(request):
    article = Article.objects.all()
    return render(request, 'app/home.html', {'article': article})


#We can create same form using class based view like this

class ArticleCreateView(CreateView):
    template_name = 'app/article_create.html'
    model = Article
    fields = ['title', 'status', 'content', 'word_column', 'twitter_post']
    success_url = reverse_lazy("home")


# def create_article(request):
#     if request.method == "post":
#         # Data is submitted
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             new_article = Article(
#                 title = form_data['title'],
#                 status = form_data['status'],
#                 content = form_data['content'],
#                 word_count = form_data['word_count'],
#                 twitter_post = form_data['twitter_post']
#             )
            
#             new_article.save()
            
#             return redirect("home")
#     else: 
#         form = CreateArticleForm()
#     return render(request, 'app/article_create.html', {'form': form})