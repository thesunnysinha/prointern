from django.urls import path,include
from Myself import views

urlpatterns=[
    path('',views.myself,name = 'myself'),
]