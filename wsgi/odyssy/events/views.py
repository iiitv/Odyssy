import os

from django.contrib.admin.templatetags.admin_list import pagination
from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Event


def event(request):
    events_list = Event.objects.order_by('-event_date')
    paginator = Paginator(events_list, os.environ.get('NUM_EVENTS_ON_INDEX_PAGE', 3 ))
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    context = {'events': events}
    return render(request, 'events/index.html', context=context)


def event_detail(request, event_id):
    single_event = get_object_or_404(Event, pk=event_id)
    context = {'event': single_event}

    return render(request, 'events/single_item.html', context=context)