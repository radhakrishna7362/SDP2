from django.shortcuts import render,HttpResponse, redirect
from .forms import LoginForm,CentralHubForm,EditCentralHubForm,HubForm,EditHubForm,SignUpForm
from .models import CentralHub, Hub
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
@login_required(login_url="login/")
def home(request):
    username = request.user.get_username()
    superuser = request.user.is_superuser
    return render(request, "datlien/index.html",{
        'username':username,
        'superuser':superuser,
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

@login_required(login_url="login/")
def viewCentralHubs(request):
    central_hubs = CentralHub.objects.all()
    username = request.user.get_username()
    superuser = request.user.is_superuser
    return render(request, "datlien/viewCentralHubs.html",{
        'username':username,
        'central_hubs':central_hubs,
        'superuser':superuser,
    })

@login_required(login_url="login/")
def addCentralHub(request):
    if request.method == "POST":
        filledform = CentralHubForm(request.POST)
        if filledform.is_valid():
            filledform.save()          
            User.objects.create_user(filledform.cleaned_data['username'],filledform.cleaned_data['email'],filledform.cleaned_data['password'],is_staff=True)
            return redirect('home')
        else:
            form = CentralHubForm()
            username = request.user.get_username()
            superuser = request.user.is_superuser
            message = "Try Again"
            return render(request, "datlien/addCentralHub.html",{
                'form':form,
                'username':username,
                'message':message,
                'superuser':superuser
            })
    else:
        form = CentralHubForm()
        username = request.user.get_username()
        superuser = request.user.is_superuser
        return render(request, "datlien/addCentralHub.html",{
            'form':form,
            'username':username,
            'superuser':superuser
        })

@login_required(login_url="login/")
def editCentralHub(request,username):
    if request.method == "POST":
        central_hub = CentralHub.objects.get(username=username)
        filledform = EditCentralHubForm(request.POST,instance=central_hub)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
        else:
            form = EditCentralHubForm(instance=central_hub)
            username = request.user.get_username()
            superuser = request.user.is_superuser
            message = "Try Again"
            return render(request, "datlien/editCentralHub.html",{
                'form':form,
                'username':username,
                'message':message,
                'superuser':superuser
            })
    else:
        central_hub = CentralHub.objects.get(username=username)
        form = EditCentralHubForm(instance=central_hub)
        username=request.user.get_username()
        superuser = request.user.is_superuser
        return render(request,"datlien/editCentralHub.html",{
            'superuser':superuser,
            'form':form,
            'username':username,
        })

@login_required(login_url="login/")
def viewHubs(request):
    hubs = Hub.objects.all()
    username = request.user.get_username()
    superuser = request.user.is_superuser
    return render(request, "datlien/viewHubs.html",{
        'username':username,
        'hubs':hubs,
        'superuser':superuser,
    })

@login_required(login_url="login/")
def addHub(request):
    if request.method == "POST":
        filledform = HubForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            User.objects.create_user(filledform.cleaned_data['username'],filledform.cleaned_data['email'],filledform.cleaned_data['password'],is_staff=True)
            return redirect('home')
        else:
            form = HubForm()
            username = request.user.get_username()
            superuser = request.user.is_superuser
            message = "Try Again"
            return render(request, "datlien/addHub.html",{
                'form':form,
                'username':username,
                'message':message,
                'superuser':superuser,
            })
    else:
        form = HubForm()
        username = request.user.get_username()
        superuser = request.user.is_superuser
        return render(request, "datlien/addHub.html",{
            'form':form,
            'username':username,
            'superuser':superuser
        })

@login_required(login_url="login/")
def editHub(request,username):
    if request.method == "POST":
        hub = Hub.objects.get(username=username)
        filledform = EditHubForm(request.POST,instance=hub)
        if filledform.is_valid():
            filledform.save()
            return redirect('home')
        else:
            form = EditHubForm(instance=hub)
            username = request.user.get_username()
            superuser = request.user.is_superuser
            message = "Try Again"
            return render(request, "datlien/editHub.html",{
                'superuser':superuser,
                'form':form,
                'username':username,
                'message':message
            })
    else:
        hub = Hub.objects.get(username=username)
        form = EditHubForm(instance=hub)
        superuser = request.user.is_superuser
        username = request.user.get_username()
        return render(request,"datlien/editHub.html",{
            'form':form,
            'username':username,
            'superuser':superuser,
        })

@login_required(login_url="login/")
def drequest(request):
    superuser = request.user.is_superuser
    username = request.user.get_username()
    return render(request, "datlien/drequest.html",{
            'username':username,
            'superuser':superuser,
    })

@login_required(login_url="login/")
def crequest(request):
    superuser = request.user.is_superuser
    username = request.user.get_username()
    return render(request, "datlien/crequest.html",{
            'username':username,
            'superuser':superuser,
    })