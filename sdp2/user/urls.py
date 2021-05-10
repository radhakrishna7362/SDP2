from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='userhome'),
    path('login/', views.login_view, name='userlogin'),
    path('register/', views.register_view, name='userregister'),
    path('logout/', views.logout_view, name='userlogout'),
]