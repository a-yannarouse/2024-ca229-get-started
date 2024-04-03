from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Area, Attraction
from django.urls import reverse_lazy

def geography_home(request):
    return HttpResponse("This is a simple page for the geography app.")

class AreaList(ListView):
    model = Area
    template_name = 'geography/area_list.html'

class AttractionList(ListView):
    model = Attraction
    template_name = 'geography/attraction_list.html'

class AreaCreate(CreateView):
    model = Area
    template_name = 'geography/area_create_form.html'
    fields = ["area_name", "area_type"]

class AreaDetail(DetailView):
    model = Area
    template_name = 'geography/area_detail.html'

class AreaUpdate(UpdateView):
    model = Area
    template_name = "geography/area_update_form.html"
    fields = ["area_name", "area_type"]

class AreaDelete(DeleteView):
    model = Area
    template_name = "geography/area_delete_form.html"
    success_url = reverse_lazy("arealist")


