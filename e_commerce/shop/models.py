from django.db import models

# Create your models here.


class Category(models.Model):
    name             = models.CharField(max_length=250)
    desc             = models.CharField(max_length=500)
    created_at       = models.DateTimeField(auto_now=True)
   
class Inventory(models.Model):
    quantity         = models.DecimalField(max_digits=40,decimal_places=0)

class Discount(models.Model):
    name             = models.CharField(max_length=100)
    desc             = models.CharField(max_length=250)
    precentage       = models.DecimalField(max_digits=7,decimal_places=2)
    active           = models.BooleanField(default=False)
    

class Product(models.Model):
    title            = models.CharField(max_length=250)
    desc             = models.CharField(max_length=500 , null=True)
    price            = models.DecimalField(max_digits=10 ,decimal_places=2 , default=0.00)
    image            = models.ImageField(upload_to='product_images/',null=True) 
    quantity         = models.DecimalField(max_digits=100,decimal_places=0 ,default=0)
    discount         = models.ForeignKey(Discount, on_delete=models.SET_NULL,null=True , blank=True)
    category         = models.ForeignKey(Category,related_name='products',on_delete=models.SET_NULL,null=True , blank=True)
    created_at       = models.DateTimeField(auto_now=True)

    

