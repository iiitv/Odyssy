from datetime import datetime, time

from django.core.paginator import Paginator, EmptyPage
from django.utils import timezone
from django.db.models import Q


def get_active_filter():
    """ basic filter for latest """
    return (Q(start_date__gte=timezone.now()) |
            Q(end_date__gte=timezone.now()))


def get_today_start():
    """ set default as start of date """
    return datetime.combine(datetime.today(), time.min)


def get_today_end():
    """ set end as undefined date """
    return datetime.combine(datetime.today(), time.max)


def paginate_view(request, query_set, num_items):
    """ Paginates view from queryset """
    paginator = Paginator(query_set, num_items)
    page = request.GET.get('page', default=1)
    try:
        data_set = paginator.page(page)
    except EmptyPage:
        data_set = paginator.page(paginator.num_pages)
    return data_set
