from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to our E-commerce Platform!")

# Create your views here.