from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def learn_django(request,**kwargs):
    status=kwargs.get('status','Not Allowed')
    return HttpResponse(f'<h1>Learn Django{status} Running App1</h1>')