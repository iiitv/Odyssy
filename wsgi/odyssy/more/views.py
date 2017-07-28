from django.shortcuts import render
<<<<<<< HEAD
=======
from django.views import generic
from photologue.models import Gallery
>>>>>>> eb917ae2a3adc9475a977b3c0203f822e3300117


def view_more(request):
    print(request)
<<<<<<< HEAD
    return render(request, request.path[1:])
=======
    return render(request, request.path[1:])

class IndexView(generic.ListView):
    template_name = 'more/student_corner.html'
    model = Gallery

class DetailView(generic.DetailView):
    template_name = 'more/student_corner_view.html'
    model = Gallery

>>>>>>> eb917ae2a3adc9475a977b3c0203f822e3300117
