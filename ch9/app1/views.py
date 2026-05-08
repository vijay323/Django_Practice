from django.shortcuts import render

# Create your views here.

def home(request):
    a=50
    b=60
    sum={'i1':a,'i2':b,'sum':a+b}
    return render(request,'app1/home.html',sum)