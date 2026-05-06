from django.shortcuts import render
from datetime import datetime
def vijay(request):
    context={'data':'Welcome here'}
    return render(request, 'course/vijay.html',context)

def dj(request):
    course={'cname':'Django Beginner to Pro','Duration':'90 Days'}
    return render(request,'course/django.html',course)


def fast(request):
    return render(request,'course/fastapi.html',{'coursename':'FAST API'})

def learnPython(request):
    name='Python Programming Course'
    Duration='3months'
    seats=90
    
    dt=datetime.now()
    c_d={'nm':name,'d':Duration,'st':seats,'dt':dt}
    return render(request,'course/python.html',c_d)