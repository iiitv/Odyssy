from announcement.models import Announcement
from news.models import News
from basic.models import PhotoExtended
from basic import utils

from django.shortcuts import render


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
    announcements, num_items = utils.paginate_view(request, announcements)
    args = {'announcements': announcements, 'num_items': num_items,}
    return render(request, 'tag/announcement_tag.html', args)


def news_tag(request, tag_name):
    """ View for news tag listing """
    news = News.get_news_tag(tag_name)
    news, num_items = utils.paginate_view(request, news)
    args = {'news': news, 'num_items': num_items,}
    return render(request, 'tag/news_tag.html', args)


def picture_tag(request, tag_name):
    """ View for picture tag listing """
    images = PhotoExtended.get_photo_tag(tag_name)
    images, num_items = utils.paginate_view(request, images)
    args = {'images': images, 'num_items': num_items,}
    return render(request, 'tag/picture_tag.html', args)
