# simple_test_root/pages/views.py

from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    return HttpResponse(pg.bodytext)

def about(request):
    pg = Page.objects.get(permalink='/about')
    return HttpResponse(pg.bodytext)

def extra(request):
    pg = Page.objects.get(permalink='/extra')
    return HttpResponse(pg.bodytext)

