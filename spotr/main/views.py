from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
import requests
import numpy as np
import pandas as pd

import requests
from requests.auth import HTTPBasicAuth
# Create your views here.

from .forms import CreateUserForm
cars = []
def homepage(request):
    context = {}
    if request.method == 'POST':    
        user = request.POST.get('username')
        if request.user.is_authenticated:
            print("Logged in")
        else:
            print("Not logged in")
            return redirect('main:login')
        print("GET:" , user)
        cars.append(user) 
    return render(request, "home.html", context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':    
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')


    context = {'form':form} 
    return render(request, "register.html", context)

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')
        print(username)
        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('main:homepage')
        else:
            messages.info(request,"Invalid Username or Password")
    context = {}
    return render(request, "login.html", context)

def logoutuser(request):
    logout(request)
    return redirect('main:login')

def github(request):

    credentials = {"username" : "spotr-se" , "password" : "spotrisnumber1"}
    authentication = HTTPBasicAuth(credentials['username'], credentials['password'])
    user = cars[-1]
    print("GET2:" , user)
    data = requests.get('https://api.github.com/users/' + user, auth = authentication)
    data = data.json()
    context = {'data':data}
    return render(request, "github.html", context)
