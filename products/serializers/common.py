from rest_framework import serializers
from ..models import *

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ("__all__")

class FabricSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fabric
    fields = ("__all__")

class PopulatedProductSerializer(ProductSerializer):
  fabric = FabricSerializer()