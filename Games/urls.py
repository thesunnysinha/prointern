from django.urls import path
from Games import views

urlpatterns = [
    path('',views.games,name = 'games')
]
