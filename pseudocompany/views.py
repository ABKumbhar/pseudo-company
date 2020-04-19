from django.shortcuts import render
from django.urls import include
# Create your views here.
def home(request):
    return render(request,'pseudocompany/home.html')

def about(request):
    return render(request,'pseudocompany/about.html')


def work(request):
    return render(request,'pseudocompany/work.html')


def services(request):
    return render(request,'pseudocompany/services.html')
