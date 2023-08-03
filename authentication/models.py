from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.db import models
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(('You must provide an email address'))
        # convert all in lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_user', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, user_name, first_name, password, **other_fields)

# 2. Creating Custom User Model
class Newuser(AbstractBaseUser, PermissionsMixin):
    phone = models.BigIntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=150, )
    first_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    email= models.EmailField(unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    # required for superuser
    REQUIRED_FIELDS = ['user_name','first_name']

    def __str__(self):
        return self.user_name
