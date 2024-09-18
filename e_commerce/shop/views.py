

from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.


class CategoryAPI(viewsets.ViewSet):
    
    
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset , many = True)
        return Response(serializer.data)
    
    def retrieve(self , request , pk = None):
        if pk:
            queryset = Product.objects.filter(category= pk)
            serializer = ProductSerializer(queryset , many=True)
            return Response(serializer.data)
        else :
            return Response("no category with this id")
    
    


class ProductAPI(viewsets.ViewSet):
    
    
    # def get_permissions(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         permission_classes = [AllowAny]
    #     else: 
    #         permission_classes = [IsAuthenticated,IsAdminUser]
            
    #     return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        try:
            
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            return Response({'error':'Bad request'},status=status.HTTP_400_BAD_REQUEST )

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = get_object_or_404(Product, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(queryset, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
