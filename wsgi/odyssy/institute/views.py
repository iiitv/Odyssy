from django.shortcuts import render
from .models import Institute
from itertools import  chain


def view_institute(request):
    print(request)
    return render(request, request.path[1:])


def view_building_works(request):
    all_members = Institute.objects.filter(committee='building-works')
    member_list = list(
        chain(
            all_members.filter(post='Chairman'),
            all_members.filter(post='Member'),
            all_members.filter(post='Member Secretary')
        )
    )
    context = {
        'member_list': member_list,
        'committee': 'Building And Works Committee'
    }
    return render(request, 'institute/committee/building-works.html', context=context)


def view_finance(request):
    all_members = Institute.objects.filter(committee='finance')
    member_list = list(
        chain(
            all_members.filter(post='Chairman'),
            all_members.filter(post='Member'),
            all_members.filter(post='Member Secretary')
        )
    )
    context = {
        'member_list': member_list,
        'committee': 'Finance Committee'
    }
    return render(request, 'institute/committee/finance.html', context=context)


def view_hr_planning(request):
    all_members = Institute.objects.filter(committee='hr-planning')
    member_list = list(
                  chain(
                      all_members.filter(post='Chairman'),
                      all_members.filter(post='Member'),
                      all_members.filter(post='Member Secretary')
                  )
    )
    context = {
        'member_list': member_list,
        'committee': 'HR Planning Committee'
    }
    return render(request, 'institute/committee/hr-planning.html', context=context)


def view_research_council(request):
    all_members = Institute.objects.filter(committee='research-council')
    member_list = list(
        chain(
            all_members.filter(post='Chairman'),
            all_members.filter(post='Vice Chairman'),
            all_members.filter(post='Member'),
            all_members.filter(post='Member Secretary')
        )
    )
    context = {
        'member_list': member_list,
        'committee': 'Research Council'
    }
    return render(request, 'institute/committee/research-council.html', context=context)


def view_strategic_planning(request):
    all_members = Institute.objects.filter(committee='strategic-planning')
    member_list = list(
        chain(
            all_members.filter(post='Chairman'),
            all_members.filter(post='Member'),
            all_members.filter(post='Member Secretary')
        )
    )
    context = {
        'member_list': member_list,
        'committee': 'Strategic Planning Committee'
    }
    return render(request, 'institute/committee/strategic-planning.html', context=context)

