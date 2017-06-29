from django.shortcuts import render, get_object_or_404
from .models import People


def faculty(request):
    faculty_list = People.objects.filter(status='faculty')
    context = {'people_list': faculty_list, 'status': 'Faculties'}
    return render(request, 'people.html', context=context)


def visiting_faculty(request):
    visiting_faculty_list = People.objects.filter(status='visiting_faculty')
    context = {'people_list': visiting_faculty_list, 'status': 'Mentor Institute Faculty Members'}
    return render(request, 'people.html', context=context)


def staff(request):
    staff_list = People.objects.filter(status='staff')
    context = {'people_list': staff_list, 'status': 'staff'}
    return render(request, 'people.html', context=context)


def administration(request):
    administration_list = People.objects.filter(status='administrative')
    context = {'people_list': administration_list, 'status': 'Administration'}
    return render(request, 'people.html', context=context)


def details(request, slug):
    person = get_object_or_404(People, slug=slug)
    context = {'person': person}
    return render(request, 'person.html', context=context)


def filter_by_tag(request, tag):
    tagged_people = People.get_people_sorted(tag)
    context = {'people_list': tagged_people, 'status': 'People with tags : ' + tag}
    return render(request, 'people.html', context=context)
