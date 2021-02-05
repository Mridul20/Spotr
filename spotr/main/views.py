from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

from .forms import CreateUserForm
def homepage(request):
    context = {}
    return render(request, "home.html", context)

def login(request):
    context = {}
    return render(request, "login.html", context)

def register(request):
    form = CreateUserForm()

    print("FORm")
    if request.method == 'POST':    
        print("poiuy")
        form = CreateUserForm(request.POST)
        print("FFWEWEFWE")
        if form.is_valid():
            form.save()
            return redirect('login')


    context = {'form':form}
    return render(request, "register.html", context)