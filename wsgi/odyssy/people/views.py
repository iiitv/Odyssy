from django.shortcuts import render, get_object_or_404
from .models import People


def faculty(request):
    people_list = People.objects.filter(status='faculty')
    context = {'people_list': people_list, 'status': 'Faculty'}
    return render(request, 'people.html', context=context)


def visiting_faculty(request):
    people_list = People.objects.filter(status='visiting_faculty')
    context = {'people_list': people_list, 'status': 'Mentor Institute Faculty Members'}
    return render(request, 'people.html', context=context)


def staff(request):
    people_list = People.objects.filter(status='staff')
    context = {'people_list': people_list, 'status': 'staff'}
    return render(request, 'people.html', context=context)


def details(request, slug):
    person = get_object_or_404(People, slug=slug)
    context = {'person': person}
    return render(request, 'person.html', context=context)
