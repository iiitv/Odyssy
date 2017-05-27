from django.utils import timezone
from django.db.models import Q


def get_active_filter():
    """ basic filter for latest """
    return (Q(start_date__gte=timezone.now()) |
            Q(end_date__gte=timezone.now()))
