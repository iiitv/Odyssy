from django.shortcuts import render


def view_academic(request):
    print(request)
    return render(request, request.path[1:])
