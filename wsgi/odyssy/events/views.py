from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from .models import Event


def event(request):
    events_list = Event.get_all_events()
    num_items = request.GET.get('num_items', default=10)
    paginator = Paginator(events_list, num_items)
    page = request.GET.get('page', default=1)
    try:
        events = paginator.page(page)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    context = {'events': events, 'num_items': num_items}
    return render(request, 'events/event_list.html', context=context)


def event_detail(request, event_id):
    single_event = Event.get_single_event_detail(event_id)
    context = {'event': single_event}
    return render(request, 'events/event_single_item.html', context=context)
