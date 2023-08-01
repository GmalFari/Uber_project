from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
# class Newuser(AbstractBaseUser):
#     is_user = models.BooleanField(default=True,null=True, blank=True)
#     is_driver = models.BooleanField(default=False ,null=True, blank=True)
#     first_name =  models.CharField(max_length=100, null=True, blank=True, unique=True)
   
#     phone = models.BigIntegerField(null=True, blank=True)

#     REQUIRED_FIELDS = ['username']
#     USERNAME_FIELD = 'first_name'

    # def __str__(self):
    #     return str(self.phone)