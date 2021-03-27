from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
import requests
import numpy as np
import tweepy 
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud


import requests
from requests.auth import HTTPBasicAuth

from datetime import datetime

from main.models import instagram_data
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
    url = "https://instagram40.p.rapidapi.com/account-info"

    querystring = {"username":user}

    headers = {
        'x-rapidapi-key': "7de9fb3e1cmshebc5993304d0035p116a4cjsn3ab4d2417fd4",
        'x-rapidapi-host': "instagram40.p.rapidapi.com"
        }

    data = requests.request("GET", url, headers=headers, params=querystring)
    data=data.json()
    try:
        if(data["status"] == 'fail'):
            found["instagram"] = 0
    except:
        found["instagram"] = 1 
        add = instagram_data(name=data['full_name'],user_name=data['username'],bio=data['biography'],follower=data['edge_followed_by']['count'],following=data['edge_follow']['count'],link="https://www.instagram.com/" + data['username'], posts=data['edge_owner_to_timeline_media']['count'] , private= data['is_private'])
        add.save()  

    consumer_key = "FD9TutCsyTjewPgwptwwBMSAd" 
    consumer_secret = "D2BNZf0rt1KLBx0hofRjX7vqIsGI9lTxp2gPRvVtq2ZuAvj4lT" 
    access_token = "832235344527388672-rwia0zreGAtm92wXgHryhHVRWFMnhx9" 
    access_token_secret = "4Oc10vpIBdkTR3AxTQYDUZ0bAXNKEzDlmSjZdJjDgkq3g" 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
    try :
        user = api.get_user('@' + user) 
        data = user._json
        found['twitter'] = 1
    except :
        found['twitter'] = 0
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

def twitter(request):
    user = cars[-1]
    context = {}
    consumer_key = "FD9TutCsyTjewPgwptwwBMSAd" 
    consumer_secret = "D2BNZf0rt1KLBx0hofRjX7vqIsGI9lTxp2gPRvVtq2ZuAvj4lT" 
    access_token = "832235344527388672-rwia0zreGAtm92wXgHryhHVRWFMnhx9" 
    access_token_secret = "4Oc10vpIBdkTR3AxTQYDUZ0bAXNKEzDlmSjZdJjDgkq3g" 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
    user = api.get_user('@' + user) 
    data = user._json
    # data['profile_image_url'] = re.findall(r'/^(.*?)\_normal/', data['profile_image_url']) + '_400x400.jpg'
    context = {'data':data}
    return render(request, "twitter.html", context)