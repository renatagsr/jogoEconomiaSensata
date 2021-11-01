from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return render(request, 'register.html')

def sigin(request):
    return render(request, 'sigin.html')

