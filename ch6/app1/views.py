from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myfunction(request):
    return HttpResponse('hello Vijay')

def home(request):
    return HttpResponse('Homepage')

def learn_django(request):
    return HttpResponse('<h1>This is Django</h1>')