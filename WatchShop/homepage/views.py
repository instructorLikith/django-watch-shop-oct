from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("Hi ! This is Home Page")

def About(request):
    return HttpResponse("This is our About Page")