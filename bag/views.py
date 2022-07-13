from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import * 
from .serializers import * 
# Create your views here.

#! BAGS
# GET ALL BAGS/ CREATE BAG
class BagList(ListCreateAPIView):
  queryset = Bag.objects.all()
  serializer_class = BagSerializer

# GET BAG BY ID
class BagById(RetrieveAPIView):
  queryset = Bag.objects.all()
  serializer_class = PopulatedBagSerializer

#! ORDERS
# GET ALL ORDERS / CREATE ORDER
class OrderList(ListCreateAPIView):
  queryset = Order.objects.all()
  serializer_class = PopulatedOrderSerializer

# GET FABRIC BY ID 
class OrderById(RetrieveAPIView):
  queryset = Order.objects.all()
  serializer_class = PopulatedOrderSerializer

#! ORDER STATUS
# CREATE ORDER STATUS
class OrderStatus(ListCreateAPIView):
  queryset = OrderStatus.objects.all()
  serializer_class = OrderStatusSerializer
