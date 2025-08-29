from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def home2(request):
    return HttpResponse("<h2>Welcome to Home2!</h2>")

