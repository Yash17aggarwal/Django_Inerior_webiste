# from django.shortcuts import render, HttpResponse
from datetime import datetime
from shop.models import Contact,subscribe
from django.shortcuts import *
from django.contrib import messages



# Create your views here.

def Home(request):
    return render(request, 'Home.html')
def about(request):
    return render(request, 'About.html')
def Contac(request):
    if request.method=='POST':
        first_name=request.POST.get('first','1')
        last_name=request.POST.get('last','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        mess=request.POST.get('mess','')
        contac=Contact(first_name=first_name,last_name=last_name,email=email,subject=subject,mess=mess,date=datetime.now())
        contac.save()
        messages.success(request, "Your message is submitted")
    return render(request,'contact.html')

   # return HttpResponse("This is contact page")
def Bedroom(request):
    return render(request,'bed.html')
    # return HttpResponse("This is our bedrrom interior design page")

def Kitchen(request):
    return render(request,'kitchen.html')
def Hall(request):
    return render(request,'hall.html')

def sub(request):
    if request.method == 'POST':
        form = SubcribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SubcribersForm()

    context = {'form': form}
    return render(request, 'base.html', context)


