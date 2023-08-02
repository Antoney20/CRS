from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.conf import settings

from .models import UserProfile
# Create your views here.

def index(request):
    return render(request, 'mycars/index.html')

def contact(request):
    return render(request, 'mycars/contact.html')

def about(request):
    return render(request, 'mycars/about.html')

def service(request):
    return render(request, 'mycars/service.html')

def news(requests):
    return render(request, 'mycars/news.html')


# myapp/views.py

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')

        UserProfile.objects.create(
            email=email,
            password=password,
            user_type=user_type,
            full_name=full_name,
            phone_number=phone_number,
        )
        return redirect('index')

    return render(request, 'myapp/signup.html')

    
    
    
