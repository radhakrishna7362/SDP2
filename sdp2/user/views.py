from django.shortcuts import render,HttpResponse, redirect
from .forms import LoginForm,SignUpForm,DeliveryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticate_user

# Create your views here.
@login_required(login_url='login/')
def home(request):
    if request.method == "POST":
        filledform = DeliveryForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('userhome')
        else:
            form = DeliveryForm()
            message = "Try Again"
            username = request.user.get_username()
            return render(request,"user/index.html",{
                'username':username,
                'form':form,
                'message': message,
            })
    else:
        username = request.user.get_username()
        initial_dict = {
            "user" : username,
            "source" : None,
            "destination":None,
        }
        form = DeliveryForm(initial=initial_dict)
        return render(request, "user/index.html",{
            'username':username,
            'form':form
        })

@unauthenticate_user
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
            return render(request,"user/login.html",{
                'form':form,
                'message': message
            })
    form = LoginForm()
    return render(request,"user/login.html",{
        'form':form
    })

@unauthenticate_user
def register_view(request):
    if request.method == "POST":
        filledform = SignUpForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return redirect('userhome')
        else:
            form = SignUpForm()
            username = request.user.get_username()
            return render(request, "user/register.html",{
                'form':form,
                'message':"Please Try Again."
            })
    form = SignUpForm()
    return render(request, "user/register.html",{
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('userhome')