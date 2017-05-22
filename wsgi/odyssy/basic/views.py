from django.shortcuts import render

from announcement.models import Announcement

def index(request):
    latest_announcement = Announcement.objects.order_by('initDate')[:5]
    context = {
        'latest_announcement': latest_announcement,
    }
    return render(request, 'basic/index.html', context)
