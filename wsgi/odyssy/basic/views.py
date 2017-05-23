from django.shortcuts import render

from announcement import views as announcement_view
from events.models import Event

def index(request):
    """ Index page of the Website """
    latest_announcement = announcement_view.latest_announcement(5)
    events_list = Event.get_latest_events(3)
    context = {
        'latest_announcement': latest_announcement,
        'events': events_list,
    }
    return render(request, 'basic/index.html', context)
