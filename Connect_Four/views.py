from django.shortcuts import render

# Create your views here.
def connect_four(request):
    return render(request,'connect_four.html')