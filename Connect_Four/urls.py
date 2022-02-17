from django.urls import path
from Connect_Four import views

urlpatterns = [
    path('',views.connect_four,name='connect_four')
]