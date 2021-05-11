from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Delivery 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class DeliveryForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(), max_length=100)
    class Meta:
        model = Delivery
        fields = ['user', 'source', 'destination']