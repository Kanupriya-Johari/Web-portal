from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login,name='login'),
    path('forgot/', views.forgot,name='forgot'),
    path('logout/', views.logout,name='logout'),
]