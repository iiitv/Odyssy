from django.shortcuts import render
from academic.models import Course, Programme


def all_programme(request):
    programmes = Programme.objects.all().order_by('name')
    context = {
        'btech': programmes.filter(name='B.Tech'),
        'mtech': programmes.filter(name='M.Tech'),
        'phd': programmes.filter(name='Ph.D.')
    }
    return render(request, 'academic/all_programme.html', context=context)


def single_programme(request, name, branch):
    programme = Programme.objects.filter(name=name, branch_code=branch)
    sems_list = list()
    sems = 8 if name == 'B.Tech' else 4
    for i in range(1, sems+1):
        temp = list()
        temp.append(i)
        course = Course.objects.filter(programme=programme, semester=str(i))
        temp.append(course)
        sems_list.append(temp)
    context = {
        'programme': programme[0],
        'semesters': sems_list
    }
    return render(request, 'academic/single_programme.html', context=context)


def single_course(request, name, branch, semester, course_code):
    programme = Programme.objects.filter(name=name, branch_code=branch)
    courses = Course.objects.filter(programme=programme, semester=semester, code=course_code)
    context = {
        'courses': courses,
        'programme': programme[0],
        'semester': semester
    }
    return render(request, 'academic/single_course.html', context=context)


def view_phd(request, name):
    programme = Programme.objects.filter(name=name)
    courses = Course.objects.filter\
        (programme=programme)
    context = {
        'courses': courses
    }
    return render(request, 'academic/phd_courses.html', context=context)
