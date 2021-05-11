from django.contrib import admin
from django.urls import path
from datlien import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('viewHubs/', views.viewHubs, name='viewHubs'),
    path('viewCentralHubs/', views.viewCentralHubs, name='viewCentralHubs'),
    path('addHub/', views.addHub, name='addHub'),
    path('addCentralHub/', views.addCentralHub, name='addCentralHub'),
    path('editCentralHub/<str:username>', views.editCentralHub, name='editCentralHub'),
    path('editHub/<str:username>', views.editHub, name='editHub'),
    path('drequest', views.drequest, name='drequest'),
    path('crequest', views.crequest, name='crequest'),
]