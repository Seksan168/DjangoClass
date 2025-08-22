from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to MyApp!</h2>")

def home2(request):
    return HttpResponse("<h2>Welcome to Home2!</h2>")

