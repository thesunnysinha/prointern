from django.contrib import admin
from django.urls import path
from SignUp import views


urlpatterns = [
    path('',views.signup,name = 'signup')
]