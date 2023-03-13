from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *

def index(request):
    data = {}
    return render(request, "index.html", context=data)


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    data = {'form': form}
    return render(request, "register.html", context=data)


def login(request):
    data = {}
    return render(request, "login.html", context=data)


def home(request):
    data = {}
    return render(request, "home.html", context=data)

def email(request):
    data = {}
    return render(request, "email.html", context=data)