
from django.contrib import admin
from django.urls import path, include
from . import views
# from .views import displaycsv

urlpatterns = [
    path('weather/', views.index, name='index'),
    
]
   