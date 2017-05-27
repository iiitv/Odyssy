from datetime import datetime, time

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
    return datetime.combine(datetime.max, time.max)

