
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

import smtplib
from smtplib import *

url = "https://instagram40.p.rapidapi.com/account-info"

user = "mridul_2008"
querystring = {"username":user}

headers = {
    'x-rapidapi-key': "7de9fb3e1cmshebc5993304d0035p116a4cjsn3ab4d2417fd4",
    'x-rapidapi-host': "instagram40.p.rapidapi.com"
    }

data = requests.request("GET", url, headers=headers, params=querystring)
data=data.json()
print(data)