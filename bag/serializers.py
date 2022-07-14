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
  order_number = OrderSerializer()
  front_id = ProductSerializer()
  back_id = ProductSerializer()
  top_id = ProductSerializer()
  bottom_id = ProductSerializer()
  strap_id = ProductSerializer()
  side_strap_id = ProductSerializer()
  lining_id = ProductSerializer()
  zip_id = ProductSerializer()
  heart_id = ProductSerializer()
  pocket_id = ProductSerializer()
  clasp_id = ProductSerializer()
  
class PopulatedOrderSerializer(OrderSerializer):
  bag_id = BagSerializer(many=True)
  order_status = OrderStatusSerializer(many=True)