from django.shortcuts import render


def view_institute(request):
    print(request)
    return render(request, request.path[1:])
