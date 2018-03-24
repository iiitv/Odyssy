from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import response
from .serializers import PeopleSerializer
from people.models import People


class AdministrationList(ListAPIView):
    """ Staff list view """
    queryset = People.objects.filter(status='administrative')
    serializer_class = PeopleSerializer


class FacultyList(ListAPIView):
    """ Faculty list view """
    queryset = People.objects.filter(status='faculty')
    serializer_class = PeopleSerializer


class VisitingFacultyList(ListAPIView):
    """ Visiting faculty list view """
    queryset = People.objects.filter(status='visiting_faculty')
    serializer_class = PeopleSerializer


class StaffList(ListAPIView):
    """ Staff list view """
    queryset = People.objects.filter(status='staff')
    serializer_class = PeopleSerializer


class Details(APIView):
    """ Details list view """

    def get(self, request, slug):
        person = get_object_or_404(People, slug=slug)
        serializer = PeopleSerializer(person, many=False)
        return response.Response(serializer.data)


class TaggedPeople(APIView):
    """ Details list view """

    def get(self, request, tag):
        person = People.get_people_sorted(tag)
        serializer = PeopleSerializer(person, many=True)
        return response.Response(serializer.data)
