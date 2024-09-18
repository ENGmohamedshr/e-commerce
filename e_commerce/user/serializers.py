



import email
from rest_framework import serializers
from rest_framework.authentication import authenticate

from .models import Address, User

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['city','country','postal_code','telephone']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','mobile','email','address']
        



class SignUpSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required =False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','mobile','email','password1','password2','address']
        
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({'password':"password didn't match"})
        return data
    
    def create(self, validated_data):
        if validated_data['address']:
            address = validated_data.pop('address',None)
        password  = validated_data.pop('password1')
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data , password=password)
        
        if address:
            Address.objects.create(user=user, **address)
        return user

        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password =  serializers.CharField()
    
    def validate(self , data):
        email =data.get('email')
        password =  data.get('password')

        if email and password:
            user  =  User.objects.get(email=email)
            if not user :
                raise serializers.ValidationError("can't login with data")
            
        else :
            raise serializers.ValidationError('email and password are requierd')

        data['user']  = user
        
        return data