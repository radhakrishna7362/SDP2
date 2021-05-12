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
    path('prequest/', views.prequest, name='prequest'),
    path('porders/', views.porders, name='porders'),
    path('corders/', views.corders, name='corders'),
    path('approve/<int:id>', views.approve, name='approve'),
    path('pick/<int:id>', views.pick, name='pick'),
    path('ship/<int:id>', views.ship, name='ship'),
    path('transit/<int:id>', views.transit, name='transit'),
    path('receive/<int:id>', views.receive, name='receive'),
    path('out_for_delivery/<int:id>', views.out_for_delivery, name='out_for_delivery'),
    path('deliver/<int:id>', views.deliver, name='deliver'),
]