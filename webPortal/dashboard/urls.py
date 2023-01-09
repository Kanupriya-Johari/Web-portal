from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index,name='index'),
    path('papers/',views.papers,name='papers'),
    path('patents/',views.patents,name='patents'),

]