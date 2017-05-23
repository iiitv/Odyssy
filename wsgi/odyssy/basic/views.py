from django.shortcuts import render
from news import views as news_view


def index(request):
    """ Index page of the Website """
    latest_news = news_view.latest_news(3)
    context = {
        'latest_news': latest_news,
    }
    return render(request, 'basic/index.html', context)
