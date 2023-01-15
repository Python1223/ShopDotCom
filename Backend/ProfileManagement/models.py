from django.db import models
from django.contrib.auth.models import User

class BuyerProfileModel(models.Model):
    '''
    Model Class for Buyers
    '''
    userIns= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profileType= models.CharField(max_length= 10, default= 'Buyer')

class SellerProfileModel(models.Model):
    '''
    Model Class for Sellers
    '''
    userIns= models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    storeId= models.IntegerField(default= -1)
    storeName= models.CharField(max_length=50)
    profileType= models.CharField(max_length= 10, default= 'Seller')
    