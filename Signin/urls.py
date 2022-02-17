from django.contrib import admin
from django.urls import path
from Signin import views

urlpatterns = [
    path('',views.signin,name = 'signin')
]