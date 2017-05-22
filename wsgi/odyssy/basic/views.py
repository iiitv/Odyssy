from django.db.models import Q
from django.shortcuts import render

from announcement.models import Announcement
import datetime

def index(request):
    latest_announcement = Announcement.objects.filter(
        Q(initDate__gte=datetime.date.today())|
        Q(finDate__gte=datetime.date.today())
    ).order_by('initDate')[:5]
    context = {
        'latest_announcement': latest_announcement,
    }
    return render(request, 'basic/index.html', context)
