from django import forms
from .models import Hub,CentralHub
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

class CentralHubForm(forms.ModelForm):
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model = CentralHub
        fields = ['state','city','username','password','email','address']

class EditCentralHubForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CentralHub
        fields = ['state','city','email','password','address']

class HubForm(forms.ModelForm):
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    class Meta:
        model = Hub
        fields = ['central_hub','city','username','password','email','address']

class EditHubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = ['central_hub','city','email','password','address']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']