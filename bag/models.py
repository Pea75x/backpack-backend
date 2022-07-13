from django.db import models
from products.models import Product
from jwt_auth.models import Customuser
# Create your models here.
class Bag(models.Model):
  customer_id = models.ForeignKey(Customuser, related_name='bag', on_delete=models.CASCADE)
  front_id = models.ForeignKey(Product, related_name='front', on_delete=models.SET_NULL, null=True)
  back_id = models.ForeignKey(Product, related_name='back', on_delete=models.SET_NULL, null=True)
  top_id = models.ForeignKey(Product, related_name='top', on_delete=models.SET_NULL, null=True)
  bottom_id = models.ForeignKey(Product, related_name='bottom', on_delete=models.SET_NULL, null=True)
  strap_id = models.ForeignKey(Product, related_name='strap', on_delete=models.SET_NULL, null=True)
  side_strap_id = models.ForeignKey(Product, related_name='side_strap', on_delete=models.SET_NULL, null=True)
  lining_id = models.ForeignKey(Product, related_name='lining', on_delete=models.SET_NULL, null=True)
  zip_id = models.ForeignKey(Product, related_name='zip', on_delete=models.SET_NULL, null=True)
  heart_id = models.ForeignKey(Product, related_name='heart', on_delete=models.SET_NULL, null=True)
  pocket_id = models.ForeignKey(Product, related_name='pocket', on_delete=models.SET_NULL, null=True)
  clasp_id = models.ForeignKey(Product, related_name='clasp', on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
    return f'{self.customer_id} - {self.name}'

class Order(models.Model):
  bag_id = models.ForeignKey(Bag, related_name='order_number', on_delete=models.CASCADE)
  customer_id = models.ForeignKey(Customuser, related_name='order', on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=6, decimal_places=2)
   
  def __str__(self):
    return f'{self.customer_id} - {self.bag_id}'

class OrderStatus(models.Model):
  PENDING = 'Pending...'
  CONFIRMED = 'Order Confirmed'
  MAKING = 'Lovingly Being Made...'
  CREATED = 'A Masterpiece is born!'
  DISPATCHED = 'On its way to its new home!'
  DELIVERED = 'Successfully Delivered!'
  
  STATUS = [
    (PENDING, 'Pending...'),
    (CONFIRMED, 'Order Confirmed'),
    (MAKING, 'Lovingly Being Made...'),
    (CREATED, 'A Masterpiece is born!'),
    (DISPATCHED, 'On its way to its new home!'),
    (DELIVERED, 'Successfully Delivered!'),
  ]
  order_id = models.ForeignKey(Order, related_name='order_status', on_delete=models.CASCADE)
  status = models.CharField(max_length=100, choices=STATUS, default=PENDING)
  created_date = models.DateTimeField(auto_now_add = True)
  def __str__(self):
      return f'{self.order_id} - {self.status}'


