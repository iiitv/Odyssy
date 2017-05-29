from announcement.models import Announcement
from news.models import News

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage


def index(request):
    """ Index view """
    return render(request, 'tags/index.html')


def picture_tag(request, tag_name):
    return render(request, 'tags/pictures.html')


def announcement_tag(request, tag_name):
    """ Fetches announcements by tag """
    announcements = Announcement.get_announcement_tag(tag_name)
    paginator_announcement = Paginator(announcements, 10)
    page_announcement = request.GET.get('page_announcement', default=1)
    try:
        announcements = paginator_announcement.page(page_announcement)
    except EmptyPage:
        announcements = paginator_announcement.page(
            paginator_announcement.num_pages
            )
    args = {'announcements': announcements}
    return render(request, 'tags/announcements.html', args)


def news_tag(request, tag_name):
    """ Fetches news by tag """
    news = News.get_news_tag(tag_name)
    paginator_news = Paginator(news, 2)
    page_news = request.GET.get('page_news', default=1)
    try:
        news = paginator_news.page(page_news)
    except EmptyPage:
        news = paginator_news.page(paginator_news.num_pages)
    args = {'news': news}
    return render(request, 'tags/news.html', args)
