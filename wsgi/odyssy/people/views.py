from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import People


def faculty(request):
    faculty_list = People.objects.filter(status='faculty')
    visiting_faculty_list = People.objects.filter(status='visiting_faculty')
    former_faculty_list = People.objects.filter(status='former_faculty')
    people = []
    people.extend(faculty_list)
    people.extend(visiting_faculty_list)
    people.extend(former_faculty_list)
    context = {'people_list': people, 'status': 'Faculties'}
    return render(request, 'people.html', context=context)


def former_faculty(request):
    former_faculty_list = People.objects.filter(status='former_faculty')
    context = {'people_list': former_faculty_list, 'status': 'Former Faculties'}
    return render(request, 'people.html', context=context)


def visiting_faculty(request):
    visiting_faculty_list = People.objects.filter(status='visiting_faculty')
    context = {'people_list': visiting_faculty_list,
               'status': 'Mentor Institute Faculty Members'}
    return render(request, 'people.html', context=context)


def staff(request):
    staff_list = People.objects.filter(status='staff')
    context = {'people_list': staff_list, 'status': 'Staff'}
    return render(request, 'people.html', context=context)


def phd(request):
    administration_list = People.objects.filter(status='phd')
    context = {'people_list': administration_list, 'status': 'PhD Scholars'}
    return render(request, 'people.html', context=context)


def details(request, slug):
    person = get_object_or_404(People, slug=slug)
    context = {'person': person}
    return render(request, 'person.html', context=context)


def filter_by_tag(request, tag):
    tagged_people = People.get_people_sorted(tag)
    context = {'people_list': tagged_people,
               'status': 'People with tags : ' + tag}
    return render(request, 'people.html', context=context)
