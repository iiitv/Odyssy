from basic import utils

from django.shortcuts import render
from .models import News


def news(request):
    news_list = News.get_all_news()
    news_context, num_items, page = utils.paginate_view(request, news_list)
    context = {
        'news_list': news_context,
        'num_items': num_items,
        'curr_page': page
    }
    return render(request, 'news/news_list.html', context=context)


def news_detail(request, news_slug):
    single_news = News.get_single_news_detail(news_slug)
    context = {
        'info': single_news
    }
    return render(request, 'news/single_news.html', context=context)
