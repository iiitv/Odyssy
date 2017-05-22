from django.shortcuts import render

from announcement import views as announcement_view

def index(request):
    """ Index page of the Website """
    latest_announcement = announcement_view.latest_announcement(5)
    context = {
        'latest_announcement': latest_announcement,
    }
    return render(request, 'basic/index.html', context)
