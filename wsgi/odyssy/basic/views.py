from django.shortcuts import render

from events.models import Event

def index(request):
    events_list = Event.objects.order_by('-event_date')[:3]
    return render(request, 'basic/index.html', context={'events': events_list})
