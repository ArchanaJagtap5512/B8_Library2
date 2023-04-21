# from statistics import mode
# from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)
    # mobile = models.IntegerField(default=123)
#     adress = models.CharField(max_length=255, default="pune")

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_("email address"), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     mobile = models.IntegerField(default=123)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email



# # custom user in django 

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)