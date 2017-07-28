from django.shortcuts import render
from django.views import generic
from photologue.models import Gallery



def view_more(request):
    print(request)
    return render(request, request.path[1:])

class IndexView(generic.ListView):
    template_name = 'more/student_corner.html'
    model = Gallery

class DetailView(generic.DetailView):
    template_name = 'more/student_corner_view.html'
    model = Gallery

