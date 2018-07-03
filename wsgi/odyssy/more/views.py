from django.shortcuts import render
from django.views import generic
from photologue.models import Gallery

from basic import utils
from models import Talk


def view_more(request):
    print(request)
    return render(request, request.path[1:])


def invited_talks(request):
    talks = Talk.objects.all().order_by('-start_date')
    talks, num_items, page = utils.paginate_view(
        request, talks)
    context = {
        'talks_list': talks,
        'num_items': num_items,
        'curr_page': page,
    }
    return render(request, 'more/invited_talks.html', context)


class IndexView(generic.ListView):
    template_name = 'more/student_corner.html'
    model = Gallery


class DetailView(generic.DetailView):
    template_name = 'more/student_corner_view.html'
    model = Gallery
