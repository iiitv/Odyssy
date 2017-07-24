from django.shortcuts import render


def view_more(request):
    print(request)
    return render(request, request.path[1:])