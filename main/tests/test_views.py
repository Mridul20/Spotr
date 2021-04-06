from main.views import *
from django.test import TestCase,Client
from django.urls import reverse,resolve
import json


class TestViews(TestCase):

    def setUp(self):
        self.client =  Client()
        self.home_url = reverse('main:homepage')
        self.login_url = reverse('main:login')
        self.register_url = reverse('main:register')
        self.logout_url = reverse('main:logout')
        self.github_url = reverse('main:github')
        self.codeforces_url = reverse('main:codeforces')
        self.instagram_url = reverse('main:instagram')
        self.twitter_url = reverse('main:twitter')
        self.reddit_url = reverse('main:reddit')
        self.sentiment_url = reverse('main:sentiment')

    def test_homepage_get(self):
        response = self.client.get(self.home_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
    
    def test_login_get(self):
        response = self.client.get(self.login_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def test_register_get(self):
        response = self.client.get(self.register_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')
    
    def test_logout_get(self):
        response = self.client.get(self.logout_url) 
        self.assertEquals(response.status_code,302) #302 status code for redirect urls 
        self.assertRedirects(response,'/login')

    def test_github_get(self):
        response = self.client.get(self.github_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'github.html')

    def test_codeforces_get(self):
        response = self.client.get(self.codeforces_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'codeforces.html')

    def test_instagram_get(self):
        response = self.client.get(self.instagram_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'instagram.html')

    def test_twitter_get(self):
        response = self.client.get(self.twitter_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'twitter.html')

    def test_reddit_get(self):
        response = self.client.get(self.reddit_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'reddit.html')
    
    def test_sentiment_get(self):
        response = self.client.get(self.sentiment_url) 
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'sentiment.html')