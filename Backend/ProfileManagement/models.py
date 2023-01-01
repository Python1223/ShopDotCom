from django.db import models
from django.contrib.auth.models import User

class BuyerProfileModel(models.Model):
    '''
    Model Class for Buyers
    '''
    userModelIns= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cartId= models.IntegerField(default= -1)
    purchaseListId= models.IntegerField(default= -1)
    orderListId= models.IntegerField(default= -1)
    profileType= models.CharField(max_length= 10)

class SellerProfileModel(models.Model):
    '''
    Model Class for Sellers
    '''
    userModelIns= models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    storeId= models.IntegerField(default= -1)
    storeName= models.CharField(max_length=50)
    profileType= models.CharField(max_length= 10)