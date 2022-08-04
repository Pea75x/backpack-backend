from rest_framework import serializers
from .models import *
from products.serializers.common import ProductSerializer

class BagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bag
    fields = ("__all__")

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ("__all__")

class OrderStatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderStatus
    fields = ("__all__")

class PopulatedBagSerializer(BagSerializer):
  order = OrderSerializer()
  front = ProductSerializer()
  top = ProductSerializer()
  bottom = ProductSerializer()
  strap = ProductSerializer()
  side_strap = ProductSerializer()
  lining = ProductSerializer()
  zip = ProductSerializer()
  heart = ProductSerializer()
  pocket = ProductSerializer()
  clasps = ProductSerializer()

class PopulatedForOrderBagSerializer(BagSerializer):
  front = ProductSerializer()
  top = ProductSerializer()
  bottom = ProductSerializer()
  strap = ProductSerializer()
  side_strap = ProductSerializer()
  lining = ProductSerializer()
  zip = ProductSerializer()
  heart = ProductSerializer()
  pocket = ProductSerializer()
  clasps = ProductSerializer()
  
class PopulatedOrderSerializer(OrderSerializer):
  order_status = OrderStatusSerializer(many=True)
  items = PopulatedForOrderBagSerializer(many=True)