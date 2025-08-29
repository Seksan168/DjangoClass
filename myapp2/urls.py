from django.contrib import admin
from django.urls import path

from myapp2.views import home
from myapp2.views import home2
from myapp2.views import about

urlpatterns = [
    path('',home),
    path('home2/',home2),
    path('about/', about,name="about-page"),
    
]
