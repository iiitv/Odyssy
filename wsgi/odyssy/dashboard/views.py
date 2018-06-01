from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import AnnouncementForm, EventForm, NewsForm, SignUpForm, PeopleProfileForm

from announcement.models import Announcement
from events.models import Event
from news.models import News


@login_required
def dashboard(request):
    recent_announcements = Announcement.objects.all()[:3]
    recent_news = News.objects.all()[:3]
    recent_events = Event.objects.all()[:3]
    return render(request, 'dashboard.html', {'recent_announcements': recent_announcements,
                                              'recent_news': recent_news,
                                              'recent_events': recent_events})


@login_required
def signup(request):
    title = 'create new user'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.people.name = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            user.save()
            msg = 'Added ' + user.username
            return redirect(reverse('dashboard:all_users', args=[msg]))
        else:
            print(form.errors)
            return render(request, 'signup.html', {'form': form, 'title': title})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'title': title,
                                           'form': form})


@login_required
def edit_user(request, username):
    title = 'Edit user'
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.people.name = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            user.save()
            msg = 'Edited ' + user.username
            return redirect(reverse('dashboard:all_users', args=[msg]))
        else:
            print(form.errors)
            return render(request, 'signup.html', {'form': form, 'title': title})
    else:
        form = SignUpForm(instance=user)
    return render(request, 'signup.html', {'title': title,
                                           'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('dashboard:dashboard'))
        else:
            if form.errors['old_password']:
                messages.error(request, 'Old password didn\'t match, please enter it again', extra_tags='safe')
            else:
                messages.error(request, 'Something went wrong')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'title': 'Update password',
        'form': form
    })


@login_required
def update_profile(request):
    if request.method == 'POST':
        profile = request.user.people
        form = PeopleProfileForm(request.POST, request.FILES, instance=profile)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:dashboard'))
        else:
            messages.error(request, 'Something went wrong')
    else:
        profile = request.user.people
        form = PeopleProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {
        'title': 'Update profile',
        'form': form
    })


@login_required
def all_users(request, msg=None):
    title = 'All users'
    users = User.objects.all()
    return render(request, 'all_users.html', {'title': title,
                                              'users': users,
                                              'msg': msg})


@login_required
def add(request, data_type):
    title = 'Add ' + data_type
    if request.method == "POST":
        if data_type == 'announcements':
            form = AnnouncementForm(request.POST)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save()
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
                object_instance = form.save()
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
                object_instance = form.save()
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
    """
    List existing announcements/news/events
    :param request: request
    :param data_type: a or n or e
    :param msg: only used for the case in which a new a/n/e is created and it's success msg is to be shown
    :return: HTML page with table containing requested objects
    """
    title = 'List of ' + data_type
    items = Announcement.objects.all()
    if data_type == 'events':
        items = Event.objects.all()
    if data_type == 'news':
        items = News.objects.all()

    return render(request, 'ane_list.html', {'items': items, 'title': title, 'data_type': data_type, 'msg': msg})


@login_required
def ane_edit(request, data_type, data_id):
    """
    Edit announcements/news/events
    :param request: request
    :param data_type: a or n or e
    :param data_id: pk of the requested object instance
    :return: rendered HTML form with instance data
    """
    title = 'Edit ' + data_type
    if request.method == "POST":
        if data_type == 'announcements':
            instance = Announcement.objects.get(pk=data_id)
            form = AnnouncementForm(request.POST, instance=instance)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save()
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return redirect(reverse('dashboard:ane_list', args=['announcements',
                                                                    'Announcement added modified']))
            else:
                print(form.errors)
                return render(request, 'add.html', {'form': form, 'title': title})
        elif data_type == 'events':
            instance = Event.objects.get(pk=data_id)
            form = EventForm(request.POST, instance=instance)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save()
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return redirect(reverse('dashboard:ane_list', args=['events',
                                                                    'Event successfully modified']))
            else:
                print(form.errors)
                return render(request, 'add.html', {'form': form, 'title': title})
        elif data_type == 'news':
            instance = News.objects.get(pk=data_id)
            form = NewsForm(request.POST, instance=instance)
            if form.is_valid():
                form_cleaned = form.clean()
                object_instance = form.save()
                object_instance.start_date = form_cleaned['start_date']
                object_instance.end_date = form_cleaned['end_date']
                object_instance.save()
                return redirect(reverse('dashboard:ane_list', args=['news',
                                                                    'News added modified']))
            else:
                print(form.errors)
                return render(request, 'add.html', {'form': form, 'title': title})
        else:
            return JsonResponse({'msg': 'Could not find what you are looking for. ;('})
    else:
        if data_type == 'announcements':
            instance = get_object_or_404(Announcement, pk=data_id)
            form = AnnouncementForm(instance=instance, initial={'start_date': instance.start_date,
                                                                'end_date': instance.end_date})
        if data_type == 'events':
            instance = get_object_or_404(Event, pk=data_id)
            form = EventForm(instance=instance, initial={'start_date': instance.start_date,
                                                         'end_date': instance.end_date})
        if data_type == 'news':
            instance = get_object_or_404(News, pk=data_id)
            form = NewsForm(instance=instance, initial={'start_date': instance.start_date,
                                                        'end_date': instance.end_date})
        if data_type == 'events' or data_type == 'news' or data_type == 'announcements':
            return render(request, 'add.html', {'form': form, 'title': title})
        else:
            return JsonResponse({'msg': 'Could not find what you are looking for. ;('})


@login_required
def ane_delete(request, data_type, data_id):
    msg = 'Something went wrong'
    if data_type == 'announcements':
        instance = get_object_or_404(Announcement, pk=data_id)
        msg = 'Announcement successfully deleted'
        instance.delete()
    elif data_type == 'news':
        instance = get_object_or_404(News, pk=data_id)
        msg = 'News successfully deleted'
        instance.delete()
    elif data_type == 'events':
        instance = get_object_or_404(Event, pk=data_id)
        msg = 'Events successfully deleted'
        instance.delete()
    else:
        return JsonResponse({'msg': 'Could not find what you are looking for. ;('})
    return redirect(reverse('dashboard:ane_list', args=[data_type, msg]))
