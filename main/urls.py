"""spotr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views


app_name = "main"

urlpatterns = [
    path('',views.homepage,name = "homepage"),
    path('login',views.loginpage,name = "login"),
    path('register',views.register,name = "register"),
    path('logout',views.logoutuser,name = "logout"),
    path('github',views.github,name = "github"),
    path('codeforces',views.codeforces,name = "codeforces"),
    path('instagram',views.instagram,name = "instagram"),
    path('twitter',views.twitter,name = "twitter"),
    path('reddit',views.reddit,name = "reddit"),
    path('sentiment',views.sentiment,name = "sentiment"),
]
