from django.shortcuts import render


def view_careers(request):
    print(request)
    return render(request, request.path[1:])

