from django.contrib import admin
from django.urls import path

from myapp2.views import home
from myapp2.views import home2

urlpatterns = [
    path('',home),
    path('home2/',home2),
    
]
