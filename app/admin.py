from django.contrib import admin
from .models import Order, OrderItem, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)