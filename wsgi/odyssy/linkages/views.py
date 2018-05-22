from basic import utils

from django.shortcuts import render
from .models import Linkages


def linkage(request):
    links_list = Linkages.get_all_linkages()
    links_context, num_items, page = utils.paginate_view(request, links_list)
    context = {
        'link_list': links_context,
        'num_items': num_items,
        'curr_page': page
    }
    return render(request, 'linkages/linkages.html', context=context)


def linkage_detail(request, link_id):
    single_link = Linkages.get_single_link(link_id)
    context = {
        'link': single_link
    }
    return render(request, 'linkages/linkage_single.html', context=context)
