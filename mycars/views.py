from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.conf import settings
# Create your views here.

def index(requests):
    return render(requests, 'mycars/index.html')

def contact(request):
    return render(requests, 'mycars/contact.html')

def about(request):
    return render(requests, 'mycars/about.html')

def service(request):
    return render(requests, 'mycars/service.html')

def news(requests):
    return render(requests, 'mycars/news.html')
    
    
    
    
    
