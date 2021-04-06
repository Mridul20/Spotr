from django.test import SimpleTestCase
from main.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):
    
    def test_homepage_url_is_resolved(self):
        url = reverse("main:homepage")
        self.assertEqual(resolve(url).func,homepage)

    def test_login_url_is_resolved(self):
        url = reverse("main:login")
        self.assertEqual(resolve(url).func,loginpage)

    def test_register_url_is_resolved(self):
        url = reverse("main:register")
        self.assertEqual(resolve(url).func,register)
    
    def test_logout_url_is_resolved(self):
        url = reverse("main:logout")
        self.assertEqual(resolve(url).func,logoutuser)

    def test_github_url_is_resolved(self):
        url = reverse("main:github")
        self.assertEqual(resolve(url).func,github)

    def test_codeforces_url_is_resolved(self):
        url = reverse("main:codeforces")
        self.assertEqual(resolve(url).func,codeforces)


    def test_instagram_url_is_resolved(self):
        url = reverse("main:instagram")
        self.assertEqual(resolve(url).func,instagram)


    def test_twitter_url_is_resolved(self):
        url = reverse("main:twitter")
        self.assertEqual(resolve(url).func,twitter)
    

    def test_reddit_url_is_resolved(self):
        url = reverse("main:reddit")
        self.assertEqual(resolve(url).func,reddit)
    

    def test_sentiment_url_is_resolved(self):
        url = reverse("main:sentiment")
        self.assertEqual(resolve(url).func,sentiment)
    