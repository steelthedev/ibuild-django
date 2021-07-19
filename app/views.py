from django.shortcuts import render, redirect

# Create your views here.

def Home(request):
    return render(request, 'app/index.html')


def Services(request):
    return render(request,'app/services.html')



def Contact(request):
    return render(request, 'app/contact.html')