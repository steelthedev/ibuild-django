from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from random import randint
from django.contrib import messages
from django.core.mail import send_mail
from ibuild import settings
from django.template.loader import render_to_string

# Create your views here.

def Home(request):
    return render(request, 'app/index.html')


def Services(request):
    return render(request,'app/services.html')



def Contact(request):
    if request.method == "POST":
        
        full_name = request.POST["full_name"]
        from_email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        message_full =  message
        to_email= "omoakinwumi@outlook.com"
        template = render_to_string('app/email_template.html',{'name':full_name, 'email':from_email , 'message':message_full })
        send_mail(subject, template , settings.EMAIL_HOST_USER ,[to_email] ,  fail_silently=False,)


        messages.info(request,"Email sent")
        return redirect("app:contact")


    return render(request, 'app/contact.html')


