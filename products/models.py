from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Fabric(models.Model):
  name = models.CharField(max_length=50)
  image = models.CharField(max_length=300)

  def __str__(self):
      return self.name

class Product(models.Model):
  BLANK = 'Blank'
  FRONT = 'Front'
  BACK = 'Back'
  TOP = 'Top'
  BOTTOM = 'Bottom'
  STRAP = 'Strap'
  LINING = 'Lining'
  ZIP = 'Zip'
  HEART = 'Heart'
  POCKET = 'Pocket'
  CLASPS = 'Clasps'
  
  PART_CHOICES = [
    (BLANK, 'Blank'),
    (FRONT, 'Front'),
    (BACK, 'Back'),
    (TOP, 'Top'),
    (BOTTOM, 'Bottom'),
    (STRAP, 'Strap'),
    (LINING, 'Lining'),
    (ZIP, 'Zip'),
    (HEART, 'Heart'),
    (POCKET, 'Pocket'),
    (CLASPS, 'Clasps')
  ]
  name = models.CharField(max_length=100)
  fabric = models.ForeignKey(Fabric, related_name='products', on_delete=models.CASCADE)
  part = models.CharField(max_length=20, choices=PART_CHOICES, default=BLANK)
  image = models.CharField(max_length=200, null=True)
  quantity = models.IntegerField(validators=[MinValueValidator(0)])

  def __str__(self):
      return self.name