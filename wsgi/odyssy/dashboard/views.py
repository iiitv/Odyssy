from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import AnnouncementForm

from announcement.models import Announcement
from events.models import Event
from news.models import News
from people.models import People


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def add(request, data_type):
    title = 'Add ' + data_type
    if request.method == "POST":
        announcement_form = AnnouncementForm(request.POST)
        if announcement_form.is_valid():
            print("yaha tak pahucha")
            announcement = announcement_form.save(commit=False)
            announcement.save()
            return redirect(dashboard)
        else:
            print(announcement_form.clean())
            return JsonResponse({'msf': 'u fucked up'})
    else:
        form = AnnouncementForm()
        return render(request, 'add.html', {'form': form,
                                            'title': title})
