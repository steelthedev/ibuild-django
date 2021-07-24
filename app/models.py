from django.db import models
from accounts.models import *


class Product(models.Model):
  name=models.CharField(max_length=200,null=True)
  slug=models.SlugField()
  price=models.FloatField()
  description=models.TextField(null=True)
  def __str__(self):
    return self.name

class OrderItem(models.Model):
    customer=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1,null=True,blank=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    @property
    def get_item_price(self):
      total =self.product.price * self.quantity
      return total



class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
  customer=models.ForeignKey(Profile,on_delete=models.SET_NULL,blank=True,null=True)
  products=models.ManyToManyField(OrderItem)
  date_order=models.DateTimeField(auto_now_add=True)
  amount=models.CharField(null=True,max_length=200)
  complete=models.BooleanField(default=False,null=True,blank=True)
  transaction_id=models.CharField(max_length=100)
  def __str__(self):
    return f'{self.customer}'
  @property
  def get_cart_total(self):
    orderitem=self.products.all()
    total=sum([item.get_item_price for item in orderitem])
    return total
    
