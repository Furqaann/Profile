from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .utils import send_mail_to_client


def index(request):
    return render(request,'index.html')

def generic(request):
    return render(request,'Projects.html')

def elements(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail_to_client(name,email,message)
    return render(request,'Contact.html')
