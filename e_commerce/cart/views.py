
from django.db.migrations import serializer
from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from shop.models import Product

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer

# Create your views here.


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CartAPI(viewsets.ViewSet):
    
    
    def list(self,request , *args, **kwargs):
        
        user = request.user
        queryset = Cart.objects.get(user = user)
        serializer = CartSerializer(queryset)
        return Response(serializer.data)

    
    @action(detail=False, methods=['post'], url_path='add-product/(?P<pk>[^/.]+)')
    def addProduct(self, request, pk=None, *args, **kwargs):
      try:
        if pk :
          product =get_object_or_404(Product,pk=pk)
          # product =  Product.objects.get(pk=pk)
          cart = request.user.cart
          CartItem.objects.create(cart =cart , product = product  )
          return Response(status=status.HTTP_201_CREATED)
      except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='delete-item/(?P<pk>[^/.]+)')
    def deleteProduct(self, request, pk=None, *args, **kwargs):
      if pk :
        cart_item =  CartItem.objects.get(pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_200_OK)
      
    @action(detail=False, methods=['put'], url_path='update-item/(?P<pk>[^/.]+)')
    def updateItem(self,request,pk=None ,*args, **kwargs):
      try:
        obj = get_object_or_404(CartItem,pk =pk)
        serializer = CartItemSerializer(obj ,data = request.data, partial = True)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data , status=status.HTTP_200_OK)
      except:
        return Response({"error":"Bad request"},status=status.HTTP_400_BAD_REQUEST)
      
      pass 
