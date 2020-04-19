from django.contrib import admin
from django.urls import path,include

from django.http import HttpResponse
from .import views

urlpatterns = [
    path('', views.home,name="home"),

    path('work/', views.work, name="work"),
    path('about/', views.about, name="about"),
    path('services/', views.services,name="services"),

]
