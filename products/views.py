from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import * 
from .serializers.common import * 
# Create your views here.

#! PRODUCTS
# GET ALL PRODUCTS/ CREATE PRODUCT
class ProductList(ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

# GET PRODUCT BY ID
class ProductById(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = PopulatedProductSerializer

# GET PRODUCT BY PART
class GetProductByPart(ListCreateAPIView):
    serializer_class = PopulatedProductSerializer
    
    def get_queryset(self):
      queryset = Product.objects.all()
      partName = self.request.query_params.get('part')

      if partName:
        productData = queryset.filter(part= partName)
        return productData

# GET PRODUCT BY FABRIC
class GetProductByFabric(ListCreateAPIView):
    serializer_class = PopulatedProductSerializer
    
    def get_queryset(self):
      queryset = Product.objects.all()
      fabricName = int(self.request.query_params.get('fabric'))

      if fabricName:
        print(fabricName)
        productData = queryset.filter(fabric=fabricName)
        return productData

# UPDATE PRODUCT
class ProductlUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

#! FABRICS
# GET ALL FABRICS / CREATE FABRIC
class FabricList(ListCreateAPIView):
  queryset = Fabric.objects.all()
  serializer_class = FabricSerializer

# GET FABRIC BY ID 
class FabricById(RetrieveAPIView):
  queryset = Fabric.objects.all()
  serializer_class = FabricSerializer