from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from .models import News


# Create your views here.

@staticmethod
def open_all_news(request):
    news = News.objects.order_by('-start_date')
    num_items = request.GET.get('num_items', default=10)
    paginator = Paginator(news, num_items)
    page = request.GET.get('page', default=1)
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news_list': news,
        'num_items': num_items,
    }
    return render(request, 'news/news_list.html', context)


@staticmethod
def open_single_news(request, news_id):
    news = News.objects.filter(pk=news_id)
    if news:
        news = news.get()
    else:
        news = None
    context = {
        'info': news,
    }
    return render(request, 'news/single_news.html', context)


@staticmethod
def latest_news(num_items):
    news_list = News.objects.order_by('-start_date')[:num_items]
    return news_list
