from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('check', views.check),
    path('view/', views.view),
]