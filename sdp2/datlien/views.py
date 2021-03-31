from django.shortcuts import render,HttpResponse, redirect
from .forms import LoginForm,CentralHubForm,HubForm,SignUpForm
from .models import CentralHub, Hub
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# Create your views here.
@login_required(login_url="/login")
def home(request):
    username = request.user.get_username()
    return render(request, "datlien/index.html",{
        'username':username
    })

@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next'))
        else:
            form = LoginForm()
            message = "Invalid Login"
            return render(request,"datlien/login.html",{
                'form':form,
                'message': message
            })
    form = LoginForm()
    return render(request,"datlien/login.html",{
        'form':form
    })

@unauthenticated_user
def register_view(request):
    if request.method == "POST":
        filledform = SignUpForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
        else:
            form = SignUpForm()
            username = request.user.get_username()
            return render(request, "datlien/register.html",{
                'form':form,
                'message':"Please Try Again."
            })
    form = SignUpForm()
    return render(request, "datlien/register.html",{
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url="/login")
def viewHubs(request):
    hubs = Hub.objects.all()
    username = request.user.get_username()
    return render(request, "datlien/viewHubs.html",{
        'username':username,
        'hubs':hubs
    })

@login_required(login_url="/login")
def viewCentralHubs(request):
    central_hubs = CentralHub.objects.all()
    username = request.user.get_username()
    return render(request, "datlien/viewCentralHubs.html",{
        'username':username,
        'central_hubs':central_hubs
    })

@login_required(login_url="/login")
def addCentralHub(request):
    if request.method == "POST":
        filledform = CentralHubForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
        else:
            form = CentralHubForm()
            username = request.user.get_username()
            message = "Try Again"
            return render(request, "datlien/addCentralHub.html",{
                'form':form,
                'username':username,
                'message':message
            })
    else:
        form = CentralHubForm()
        username = request.user.get_username()
        return render(request, "datlien/addCentralHub.html",{
            'form':form,
            'username':username,
        })

@login_required(login_url="/login")
def addHub(request):
    if request.method == "POST":
        filledform = HubForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
        else:
            form = HubForm()
            username = request.user.get_username()
            message = "Try Again"
            return render(request, "datlien/addHub.html",{
                'form':form,
                'username':username,
                'message':message
            })
    else:
        form = HubForm()
        username = request.user.get_username()
        return render(request, "datlien/addHub.html",{
            'form':form,
            'username':username
        })