from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sorna(request):
    return HttpResponse('<h1><marquee>sorna is very talented</marquee></h1>')