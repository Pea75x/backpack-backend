from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import * 
from .serializers.common import * 
# Create your views here.

#! Products
# GET ALL PRODUCTS/ CREATE PRODUCT
class ProductList(ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

# GET PRODUCT BY ID
class ProductById(RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer