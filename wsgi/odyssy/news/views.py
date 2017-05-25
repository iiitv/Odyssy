from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from .models import News


def news(request):
    news_list = News.get_all_news()
    num_items = request.GET.get('num_items', default=10)
    paginator = Paginator(news_list, num_items)
    page = request.GET.get('page', default=1)
    try:
        news_context = paginator.page(page)
    except EmptyPage:
        news_context = paginator.page(paginator.num_pages)
    context = {
        'news_list': news_context,
        'num_items': num_items
    }
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, news_id):
    single_news = News.get_single_news_detail(news_id)
    context = {
        'info': single_news
    }
    return render(request, 'news/single_news.html', context=context)
