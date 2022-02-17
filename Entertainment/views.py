from django.shortcuts import render

# Create your views here.
def entertainment(request):
    return render(request,'entertainment.html')