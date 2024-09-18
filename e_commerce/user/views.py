import email
from django.core.serializers import serialize
from django.db.models import query
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import LoginSerializer, SignUpSerializer, UserSerializer

# Create your views here.



class UserAPI(viewsets.ViewSet):
    
    
    def list(self , request ,*args, **kwargs):
        queryset = User.objects.all()
        
        serializer = UserSerializer(queryset, many = True)
        
        return Response(serializer.data)
    
    
    def retrieve(self , request ,pk = None,*args, **kwargs ):
        if pk :
            try:
                queryset = User.objects.get(pk=pk)
                serializer = UserSerializer(queryset)
                return Response(serializer.data)
            except:
                return Response(status=status.HTTP_204_NO_CONTENT)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    @action(detail=False , methods=['post'] , url_path='sign-up')
    def signup(self, request,*args, **kwargs):
        serializer = SignUpSerializer(data =  request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
    
    
    @action(detail=False, methods=['post'],url_path='login')
    def login(self , request , *args, **kwargs):
        serializer = LoginSerializer(data= request.data , context= {'request':request})
        
        if serializer.is_valid(raise_exception=True):
            user =  serializer.validated_data['user']
            token , created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        
        
    @action(detail=False , methods=['get'])    
    def logout(self, requset,*args, **kwargs):
        pass