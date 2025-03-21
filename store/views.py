from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django .contrib.auth.forms import UserCreationForm
from django import forms


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

def about(request):
    return render(request, 'store/about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ("you have been logged in "))
            return redirect('home')
        else:
            messages.success(request, ("There was an error ..sorry.. "))
            return redirect('login')
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("you have been logged out .... Thanks"))
    return redirect('home')

def register_user(request):
    
    return render(request, 'store/register.html', {})
    
    