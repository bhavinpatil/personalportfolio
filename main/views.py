from django.shortcuts import render,HttpResponse
from django.http import request
from datetime import datetime
from main.models import Contact
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is Home page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been send Successfully!')
    return render(request, 'contact.html')