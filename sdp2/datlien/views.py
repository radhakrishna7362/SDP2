from django.shortcuts import render,HttpResponse, redirect
from .forms import LoginForm,CentralHubForm,HubForm
from .models import CentralHub, Hub
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "datlien/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    form = LoginForm()
    return render(request,"datlien/login.html",{
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('login')

def addCentralHub(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        filledform = CentralHubForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
    else:
        form = CentralHubForm()
        username = request.user.get_username()
        return render(request, "datlien/addCentralHub.html",{
            'form':form
        })
    
def addHub(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        filledform = HubForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
    else:
        form = HubForm()
        username = request.user.get_username()
        return render(request, "datlien/addHub.html",{
            'form':form
        })