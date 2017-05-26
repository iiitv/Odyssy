from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from .models import Announcement


def index(request):
    announcements = Announcement.get_all_announcement()
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
    announcement = Announcement.get_single_announcement(announcement_id)
    if announcement:
        announcement = announcement.get()
    else:
        announcement = None
    context = {
        'info': announcement,
        }
    return render(request, 'announcement/info.html', context)
