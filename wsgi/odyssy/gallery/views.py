from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from photologue.models import Photo, Gallery


class IndexView(generic.ListView):
	template_name = 'gallery/gallery_list.html'
	model = Gallery

class DetailView(generic.DetailView):
	template_name = 'gallery/gallery_detail.html'
	model = Gallery