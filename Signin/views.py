from django.shortcuts import render
from Home import views
from SignUp.forms import UserProfileInfoForm,UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse 
from django.contrib.auth.decorators import login_required


# Create your views here.
def signin(request):

    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('prointern'))   
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username : {} and password {}".format(username,password))
            return HttpResponse("invalid signin detailes supplied!")
    else:
        return render(request, 'signin.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in , Nice!")

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('prointern'))