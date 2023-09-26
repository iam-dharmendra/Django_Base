from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .manager import MyManager
# Create your models here.


class User(AbstractUser,PermissionsMixin):

    username=None
    email=models.EmailField(max_length=50,null=True,blank=True,unique=True)
    phone_number=models.CharField(max_length=50,null=True,blank=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=MyManager()
