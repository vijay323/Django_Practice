from django.shortcuts import render

def vijay(request):
    context={'data':'Welcome here'}
    return render(request, 'course/vijay.html',context)