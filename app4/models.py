from django.db import models


# # Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)     # default=false 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"

#------------------------------------------------------------------------
 
# from pyexpat import model
# from django.db import models

from django.contrib.auth.models import User, Group

# class ExtendedUser(models.Model):
#     mob = models.CharField(max_length=100)
#     adr = models.IntegerField()
#     age = models.FloatField()
#     user = models.OneToOneField(User)

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "book"

# ------------------------------------------------------------------------------------------
# 1 

from pyexpat import model
from django.db import models


# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     Price = models.IntegerField()
#     qty = models.FloatField()
#     is_published = models.BooleanField(default=True)     

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "book"


# #-------------------------------------------------------------------

# # 2 how to extend user model in django


