from django.shortcuts import render

# Create your views here.
def tic_tac_toe(request):
    return render(request,'tic_tac_toe.html')