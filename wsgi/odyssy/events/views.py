from basic import utils

from django.shortcuts import render
from .models import Event


def event(request):
    events_list = Event.get_all_events()
    events, num_items, page = utils.paginate_view(request, events_list)
    context = {'events': events, 'num_items': num_items, 'curr_page': page}
    return render(request, 'events/event_list.html', context=context)


def event_detail(request, event_id):
    single_event = Event.get_single_event_detail(event_id)
    context = {'event': single_event}
    return render(request, 'events/event_single_item.html', context=context)
