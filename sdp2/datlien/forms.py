from django import forms
from .models import Hub,CentralHub

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput)

class CentralHubForm(forms.ModelForm):
    class Meta:
        model = CentralHub
        fields = '__all__'

class HubForm(forms.ModelForm):
    class Meta:
        model = Hub
        fields = '__all__'