from django.shortcuts import render,HttpResponse, redirect
from .forms import LoginForm,CentralHubForm,HubForm,SignUpForm
from .models import CentralHub, Hub
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    username = request.user.get_username()
    return render(request, "datlien/index.html",{
        'username':username
    })

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

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        filledform = SignUpForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('login')
    else:
        form = SignUpForm()
    username = request.user.get_username()
    return render(request, "datlien/register.html",{
        'username':username,
        'form':form
    })


def viewHubs(request):
    if not request.user.is_authenticated:
        return redirect('login')

    hubs = Hub.objects.all()
    username = request.user.get_username()
    return render(request, "datlien/viewHubs.html",{
        'username':username,
        'hubs':hubs
    })

def viewCentralHubs(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    central_hubs = CentralHub.objects.all()
    username = request.user.get_username()
    return render(request, "datlien/viewCentralHubs.html",{
        'username':username,
        'central_hubs':central_hubs
    })

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
            'form':form,
            'username':username,
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
            'form':form,
            'username':username
        })