from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.shortcuts import render
from . import forms
import json

def index(request):
    return render(request,'home/home.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('pruebaCRUD:index'))

def register(request):
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            auth_login(request, user)
            return HttpResponseRedirect(reverse('pruebaCRUD:index'))
        else:
            return HttpResponse(json.dumps(user_form.errors))
    else:
        return render(request, 'register/register.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('pruebaCRUD:index'))

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))

            return HttpResponse("Los datos de ingreso son incorrectos")
    else:
        return render(request, 'login/login.html', {})
