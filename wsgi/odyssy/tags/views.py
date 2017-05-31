from announcement.models import Announcement
from news.models import News

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage


def index(request):
    """ Index view """
    return render(request, 'tags/index.html')


def picture_tag(request, tag_name):
    """ Fetches picture by tag """
    return render(request, 'tags/pictures.html')


def paginate(query_set, page_no, page_count):
    paginated_list = Paginator(query_set, page_count)
    try:
        page_data = paginated_list.page(page_no)
    except EmptyPage:
        page_data = paginated_list.page(paginated_list.num_pages)
    return page_data


def announcement_tag(request, tag_name):
    """ Fetches announcements by tag """
    announcements = Announcement.get_announcement_tag(tag_name)
    page_announcement = request.GET.get('page_announcement', default=1)
    announcements = paginate(announcements, page_announcement, 10)
    args = {'announcements': announcements}
    return render(request, 'tags/announcements.html', args)


def news_tag(request, tag_name):
    """ Fetches news by tag """
    news = News.get_news_tag(tag_name)
    page_news = request.GET.get('page_news', default=1)
    news = paginate(news, page_news, 2)
    args = {'news': news}
    return render(request, 'tags/news.html', args)


def normal_tag(request, tag_name):
    """ Fetches all the things from that tag """
    return render(request, 'tags/tag.html')
