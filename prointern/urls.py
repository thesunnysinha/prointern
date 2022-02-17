"""prointern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Signin import views
from Home import views as views1

from django.views.static import serve
from django.conf.urls import url 

urlpatterns = [
    path('',views1.prointern,),
    path('prointern/',include('Home.urls')),
    path('signin/',include('Signin.urls')),
    path('signout/',views.signout,name = 'signout'),
    path('special/',views.special,name = 'special'),
    path('signup/',include('SignUp.urls')),
    path('myself/',include('Myself.urls')),
    path('games/',include('Games.urls')),
    path('connect_four/',include('Connect_Four.urls')),
    path('tic_tac_toe/',include('Tic_Tac_Toe.urls')),
    path('entertainment/',include('Entertainment.urls')),
    path('studymaterial/',include('StudyMaterial.urls')),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
