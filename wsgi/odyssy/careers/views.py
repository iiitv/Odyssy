from django.shortcuts import render
from .models import Career


def view_careers(request):
    careers = Career.get_active_career()
    status = 'All recruitment releases'
    return render(request, 'careers/careers.html', {'careers': careers})
