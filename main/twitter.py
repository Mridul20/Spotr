# import the module 
import tweepy 
import pandas as pd
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
import numpy as np
import json

# assign the values accordingly 
consumer_key = "FD9TutCsyTjewPgwptwwBMSAd" 
consumer_secret = "D2BNZf0rt1KLBx0hofRjX7vqIsGI9lTxp2gPRvVtq2ZuAvj4lT" 
access_token = "832235344527388672-rwia0zreGAtm92wXgHryhHVRWFMnhx9" 
access_token_secret = "4Oc10vpIBdkTR3AxTQYDUZ0bAXNKEzDlmSjZdJjDgkq3g" 

# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret) 

# calling the api 
api = tweepy.API(auth) 

# using get_user with id 
# _id = "@iefrgdhnfgderrgdhwergtfhre3rthycggrerxthfc"
# user = api.get_user(_id) 

# printing the name of the user 
twitterAccount = "@imVkohli"

twetterApi = tweepy.API(auth, wait_on_rate_limit = True)
tweets = tweepy.Cursor(twetterApi.user_timeline, 
                        screen_name=twitterAccount, 
                        count=None,
                        since_id=None,
                        max_id=None,
                        trim_user=True,
                        exclude_replies=True,
                        contributor_details=False,
                        include_entities=False
                        ).items(50);

df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweet'])


# print(df.head(50))

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

print(str(positive.shape[0]/(df.shape[0])*100) + " % of positive tweets")

labels = df.groupby('Score').count().index.values

values = df.groupby('Score').size().values

plt.bar(labels, values)
plt.show()

# for index, row in df.iterrows():
#     if row['Score'] == 'Positive':
#         plt.scatter(row['Polarity'], row['Subjectivity'], color="green")
#     elif row['Score'] == 'Negative':
#         plt.scatter(row['Polarity'], row['Subjectivity'], color="red")
#     elif row['Score'] == 'Neutral':
#         plt.scatter(row['Polarity'], row['Subjectivity'], color="blue")

# plt.title('Twitter Sentiment Analysis')
# plt.xlabel('Polarity')
# plt.ylabel('Subjectivity')
# # add legend
# plt.show()


# objective = df[df['Subjectivity'] == 0]

# print(str(objective.shape[0]/(df.shape[0])*100) + " % of objective tweets")

# # Creating a word cloud
# words = ' '.join([tweet for tweet in df['Tweet']])
# wordCloud = WordCloud(width=600, height=400).generate(words)

# plt.imshow(wordCloud)
# plt.savefig(twitterAccount + '.png')
# plt.show()

# print(df.head(50))