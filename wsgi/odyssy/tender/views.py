from django.shortcuts import render
from tender.models import Tender


def view_tender(request):
    tenders = Tender.get_all_active_tenders()
    context = {
        'tenders': tenders
        }
    return render(request, 'tender/tender.html', context=context)


def view_archive(request):
    tenders = Tender.get_archives()
    context = {
        'tenders': tenders
    }
    return render(request, 'tender/archive.html', context=context)
