from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def math(request):
    a=10
    b=20
    return HttpResponse(a+b)
