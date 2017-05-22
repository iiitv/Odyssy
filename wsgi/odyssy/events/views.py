from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Event


def event(request):
    events_list = Event.objects.order_by('-event_date')
    paginator = Paginator(events_list, 3)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    context = {'events': events}
    return render(request, 'events/event_list.html', context=context)


def event_detail(request, event_id):
    single_event = get_object_or_404(Event, pk=event_id)
    context = {'event': single_event}
    return render(request, 'events/event_single_item.html', context=context)
