from django.shortcuts import render

# Create your views here.
def studymaterial(request):
    return render(request, 'study_material.html')