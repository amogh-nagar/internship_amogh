from django.shortcuts import render, redirect
from datetime import datetime
from app.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import logout, authenticate, login
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, "index.html")
    messages.success(request, 'YOUR MESSAGE HAS BEEN SENT')
    # return HttpResponse('This is homepage')


def services(request):
    return render(request, "services.html")
    # return HttpResponse('This is servicespage')


def about(request):
    return render(request, "about.html")
    # return HttpResponse('This is aboutpage')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'YOUR MESSAGE HAS BEEN SENT')
    return render(request, "contact.html")
    # return HttpResponse('This is contactpage')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
            messages.success(request, 'YOUR MESSAGE HAS BEEN SENT')
    # A backend authenticated the credentials
        else:
            return render(request, 'login.html')

    # No backend authenticated the credentials

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')
