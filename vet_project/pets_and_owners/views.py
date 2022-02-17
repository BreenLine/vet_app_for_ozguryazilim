from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("bu bir sayfa")


def about(request):
    return HttpResponse("about sayfası")