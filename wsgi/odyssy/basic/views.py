import os

from django.shortcuts import render

from events.models import Event

def index(request):
    events_list = Event.objects.order_by('-event_date')[:int(os.environ.get('NUM_EVENTS_ON_INDEX_PAGE', 3 ))]
    return render(request, 'basic/index.html', context={'events': events_list})
