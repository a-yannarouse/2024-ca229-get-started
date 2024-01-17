# simple_test_root/pages/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Simple Test Site")

