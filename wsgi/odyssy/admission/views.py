from django.shortcuts import render

from .models import Admission


def view_btech_admission(request):
    fee_structure = Admission.objects.latest('fee_structure')
    context = {
        'fee_structure': fee_structure
    }
    return render(request,
                  'admission/btech_admission.html',
                  context=context)


def view_admission(request):
    print(request)
    return render(request, request.path[1:])
