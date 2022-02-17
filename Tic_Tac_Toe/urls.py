from django.urls import path
from Tic_Tac_Toe import views

urlpatterns = [
    path('',views.tic_tac_toe,name='tic_tac_toe')
]