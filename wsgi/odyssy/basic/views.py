from django.shortcuts import render

from events import views


def index(request):
    events_list = views.get_latest_events(3)
    return render(request, 'basic/index.html', context={'events': events_list})
