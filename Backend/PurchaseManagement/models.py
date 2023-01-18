from django.db import models
from ProfileManagement.models import BuyerProfileModel

class PurchaseModel(models.Model): pass

class PurchaseListModel(models.Model):
  '''
  Model for all purchases done by a Buyer Profile
  '''
  purchaseListId= models.AutoField(primary_key= True)
  buyerProfileIns= models.OneToOneField(to= BuyerProfileModel, on_delete= models.CASCADE)
  purchaseIdList= models.CharField(default= str(), max_length= 500)
