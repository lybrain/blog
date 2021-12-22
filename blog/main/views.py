from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from article.models import Article
from django.core.paginator import Paginator



def index(request, page=1):
    if request.method == 'GET':
        search_query = request.GET.get('search', None)
        ordering = request.GET.get('order', '-created_date,Created date ↓')
        ordering = ordering.split(',')
        items_per_page = 2
        articles = Article.objects.all().order_by(ordering[0])
        if search_query:  # select * from articles where title like '%search_query%';
            articles = articles.filter(title__icontains=search_query)
        paginated_articles = Paginator(articles,items_per_page)
        return render(request, 'index.html', {"articles": paginated_articles.page(page),
                                              "pages_range": paginated_articles.page_range, 
                                              'ordering': ordering[1]})
    else:
        raise HttpResponseBadRequest
