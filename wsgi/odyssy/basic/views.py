from django.shortcuts import render

from events.models import Event


def index(request):
    events_list = Event.get_latest_events(3)
    return render(request, 'basic/index.html', context={'events': events_list})
