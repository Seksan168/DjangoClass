from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def home(request):
    allproduct = Product.objects.all()
    content = {'pd':allproduct}
    return render(request, 'myapp/home.html',content)

def home2(request):
    return HttpResponse("<h2>Welcome to Home2!</h2>")

def about(request):
    return render(request, 'myapp/aboutus.html')