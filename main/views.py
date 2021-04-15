from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
import requests
import numpy as np
import tweepy
import threading
import re
import os
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd


import requests
from requests.auth import HTTPBasicAuth

from datetime import datetime

from main.models import *

import smtplib
from smtplib import *

# Create your views here.

from .forms import CreateUserForm


found = {"search": 0, "instagram": 0, "twitter": 0, "github": 0,
         "linkedin": 0, "codeforces": 0, "facebook": 0, "reddit": 0}
data_codeforces = {}
data_github = {}
data_twitter = {}
data_instagram = {}
data_reddit = {}


def homepage(request):
    context = {}
    if request.method == 'POST':
        if request.user.is_authenticated:
            print("Logged in")
            user = request.POST.get('username')
            data_codeforces.clear()
            data_github.clear()
            data_twitter.clear()
            found = check(user)
            context = {"found": found}
            return render(request, "home.html", context)
        else:
            print("Not logged in")
            return redirect('main:login')

    return render(request, "home.html", context)


def check(user):
    for key in found:
        found[key] = 0
    # Codeforces
    data = requests.get('https://codeforces.com/api/user.info?handles=' + user)
    data = data.json()
    if data['status'] == "OK":
        found["codeforces"] = 1
        data = data['result'][0]
        ts = int(data['lastOnlineTimeSeconds'])
        data['lastOnlineTimeSeconds'] = datetime.utcfromtimestamp(
            ts).strftime('%H:%M:%S  %d-%m-%Y')
        ts = int(data['registrationTimeSeconds'])
        data['registrationTimeSeconds'] = datetime.utcfromtimestamp(
            ts).strftime('%H:%M:%S  %d-%m-%Y')
        data_codeforces.clear()
        for key in data:
            data_codeforces[key] = data[key]
        try:
            add = codeforces_data(organisation=data['organisation'], city=data['city'], country=data['country'],
                                  first_name=data['firstName'], last_name=data['lastName'], handle=data['handle'],
                                  reg_time=data['registrationTimeSeconds'], last_online=data['lastOnlineTimeSeconds'],
                                  friends=data['friendOfCount'], link='https://codeforces.com/profile/' +
                                  data['handle'],
                                  max_rank=data['maxRank'], max_rating=data['maxRating'], rank=data['rank'], rating=data['rating'])
            add.save()
        except:
            add = codeforces_data(handle=data['handle'], reg_time=data['registrationTimeSeconds'],
                                  last_online=data['lastOnlineTimeSeconds'], friends=data['friendOfCount'],
                                  link='https://codeforces.com/profile/' + data['handle'])
            add.save()

    # Github
    credentials = {"username": "spotr-se", "password": "spotrisnumber1"}
    authentication = HTTPBasicAuth(
        credentials['username'], credentials['password'])
    data = requests.get('https://api.github.com/users/' +
                        user, auth=authentication)
    data = data.json()

    try:
        if(data["message"] == 'Not Found'):
            found["github"] = 0
    except:
        found["github"] = 1
        data_github.clear()
        for key in data:
            data_github[key] = data[key]
        add = github_data(name=data['name'], login=data['login'], bio=data['bio'], location=data['location'],
                          followers=data['followers'], following=data['following'], public_repos=data['public_repos'],
                          created_at=data['created_at'], updated_at=data['updated_at'], link='https://github.com/' + data['login'])
        add.save()

    # Instagram
    url = "https://instagram40.p.rapidapi.com/account-info"

    querystring = {"username":user}

    headers = {
        'x-rapidapi-key': "ded0e36c2cmshe89f61756dc618cp142d1cjsn48c1977bfb91",
        'x-rapidapi-host': "instagram40.p.rapidapi.com"
        }

    data = requests.request("GET", url, headers=headers, params=querystring)
    data=data.json()
    try:
        if(data["status"] == 'fail'):
            found["instagram"] = 0
    except:
        found["instagram"] = 1
        data_instagram.clear()
        for key in data:
            data_instagram[key] = data[key]
        add = instagram_data(name=data['full_name'],user_name=data['username'],bio=data['biography'],follower=data['edge_followed_by']['count'],following=data['edge_follow']['count'],link="https://www.instagram.com/" + data['username'], posts=data['edge_owner_to_timeline_media']['count'] , private= data['is_private'])
        add.save()

    # Twitter
    consumer_key = "FD9TutCsyTjewPgwptwwBMSAd"
    consumer_secret = "D2BNZf0rt1KLBx0hofRjX7vqIsGI9lTxp2gPRvVtq2ZuAvj4lT"
    access_token = "832235344527388672-rwia0zreGAtm92wXgHryhHVRWFMnhx9"
    access_token_secret = "4Oc10vpIBdkTR3AxTQYDUZ0bAXNKEzDlmSjZdJjDgkq3g"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        user_data = api.get_user('@' + user)
        data = user_data._json
        #Sentiment Analysis
        twetterApi = tweepy.API(auth, wait_on_rate_limit = True)
        tweets = tweepy.Cursor(twetterApi.user_timeline, 
                                screen_name="@" + user, 
                                count=None,
                                since_id=None,
                                max_id=None,
                                trim_user=True,
                                exclude_replies=True,
                                contributor_details=False,
                                include_entities=False
                                ).items(50);

        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweet'])

        # Cleaning the tweets

        def cleanUpTweet(txt):
            # Remove mentions
            txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)
            # Remove hashtags
            txt = re.sub(r'#', '', txt)
            # Remove retweets:
            txt = re.sub(r'RT : ', '', txt)
            # Remove urls
            txt = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', txt)
            return txt

        df['Tweet'] = df['Tweet'].apply(cleanUpTweet)
        df = df.drop(df[df['Tweet'] == ''].index)
        # print(df.head(50))

        def getTextSubjectivity(txt):
            return TextBlob(txt).sentiment.subjectivity

        def getTextPolarity(txt):
            return TextBlob(txt).sentiment.polarity
        df['Subjectivity'] = df['Tweet'].apply(getTextSubjectivity)
        df['Polarity'] = df['Tweet'].apply(getTextPolarity)

        def getTextAnalysis(a):
            if a < 0:
                return "Negative"
            elif a == 0:
                return "Neutral"
            else:
                return "Positive"

        df['Score'] = df['Polarity'].apply(getTextAnalysis)
        positive = df[df['Score'] == 'Positive']
        data['positive_tweets'] =  int(positive.shape[0]/(df.shape[0])*100) 

        labels = df.groupby('Score').count().index.values
        values = df.groupby('Score').size().values
        plt.switch_backend('agg')
        plt.bar(labels, values)
        my_path = os.path.dirname(os.path.realpath(__file__))
        file_name = my_path +'\\static\\sentiment\\user_data\\' + user + '1.png'
        print(my_path)
        plt.savefig(file_name)  
        data['chart1'] = '../static/sentiment/user_data/' + user + '1.png'
        plt.switch_backend('agg')
        for index, row in df.iterrows():
            if row['Score'] == 'Positive':
                plt.scatter(row['Polarity'], row['Subjectivity'], color="green")
                print('green')
            elif row['Score'] == 'Negative':
                plt.scatter(row['Polarity'], row['Subjectivity'], color="red")
                print('red')
            elif row['Score'] == 'Neutral':
                plt.scatter(row['Polarity'], row['Subjectivity'], color="blue")
                print('blue')
        plt.title('Twitter Sentiment Analysis')
        plt.xlabel('Polarity')
        plt.ylabel('Subjectivity')
        file_name = my_path +'\\static\\sentiment\\user_data\\' + user + '2.png'
        plt.savefig(file_name)  
        data['chart2'] = '../static/sentiment/user_data/' + user + '2.png'
        plt.switch_backend('agg')
        objective = df[df['Subjectivity'] == 0]

        data['objective_tweets'] = int(objective.shape[0]/(df.shape[0])*100) 

        # Creating a word cloud
        words = ' '.join([tweet for tweet in df['Tweet']])
        wordCloud = WordCloud(width=600, height=400).generate(words)
        plt.switch_backend('agg')
        plt.imshow(wordCloud)
        file_name = my_path +'\\static\\sentiment\\user_data\\' + user + '3.png'
        plt.savefig(file_name)  
        data['chart3'] = '../static/sentiment/user_data/' + user + '3.png'
        plt.switch_backend('agg')
        data['profile_image_url'] = data['profile_image_url'].replace("normal", "400x400")
        print(data)

        for i in range(10):
            try: 
                data['tweet' + str(i) + 'tweet'] = df.loc[i]['Tweet']
                data['tweet' + str(i) + 'Subjectivity'] = df.loc[i]['Subjectivity']
                data['tweet' + str(i) + 'Polarity'] = df.loc[i]['Polarity']
                data['tweet' + str(i) + 'Score'] = df.loc[i]['Score']
            except:
                break
        found['twitter'] = 1
        data_twitter.clear()
        for key in data:
            data_twitter[key] = data[key]
        add = twitter_data(name=data['name'], screen_name=data['screen_name'], description=data['description'],
                           location=data['location'], follower_count=data['followers_count'], friend_count=data['friends_count'],
                           created_at=data['created_at'], verified=data['verified'], last_tweet=data['status']['text'],
                           last_tweet_time=data['status']['created_at'], link='https://twitter.com/' +
                           data['screen_name']
                           )
        add.save()
    except:
        found['twitter'] = 0


    # Reddit
    HEADERS = {"user-agent": "spotr:/u/blackhawk_2081"}
    link = 'https://www.reddit.com/user/' + user + '/about.json'
    data = requests.get(link, headers=HEADERS)
    data = data.json()

    try:
        if(data["message"] == 'Not Found'):
            found["reddit"] = 0
    except:
        found["reddit"] = 1
        try:
            ts = int(data['data']['created_utc'])
            data['data']['created_utc'] = datetime.utcfromtimestamp(
                ts).strftime('%H:%M:%S  %d-%m-%Y')
        except:
            data['data']['created_utc'] = "Date Created"   
        data_reddit.clear()
        for key in data:
            data_reddit[key] = data[key]
        add = reddit_data(name=data['data']['name'],total_karma=data['data']['total_karma'],
                          created_utc=data['data']['created_utc'])
        add.save()

    return found


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
        else:
            print(form.errors.as_json())
            dict1 = json.loads(form.errors.as_json())
            dict2 = {}
            for i in dict1:
                dict2[i] = dict1[i][0]['message']
            context = {'error' : dict2 , 'form' : form}
            return render(request, "register.html", context)
    context = {'form': form }
    return render(request, "register.html", context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:homepage')
        else:
            msg = {'err':'1' ,'msg': "Invalid Username or Password"}
            context = {'msg':msg}
            return render(request, "login.html", context)
    context = {}
    return render(request, "login.html", context)


def logoutuser(request):
    logout(request)
    return redirect('main:login')


def github(request):
    if(found['github'] == 1):
        context = {'data': data_github}
        return render(request, "github.html", context)
    else:
        data = {'name': 'Full Name', 'avatar_url' : '../static/home/assets/img/portfolio/github (2).png', 'login': 'Username', 'bio': 'Bio', 'location': 'Location', 'followers': 'Followers',
                'following': 'Following', 'public_repos': 'Public Repos', 'created_at': 'Time Created',
                'updated_at': 'Last Updated Time'}
        context = {'data': data}
        return render(request, "github.html", context)


def codeforces(request):
    if found['codeforces'] == 1:
        context = {'data': data_codeforces}
        return render(request, "codeforces.html", context)
    else:
        data = {'firstName': 'Full', 'titlePhoto' : '../static/home/assets/img/portfolio/codeforces (2).png' ,'lastName': 'Name', 'handle': 'Username', 'rank': 'Rank', 'organization': 'Organization',
                'city': 'City', 'country': 'Country', 'rating': 'Rating', 'maxRating': 'Max Rating', 'friendOfCount': 'Friend Count',
                'maxRank': 'Max Rank', 'lastOnlineTimeSeconds': 'Last Online Time', 'registrationTimeSeconds': 'Registration Time'}
        context = {'data': data}
        return render(request, "codeforces.html", context)


def instagram(request):
    if(found['instagram'] == 1):
        context = {'data': data_instagram}
        return render(request, "instagram.html", context)
    else:
        data = {'full_name': 'Full Name', 'profile_pic_url_hd' : '../static/home/assets/img/portfolio/instagram (2).png' ,'username': 'Username', 'biography': 'Biography', 'is_private': 'Private',
                'edge_followed_by': {'count': 'Followers'}, 'edge_follow': {'count': 'Following'},
                'edge_owner_to_timeline_media': {'count': 'Total Post'}}
        context = {'data': data}
        return render(request, "instagram.html", context)


def twitter(request):
    if(found['twitter'] == 1):
        context = {'data': data_twitter}
        return render(request, "twitter.html", context)
    else:
        data = {'name': 'Full Name', 'profile_image_url': '../static/home/assets/img/portfolio/twitter(2).png' ,'screen_name': 'Username', 'description': 'Description', 'location': 'Location',
                'verified': 'Verified', 'followers_count': 'Follower Count', 'friends_count': 'Friend Count', 'created_at': 'Created Time',
                'friendOfCount': 'Friend Count', 'status': {'created_at': 'Last Tweet Time', 'text': 'Last Tweet'}}
        context = {'data': data}
        return render(request, "twitter.html", context)


def reddit(request):

    if(found['reddit'] == 1):
        context = {'data': data_reddit}
        return render(request, "reddit.html", context)
    else:
        data = {'data': {'name': 'Name', 'icon_img' : '../static/home/assets/img/portfolio/reddit (2).png', 'subreddit': {'display_name': 'Display Name'}, 'public_description': 'Description', 'is_gold': 'Is GOLD',
                         'verified': 'Verified', 'total_karma': 'Total Karma', 'created_utc': 'Created At'}}
        context = {'data': data}
        return render(request, "reddit.html", context)


def sentiment(request):

    if(found['twitter'] == 1):
        context = {'data': data_twitter}
        return render(request, "sentiment.html", context)
    else:
        data = {'name': 'Full Name', 'screen_name': 'Username', 'description': 'Description', 'location': 'Location',
                'verified': 'Verified', 'followers_count': 'Follower Count', 'friends_count': 'Friend Count', 'created_at': 'Created Time',
                'friendOfCount': 'Friend Count', 'status': {'created_at': 'Last Tweet Time', 'text': 'Last Tweet'}}
        context = {'data': data}
        return render(request, "sentiment.html", context)
