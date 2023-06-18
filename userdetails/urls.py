from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path('trackmyloan', views.trackmyloan),

]
