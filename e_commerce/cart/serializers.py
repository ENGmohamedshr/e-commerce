


from rest_framework import serializers

from shop.serializers import ProductSerializer

from .models import Cart, CartItem



class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id','quantity','cart','product']
        
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many = True)
    class Meta:
        model = Cart
        
        fields =['id','user', 'items']