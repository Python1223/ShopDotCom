from django.db import models
from ProfileManagement.models import SellerProfileModel

# Create your models here.
class ItemModel(models.Model):

    itemId= models.AutoField(primary_key= True)
    itemName= models.CharField(max_length= 100)
    itemPrice= models.IntegerField(min= 0)
    sellerProfileModelIns= models.ForeignKey(to= SellerProfileModel, on_delete=models.CASCADE)
    # imagePicUrl= 
    # imageCategory= 
