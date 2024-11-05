from django.contrib import admin
from django.urls import path
from .views import Home, About

urlpatterns = [
    path('home', Home , name ="home"),
    path('about', About , name ="about")
]
