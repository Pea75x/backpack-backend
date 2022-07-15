"""mybackpackapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bag.views import BagById, BagList
from products.views import *
from jwt_auth.views import *
from bag.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # FABRIC 
    path('fabrics/', FabricList.as_view()),
    path('fabric/<int:pk>', FabricById.as_view()),
    # PRODUCTS   
    path('products/', ProductList.as_view()),
    path('product/<int:pk>/', ProductById.as_view()),
    path('productsearch/', GetProductByPart.as_view()),
    path('productupdate/<int:pk>/', ProductlUpdateDestroy.as_view()),
    # USERS
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    # BAGS
    path('bags/', BagList.as_view()),
    path('bag/<int:pk>', BagById.as_view()),
    path('createbag/', CreateBag.as_view()),
    # ORDERS
    path('orders/', OrderList.as_view()),
    path('order/<int:pk>', OrderById.as_view()),
    path('createorder/', CreateOrder.as_view()), 
    path('userorders/', GetUserOrders.as_view()), 
    # ORDER STATUS
    path('orderstatus/', OrderStatus.as_view()),
    
]
