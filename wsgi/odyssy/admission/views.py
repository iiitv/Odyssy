from django.http import Http404
from django.shortcuts import render

from .models import Admission


def view_admission_programme(request, programme):
    print(programme)
    if programme != 'btech' and programme != 'mtech':
        raise Http404
    fee_struct = Admission.fetch_structures(programme)
    context = {
        'fee_struct': fee_struct,
    }
    return render(request,
                  'admission/' + programme + '.html',
                  context=context)


def view_admission(request):
    print(request)
    return render(request, request.path[1:])
