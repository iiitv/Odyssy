from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import AnnouncementForm, EventForm, NewsForm

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
        if data_type == 'announcements':
            form = AnnouncementForm(request.POST)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save(commit=False)
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return redirect(dashboard)
            else:
                print(form.clean())
                return JsonResponse({'msg': 'something went wrong'})
        elif data_type == 'event':
            form = EventForm(request.POST)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save(commit=False)
                object_instance.start_time = form_cleaned['start_date']
                object_instance.end_time = form_cleaned['end_date']
                object_instance.save()
                return redirect(dashboard)
            else:
                print(form.clean())
                return JsonResponse({'msg': 'something went wrong'})
        elif data_type == 'news':
            form = NewsForm(request.POST)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save(commit=False)
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return redirect(dashboard)
            else:
                print(form.clean())
                return JsonResponse({'msg': 'something went wrong'})
        else:
            return JsonResponse({'msg': 'Could not find what you are looking for. ;('})
    else:
        if data_type == 'announcements':
            form = AnnouncementForm()
            return render(request, 'add.html', {'form': form,
                                                'title': title})
        if data_type == 'event':
            form = EventForm()
            return render(request, 'add.html', {'form': form,
                                                'title': title})

        if data_type == 'news':
            form = NewsForm()
            return render(request, 'add.html', {'form': form,
                                                'title': title})
