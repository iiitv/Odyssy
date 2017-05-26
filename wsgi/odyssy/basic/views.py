from django.shortcuts import render
from news.models import News

from events.models import Event


def index(request):
    """ Index page of the Website.
    
    """
    latest_news = News.get_latest_news(3)
    events_list = Event.get_latest_events(3)
    context = {
        'latest_news': latest_news,
        'events': events_list
    }
    return render(request, 'basic/index.html', context)
