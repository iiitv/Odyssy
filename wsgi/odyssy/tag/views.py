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


def paginate_view(request, query_set, num_items):
    """ Paginates view from queryset """
    paginator = Paginator(query_set, num_items)
    page = request.GET.get('page', default=1)
    try:
        data_set = paginator.page(page)
    except EmptyPage:
        data_set = paginator.page(paginator.num_pages)
    return data_set


def announcement_tag(request, tag_name):
    """ View for announcement tag listing """
    announcements = Announcement.get_announcement_tag(tag_name)
    announcements = paginate_view(request, announcements, 10)
    args = {'announcements': announcements}
    return render(request, 'tag/announcement_tag.html', args)


def news_tag(request, tag_name):
    """ View for news tag listing """
    news = News.get_news_tag(tag_name)
    news = paginate_view(request, news, 10)
    args = {'news': news}
    return render(request, 'tag/news_tag.html', args)


def picture_tag(request, tag_name):
    """ View for picture tag listing """
    images = PhotoExtended.get_photo_tag(tag_name)
    images = paginate_view(request, images, 10)
    args = {'images': images}
    return render(request, 'tag/picture_tag.html', args)
