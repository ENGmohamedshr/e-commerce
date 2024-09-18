from django.db import models
from django.conf import settings

from user.models import User
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return f'Cart for {self.user.email}'
    
    
    
class CartItem(models.Model):
    cart                = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity            = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cart','product'],
                                    name='cart_product_unique' )
            ]  # Ensure unique product per cart

    def __str__(self):
        return f'{self.quantity} x {self.product.title} in cart of {self.cart.user.email}'