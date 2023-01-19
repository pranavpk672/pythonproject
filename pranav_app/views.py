
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.
def register(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            nm= a.cleaned_data['name']
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            cp= a.cleaned_data['cpassword']
            ph=a.cleaned_data['phone']

            if(ps==cp):
                b=regmodel(name=nm,email=em,password=ps,phone=ph)
                b.save()

                return redirect(login)
            else:
                return HttpResponse("failed")
        else:
            return HttpResponse("enter coorect values")
    else:
        return render(request,'registration.html')



def login(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']

            b=regmodel.objects.all()
            for i in b:
                if em==i.email and ps==i.password:
                     return  render(request,'home.html')

            else:
                return HttpResponse("login failed2")

    else:
        return render(request,"login.html")

def logoutpage(request):

    return redirect(login)

