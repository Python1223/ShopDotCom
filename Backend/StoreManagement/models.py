from django.db import models
from ProfileManagement.models import SellerProfileModel

# Create your models here.

class Store(models.Model):
  storeId= models.AutoField(primary_key= True)
  storeName= models.CharField(default= str(), max_length= 100)
  sellerProfileIns= models.OneToOneField(to= SellerProfileModel, on_delete=models.CASCADE)
  itemIdList= models.CharField(default= str(), max_length= 500)
