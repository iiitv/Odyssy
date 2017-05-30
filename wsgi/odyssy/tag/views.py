from announcement.models import Announcement
from news.models import News
from basic.models import PhotoExtended

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage


def simple_tag(request, tag_name):
    """ View for simple tag listing """
    latest_announcement = Announcement.get_latest_announcement_tag(tag_name, 5)
    latest_news = News.get_latest_news_tag(tag_name, 5)
    latest_images = PhotoExtended.get_latest_images_tag(tag_name, 5)
    args = {
        'latest_announcement': latest_announcement,
        'latest_news': latest_news,
        'latest_images': latest_images,
    }
    return render(request, 'tag/simple_tag.html', args)


def announcement_tag(request, tag_name):
    """ View for announcement tag listing """
    announcements = Announcement.get_announcement_tag(tag_name)
    paginator = Paginator(announcements, 10)

    page = request.GET.get('page', default=1)
    try:
        announcements = paginator.page(page)
    except EmptyPage:
        announcements = paginator.page(paginator.num_pages)
    args = {'announcements': announcements}
    return render(request, 'tag/announcement_tag.html', args)


def news_tag(request, tag_name):
    """ View for news tag listing """
    news = News.get_news_tag(tag_name)
    paginator = Paginator(news, 10)

    page = request.GET.get('page', default=1)
    try:
        news = paginator.page(page)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    args = {'news': news}
    return render(request, 'tag/news_tag.html', args)


def picture_tag(request, tag_name):
    """ View for picture tag listing """
    images = PhotoExtended.get_photo_tag(tag_name)
    paginator = Paginator(images, 10)

    page = request.GET.get('page', default=1)
    try:
        images = paginator.page(page)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    args = {'images': images}
    return render(request, 'tag/picture_tag.html', args)
