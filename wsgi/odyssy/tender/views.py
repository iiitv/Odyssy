from django.shortcuts import render, get_object_or_404
from .models import Tender


def view_tender(request):
    faculty_list = Tender.objects.filter(status='faculty')
    context = {'tender_list': faculty_list, 'status': 'Faculties'}
    return render(request, 'tender.html', context=context)
