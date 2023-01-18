from django.db import models
from ProfileManagement.models import SellerProfileModel
from django.core.validators import MinValueValidator

# Create your models here.
class ItemModel(models.Model):
    
    itemId= models.AutoField(primary_key= True)
    itemName= models.CharField(max_length= 100)
    itemPrice= models.PositiveIntegerField(default= 0, validators=[MinValueValidator(0)])
    # imagePicUrl= 
    # imageCategory= 
