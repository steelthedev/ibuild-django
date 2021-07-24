from django.urls import path,include
from . import views

app_name = "app"

urlpatterns = [
    path('',views.Home, name="home"),
    path('services',views.Services, name="services"),
    path('contact',views.Contact, name="contact"),
    
]


