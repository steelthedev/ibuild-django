
from django.urls import path,include
from . import views 

app_name = 'dashboard'

urlpatterns = [
   
   path('',views.Dashboard, name="dashboard"),
   path('cart/description/<slug:slug>', views.DashboardView, name="desc"),
   path('cart/add_to_cart/<slug:slug>',views.add_to_cart, name="add_to_cart"),
   path('cart', views.cart_view, name="cart_view"),
   path('cart/verify_payment/<str:ref>', views.verify_payment, name="verify_payment"),
   path('order-history', views.OrderHsitory, name="order_history"),
    
]


