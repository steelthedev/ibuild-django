from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import requests
from app.models import *
from django.shortcuts import get_object_or_404 
from random import randint
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from pypaystack import Transaction, Customer, Plan
from django.contrib import messages
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
@login_required(login_url="accounts:login")
def Dashboard(request):
    if request.user.is_authenticated:
        product = Product.objects.all()

        context = {
            'products':product
        }

        return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url="accounts:login")
def DashboardView(request, slug):
    if request.user.is_authenticated:
        
        product = Product.objects.get(slug=slug)

        context = {

            'product':product
        }

        return render(request, 'dashboard/package_desc.html', context)




@login_required(login_url="accounts:login")
def add_to_cart(request,slug):
    if request.user.is_authenticated:
        user = request.user
        customer = request.user.profile
        product = get_object_or_404(Product, slug=slug)
        order_item , created = OrderItem.objects.get_or_create(customer = customer , product = product , complete = False)

        order_qs=Order.objects.filter(customer=customer,user=user,complete=False)

        if order_qs.exists():
            order=order_qs[0]
            if order.products.filter(product__slug=product.slug).exists():
                order_item.quantity += 1
                order_item.save()
                messages.info(request,"Quantity  successfully updated")
                return redirect('dashboard:dashboard')
            else:
            
                order.products.add(order_item)
                messages.info(request,"item successfully added to cart")
                return redirect('dashboard:desc', slug=slug)
        else:
            rand_short = randint(0,1000)
            rand_long = randint(0,30000)
            ref = f"ref-{rand_short}-{rand_long}"
            order=Order.objects.create(customer=customer,user=user,ref=ref,complete=False)
            order.products.add(order_item)
            messages.info(request,"Cart successfully created and item added")
            return redirect('dashboard:dashboard')
    else:
        messages.info(request,"You must be logged in")
        return redirect('app:home')



@login_required(login_url="accounts:login")
def cart_view(request:HttpRequest) -> HttpResponse:
  user=request.user
  customer=request.user.profile
  try:

        order=Order.objects.get(customer=customer,user=user,complete=False)
        email = customer.email
        first_name = customer.first_name
        last_name = customer.last_name
        paystack_secret = "sk_test_b1630e59eb70f2592023210935c7894455b9ac1b"
        paystack_public = "pk_test_ef1bea703713ac519754d7b88f3b56ea141c1d67"
        

        context = {
            'order':order,
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'paystack_secret':paystack_secret,
            'paystack_public':paystack_public,
            

        }


    
        return render(request,'dashboard/cart.html', context)
  except ObjectDoesNotExist:


        messages.error(request,"No active Order")
        return redirect('/')



def verify_payment(request:HttpRequest, ref) -> HttpResponse:
    order = get_object_or_404(Order, ref=ref)
    verified = order.verify_payment()
    if verified:
        messages.success(request," Alright mate ya done")
    else:
        messages.error(request,"verification failed ")
    return redirect('dashboard:dashboard')

    