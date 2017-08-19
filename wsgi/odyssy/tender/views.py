from django.shortcuts import render
from .models import Tender


def view_tender(request):
    tenders = Tender.get_all_tender()
    context = {
        'tenders': tenders
        }
    return render(request, 'tender/tender.html', context=context)
