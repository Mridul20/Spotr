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

from datetime import datetime

# Create your views here.

from .forms import CreateUserForm
cars = []
def homepage(request):
    context = {}
    if request.method == 'POST':   
        if request.user.is_authenticated:
            print("Logged in")
            user = request.POST.get('username')
            cars.append(user)
            found = check(user)
            context = {"found" : found}
            return render(request, "home.html", context)
        else:
            print("Not logged in")
            return redirect('main:login') 
                
    return render(request, "home.html", context)

def check(user):

    found = {"search" : 0 , "instagram" : 0,"twitter" : 0,"github" : 0,"linkedin" : 0,"codeforces" : 0,"facebook" : 0}
    #Codeforces
    data = requests.get('https://codeforces.com/api/user.info?handles=' + user)
    data = data.json()
    if data['status'] == "OK":
        found["codeforces"] = 1
    #Github
    credentials = {"username" : "spotr-se" , "password" : "spotrisnumber1"}
    authentication = HTTPBasicAuth(credentials['username'], credentials['password'])
    data = requests.get('https://api.github.com/users/' + user, auth = authentication)
    data = data.json()
    try:
        if(data["message"] == 'Not Found'):
            found["github"] = 0
    except:
        found["github"] = 1 
    # Instagram
    # url = "https://instagram40.p.rapidapi.com/account-info"

    # querystring = {"username":user}

    # headers = {
    #     'x-rapidapi-key': "7de9fb3e1cmshebc5993304d0035p116a4cjsn3ab4d2417fd4",
    #     'x-rapidapi-host': "instagram40.p.rapidapi.com"
    #     }

    # data = requests.request("GET", url, headers=headers, params=querystring)
    # data=data.json()
    # try:
    #     if(data["status"] == 'fail'):
    #         found["instagram"] = 0
    # except:
    #     found["instagram"] = 1 
    return found

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':    
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                print(msg)   


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
    data = requests.get('https://api.github.com/users/' + user, auth = authentication)
    data = data.json()
    print(data)
    context = {'data':data}
    return render(request, "github.html", context)

def codeforces(request):
    user = cars[-1]
    context = {}
    data = requests.get('https://codeforces.com/api/user.info?handles=' + user)
    data = data.json()
    if data['status'] == "OK":
        data = data['result'][0]
        ts = int(data['lastOnlineTimeSeconds'])
        data['lastOnlineTimeSeconds'] = datetime.utcfromtimestamp(ts).strftime('%H:%M:%S  %d-%m-%Y')
        ts = int(data['registrationTimeSeconds'])
        data['registrationTimeSeconds'] = datetime.utcfromtimestamp(ts).strftime('%H:%M:%S  %d-%m-%Y')
        context = {'data':data}
    return render(request, "codeforces.html", context)

def instagram(request):
    user = cars[-1]
    url = "https://instagram40.p.rapidapi.com/account-info"

    querystring = {"username":user}

    headers = {
        'x-rapidapi-key': "7de9fb3e1cmshebc5993304d0035p116a4cjsn3ab4d2417fd4",
        'x-rapidapi-host': "instagram40.p.rapidapi.com"
        }

    data = requests.request("GET", url, headers=headers, params=querystring)
    data=data.json()
    context = {'data':data}
    return render(request, "instagram.html", context)