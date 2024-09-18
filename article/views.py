from django.views.generic import DetailView
from .models import Article

class ArticleDetailView(DetailView):
    template_name = "article/article_detail.html"
    model = Article