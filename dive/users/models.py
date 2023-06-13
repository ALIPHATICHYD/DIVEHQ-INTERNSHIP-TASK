from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from .enums import Role

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self,fullname, email,  password=None):
        if not email:
            raise ValueError('Please enter a valid email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            fullname=fullname
        )
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, fullname, password=None):
        user= self.create_user(
            email, 
            fullname,
            password=password
        )
        user.is_staff = True
        user.is_admin=True
        user.is_superuser = False



class UserAccount(AbstractUser, PermissionsMixin):

    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(choices=Role.choices, max_length=50)
    manager = models.ForeignKey('self', related_name='users')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email
