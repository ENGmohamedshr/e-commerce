
from django.dispatch import receiver

from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token

from cart.models import Cart

from .models import User

@receiver(post_save , sender = User)
def create_user_token(sender , instance , created , *args, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

@receiver(post_save,sender = User)
def create_cart_for_user(sender,instance , created ,*args, **kwargs):
    if created:
        Cart.objects.create(user = instance)