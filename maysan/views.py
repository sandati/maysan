from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import User, Message

def index(request):
    data = {}
    return render(request, "index.html", context=data)


def register(request):
    if request.method == 'POST':
        valid = True
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # user = User.objects.all()
        user = User.objects.filter(email=email).exists()
        if user == True:
            messages.info(request, "User already exist.")
            valid = False
        if email[-10:] != "@maysan.fr":
            print("email no valid")
            messages.error(request, "Email must be in this form 'example@maysan.fr'.")
            valid = False
        if valid == True:
            new_user = User(name=name, email=email, password=password)
            new_user.save()
            messages.success(request, "Registration with success.")
            return redirect('home')
    data = {}
    return render(request, "register.html", context=data)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).exists()
        if user == True:
            messages.success(request, "Login with success.")
            return redirect('home')
        else:
            messages.info(request, "User does not exist. - (or) Email or password is not invalid.")
    data = {}
    return render(request, "login.html", context=data)


def logout(request):
    pass


def home(request):
    data = {}
    return render(request, "home.html", context=data)

def email(request):
    data = {}
    return render(request, "email.html", context=data)