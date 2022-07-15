from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import * 
from .serializers import * 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#! BAGS
#CREATE BAG
class CreateBag(APIView):
  permission_classes = [IsAuthenticated,]

  def post(self, request):
    request.data['customer_id'] = request.user.id
    bag_serializer = BagSerializer(data= request.data)
    if bag_serializer.is_valid():
      bag_serializer.save()
      return Response(data = bag_serializer.data, status = status.HTTP_201_CREATED)
    return Response(data = bag_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# GET ALL BAGS
class BagList(ListCreateAPIView):
    queryset = Bag.objects.all()
    serializer_class = BagSerializer

# GET BAG BY ID
class BagById(RetrieveAPIView):
  queryset = Bag.objects.all()
  serializer_class = PopulatedBagSerializer

#! ORDERS
# CREATE ORDER
class CreateOrder(APIView):
  permission_classes = [IsAuthenticated,]

  def post(self, request):
    request.data['customer_id'] = request.user.id
    order_serializer = OrderSerializer(data= request.data)
    if order_serializer.is_valid():
      order_serializer.save()
      return Response(data = order_serializer.data, status= status.HTTP_201_CREATED)
    return Response (data= order_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# GET ALL ORDERS
class OrderList(ListCreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer
 
# GET FABRIC BY ID 
class OrderById(RetrieveAPIView):
  queryset = Order.objects.all()
  serializer_class = PopulatedOrderSerializer

#! ORDER STATUS
# CREATE ORDER STATUS
class OrderStatus(ListCreateAPIView):
  queryset = OrderStatus.objects.all()
  serializer_class = OrderStatusSerializer
