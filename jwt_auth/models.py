from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.
class Customuser(AbstractUser):
  address1 = models.CharField(max_length=200)
  address2 = models.CharField(max_length=200, null=True, blank=True)
  postcode = models.CharField(max_length=8)

  
