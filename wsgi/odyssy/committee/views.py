from django.http import Http404
from django.shortcuts import render
from .models import Committee
from itertools import chain


def view_institute(request):
    print(request)
    return render(request, request.path[1:])


def all_committee(request):
    committees_list = Committee.COMMITTEE_CHOICES[1:]
    committees = list()
    for i in committees_list:
        committees.append([i[0], i[1], "basic/images/" + str(i[0]) + ".png"])
    context = {
        'committees': committees
    }
    return render(request, 'committee/all_committee.html', context=context)


def single_committee(request, committee_name):
    print(committee_name)
    committee_list = [str(i[0]) for i in Committee.COMMITTEE_CHOICES[1:]]
    print(committee_list)
    if committee_name not in committee_list:
        raise Http404
    all_members = Committee.objects.filter(committee=committee_name)
    member_list = list(
        chain(
            all_members.filter(post='Chairman'),
            all_members.filter(post='Vice Chairman'),
            all_members.filter(post='Member'),
            all_members.filter(post='Member Secretary')
        )
    )
    for i in Committee.COMMITTEE_CHOICES[1:]:
        if i[0] == committee_name:
            committee_name = i[1]
            break
    context = {
        'member_list': member_list,
        'committee_name': committee_name,
    }
    return render(request, 'committee/committee_base.html', context=context)
