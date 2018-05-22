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
                return ane_list(request, data_type='announcements',
                                msg='Announcement added successfully')
            else:
                print(form.errors)
                return render(request, 'add.html', {'form': form, 'title': title})
        elif data_type == 'events':
            form = EventForm(request.POST)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save(commit=False)
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return ane_list(request, data_type='events',
                                msg='Announcement added successfully')
            else:
                print(form.errors)
                return render(request, 'add.html', {'form': form, 'title': title})
        elif data_type == 'news':
            form = NewsForm(request.POST)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save(commit=False)
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return ane_list(request, data_type='news',
                                msg='Announcement added successfully')
            else:
                print(form.errors)
                return render(request, 'add.html', {'form': form, 'title': title})
        else:
            return JsonResponse({'msg': 'Could not find what you are looking for. ;('})
    else:
        if data_type == 'announcements':
            form = AnnouncementForm()
            return render(request, 'add.html', {'form': form,
                                                'title': title})
        if data_type == 'events':
            form = EventForm()
            return render(request, 'add.html', {'form': form,
                                                'title': title})

        if data_type == 'news':
            form = NewsForm()
            return render(request, 'add.html', {'form': form,
                                                'title': title})


@login_required
def ane_list(request, data_type, msg=None):
    title = 'List of ' + data_type
    items = Announcement.objects.all()
    if data_type == 'events':
        items = Event.objects.all()
    if data_type == 'news':
        items = News.objects.all()

    return render(request, 'ane_list.html', {'items': items, 'title': title, 'msg': msg})
