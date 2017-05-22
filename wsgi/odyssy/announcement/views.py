from django.shortcuts import render

from .models import Announcement

# Create your views here.
def index(request):
    announcements = Announcement.objects.all()
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
