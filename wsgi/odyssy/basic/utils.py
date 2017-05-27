from django.utils import timezone
from django.db.models import Q


def get_active_filter():
    """ basic filter for latest """
    return (Q(initDate__gte=timezone.now()) |
            Q(finDate__gte=timezone.now()))
