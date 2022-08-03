from django.db import models
from products.models import Product
from jwt_auth.models import Customuser
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Order(models.Model):
  customer_id = models.ForeignKey(Customuser, related_name='order', on_delete=models.CASCADE)
  created_date = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return f'{self.customer_id} - {self.created_date}'

class Bag(models.Model):
  customer_id = models.ForeignKey(Customuser, related_name='bag', on_delete=models.CASCADE)
  order_id = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  front = models.ForeignKey(Product, related_name='front', on_delete=models.SET_NULL, null=True)
  top = models.ForeignKey(Product, related_name='top', on_delete=models.SET_NULL, null=True)
  bottom = models.ForeignKey(Product, related_name='bottom', on_delete=models.SET_NULL, null=True)
  strap = models.ForeignKey(Product, related_name='strap', on_delete=models.SET_NULL, null=True)
  side_strap = models.ForeignKey(Product, related_name='side_strap', on_delete=models.SET_NULL, null=True)
  lining = models.ForeignKey(Product, related_name='lining', on_delete=models.SET_NULL, null=True)
  zip = models.ForeignKey(Product, related_name='zip', on_delete=models.SET_NULL, null=True)
  heart = models.ForeignKey(Product, related_name='heart', on_delete=models.SET_NULL, null=True)
  pocket = models.ForeignKey(Product, related_name='pocket', on_delete=models.SET_NULL, null=True)
  clasp = models.ForeignKey(Product, related_name='clasp', on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=50, null=True, blank=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return f'{self.customer_id} - {self.name}'

class OrderStatus(models.Model):
  PENDING = 'pending'
  CONFIRMED = 'confirmed'
  MAKING = 'making'
  CREATED = 'created'
  DISPATCHED = 'dispatched'
  DELIVERED = 'delivered'
  
  STATUS = [
    (PENDING, 'pending'),
    (CONFIRMED, 'confirmed'),
    (MAKING, 'making'),
    (CREATED, 'created'),
    (DISPATCHED, 'dispatched'),
    (DELIVERED, 'delivered'),
  ]
  order_id = models.ForeignKey(Order, related_name='order_status', on_delete=models.CASCADE)
  status = models.CharField(max_length=100, choices=STATUS, default=PENDING)
  created_date = models.DateTimeField(auto_now_add = True)
  def __str__(self):
      return f'{self.order_id} - {self.status}'


