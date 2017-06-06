from django.shortcuts import render
from news.models import News

from announcement.models import Announcement
from events.models import Event

import carousel_api


def index(request):
    """ Index page of the Website.

    """
    latest_news = News.get_latest_news(3)
    latest_announcement = Announcement.get_latest_announcements(5)
    events_list = Event.get_latest_events(3)
    active_images = carousel_api.get_all_index_page_images()
    context = {
        'latest_news': latest_news,
        'latest_announcement': latest_announcement,
        'events': events_list,
        'carousel': active_images
    }
    return render(request, 'basic/index.html', context)
