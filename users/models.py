#   User class imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

#   UserManager imports
from django.contrib.auth.base_user import BaseUserManager

#   Common Imports
from django.utils.translation import gettext_lazy as _ 


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError('Must have Email')
        
        email   = self.normalize_email(email)   #   lowercase email
        user    = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(max_length=255, unique=True)

    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email