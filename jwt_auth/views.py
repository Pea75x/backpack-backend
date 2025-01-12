from django.shortcuts import render

# Create your views here.
from time import strftime
#from genericpath import exists
# from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import *

# Create your views here.

User = get_user_model()

class RegisterView(APIView):
  def post(self,request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Registration successful'})
    return Response(serializer.errors, status=422)



class LoginView(APIView):
  def post(self, request):
    email = request.data.get('email')
    password = request.data.get('password')

    try: 
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      raise PermissionDenied({'message': 'Invalid credentials'})
    
    if not user.check_password(password):
      raise PermissionDenied({'message' : 'Invalid credentials'})
    
    dt = datetime.now() + timedelta(days=7)
    token = jwt.encode(
      {
        'sub': user.id,
        'exp': int(dt.strftime('%s')),
        'admin': user.is_staff
      },
      settings.SECRET_KEY,
      algorithm='HS256'
    )
    return Response({'token': token, 'message': f'Welcome back {user.username}!'})

