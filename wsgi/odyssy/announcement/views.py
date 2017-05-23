from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.db.models import Q

from .models import Announcement
import datetime

# Create your views here.
def index(request):
    announcements = Announcement.objects.all().order_by('-initDate')
    paginator = Paginator(announcements, 10)

    page = request.GET.get('page', default=1)
    try:
        announcements = paginator.page(page)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)
    context = {
        'announcement_list': announcements,
        }
    return render(request, 'announcement/index.html', context)


def open_view(request, announcement_id):
    announcement = Announcement.objects.filter(key=announcement_id)
    if announcement:
        announcement = announcement.get()
    else:
        announcement = None
    context = {
        'info': announcement,
        }
    return render(request, 'announcement/info.html', context)

def latest_announcement(cnt):
    announcements = Announcement.objects.filter(
        Q(initDate__gte=datetime.date.today())|
        Q(finDate__gte=datetime.date.today())
    ).order_by('-initDate')[:cnt]
    return announcements
