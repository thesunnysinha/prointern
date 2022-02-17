from django.urls import path,include
from Entertainment import views

urlpatterns = [
    path('',views.entertainment,name = 'entertainment')
]