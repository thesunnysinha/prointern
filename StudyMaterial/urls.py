from django.contrib import admin
from django.urls import path
from StudyMaterial import views

urlpatterns = [
    path('',views.studymaterial,name = 'studymaterial')
]