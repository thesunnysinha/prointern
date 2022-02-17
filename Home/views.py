from django.shortcuts import render

# Create your views here.
def prointern(request):
    return render(request, 'prointern.html',{})