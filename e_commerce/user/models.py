


from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self , email , password = None , **extra_fields):
        if not email :
            raise ValueError('the email field is required')
        email = self.normalize_email(email)
        user  = self.model(email =email ,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self , email  , password = None , **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            return ValueError('superUser Must be is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            return ValueError('superUser Must be is_superuser = True')
        
        return self.create_user(email,password,**extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)
        

class User(AbstractBaseUser,PermissionsMixin):
    first_name          = models.CharField(max_length=100)
    last_name           = models.CharField(max_length=100)
    username            = models.CharField(max_length=100)
    mobile              = models.CharField(max_length=50)
    email               = models.EmailField(unique=True) 
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    
class Address(models.Model):
    user_id             = models.ForeignKey(User , related_name="address",on_delete=models.CASCADE)
    city                = models.CharField(max_length=100)
    country             = models.CharField(max_length=100)
    postal_code         = models.CharField(max_length=50)
    telephone           = models.CharField(max_length=50)