from basic import utils

from django.shortcuts import render

from .models import Announcement


def index(request):
    announcements = Announcement.get_all_announcement()
    announcements, num_items, page = utils.paginate_view(request, announcements)
    context = {
        'announcement_list': announcements,
        'num_items': num_items,
        'curr_page': page,
        }
    return render(request, 'announcement/announcement-all.html', context)


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
