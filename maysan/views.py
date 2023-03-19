from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import User, Message

import datetime

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
            user = User.objects.filter(email=email)
            id = user.values_list('id')[0][0]
            messages.success(request, "Registration with success.")
            return redirect('home', id=id)
    return render(request, "register.html", context={})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).exists()
        if user == True:
            user = User.objects.filter(email=email)
            id = user.values_list('id')[0][0]
            # print("-----------------", user.values_list('id')[0][0])
            # print(user.User)
            messages.success(request, "Login with success.")
            return redirect('home', id=id)
        else:
            messages.error(request, "User does not exist. - (or) Email or password is not invalid.")
    return render(request, "login.html", context={})


def home(request, id):
    # print("--------home id:", id)
    from_msg = []
    to_msg = []
    user = User.objects.filter(id=id)
    email = user.values_list('email')[0][0]
    name = user.values_list('name')[0][0]
    fmsg = Message.objects.filter(from_msg=id)
    tmsg = Message.objects.filter(to_msg=id)
    print("from:", fmsg)
    print("to:", tmsg)
    for f in fmsg:
        print
        userf = User.objects.filter(id=f.from_msg)
        usert = User.objects.filter(id=f.to_msg)
        from_msg.append({
            "id": f.id,
            "from_name": userf.values_list('name')[0][0],
            "from_email": userf.values_list('email')[0][0],
            "to_name": usert.values_list('name')[0][0],
            "to_email": usert.values_list('email')[0][0],
            "subject": f.object_message,
            "content": f.content,
            "date": f.date_time,
            "seen": f.seen,
        })
    for t in tmsg:
        userf = User.objects.filter(id=t.from_msg)
        usert = User.objects.filter(id=t.to_msg)
        from_msg.append({
            "id": t.id,
            "from_name": userf.values_list('name')[0][0],
            "from_email": userf.values_list('email')[0][0],
            "to_name": usert.values_list('name')[0][0],
            "to_email": usert.values_list('email')[0][0],
            "subject": t.object_message,
            "content": t.content,
            "date": t.date_time,
            "seen": t.seen,
        })
    context = {
        "user_id": id,
        "user_email": email,
        "user_name": name,
        "from_msg": from_msg,
        "to_msg": to_msg,
        "from": len(from_msg),
        "to": len(to_msg),
    }
    if request.method == 'POST':
        valid = True
        to = request.POST['to']
        subject = request.POST['subject']
        content = request.POST['content']
        if User.objects.filter(email=to).exists() == False:
            messages.error(request, "This email '" + to + "' does not exist.")
            valid = False
        if valid == True:
            date = datetime.datetime.now()
            usert = User.objects.filter(email=to)
            print("from_msg:", id)
            print("to_msg:", usert.values_list('id')[0][0])
            print("object_message:", subject)
            print("content:", content)
            print("date:", date)
            print("seen:", False)
            new_message = Message(from_msg=id, to_msg=usert.values_list('id')[0][0], object_message=subject, content=content, date_time=date, seen=False)
            new_message.save()
            messages.success(request, "Email sent with success.")
        # print("to:", to)
        # print("subject:", subject)
        # print("content:", content)
    return render(request, "home.html", context)

def email(request):
    data = {}
    return render(request, "email.html", context=data)