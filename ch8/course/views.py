from django.shortcuts import render

def vijay(request):
    context={'data':'Welcome here'}
    return render(request, 'course/vijay.html',context)

def dj(request):
    course={'cname':'Django Beginner to Pro','Duration':'90 Days'}
    return render(request,'course/django.html',course)


def fast(request):
    return render(request,'course/fastapi.html',{'coursename':'FAST API'})