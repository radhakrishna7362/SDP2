from django.shortcuts import render,HttpResponse, redirect
from .forms import LoginForm,SignUpForm,DeliveryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import access_roles, unauthenticate_user
from .models import Delivery

# Create your views here.
@login_required(login_url='login/')
@access_roles
def home(request):
    if request.method == "POST":
        request.POST._mutable = True
        request.POST['user']=request.user.get_username()
        filledform = DeliveryForm(request.POST)
        if request.POST['source']==request.POST['destination']:
            message = "Source & Destination Shouldn't be the Same ❗"
            username = request.user.get_username()
            initial_dict = {
                "user" : username,
                "source" : None,
                "destination":None,
            }
            form = DeliveryForm(initial=initial_dict)
            history = Delivery.objects.filter(user=username)
            return render(request, "user/index.html",{
                'username':username,
                'form':form,
                'history':history,
                'message':message
            })
        if filledform.is_valid():
            filledform.save()
            return redirect('userhome')
        else:
            message = "Try Again"
            username = request.user.get_username()
            initial_dict = {
                "user" : username,
                "source" : None,
                "destination":None,
            }
            form = DeliveryForm(initial=initial_dict)
            history = Delivery.objects.filter(user=username)
            return render(request, "user/index.html",{
                'username':username,
                'form':form,
                'history':history,
                'message':message
            })
    else:
        username = request.user.get_username()
        initial_dict = {
            "user" : username,
            "source" : None,
            "destination":None,
        }
        form = DeliveryForm(initial=initial_dict)
        history = Delivery.objects.filter(user=username)
        return render(request, "user/index.html",{
            'username':username,
            'form':form,
            'history':history,
        })

@unauthenticate_user
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username , password=password)
        if user is not None:
            if user.is_staff:
                form = LoginForm()
                message = "Access Denied"
                return render(request,"user/login.html",{
                    'form':form,
                    'message': message
                })
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
            return redirect('userlogin')
        else:
            form = SignUpForm()
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