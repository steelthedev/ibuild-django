from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from random import randint
from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request, 'app/index.html')


def Services(request):
    return render(request,'app/services.html')



def Contact(request):
    return render(request, 'app/contact.html')


