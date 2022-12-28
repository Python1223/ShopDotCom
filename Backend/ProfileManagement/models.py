from django.db import models
from django.contrib.auth.models import User

#  Profile model class 
class ProfileModel(models.Model):
    profileId= models.AutoField(primary_key=True)
    userIns= models.OneToOneField(User,on_delete=models.CASCADE)
    profileType= models.CharField(max_length=20)

    @staticmethod
    def isBuyer(profileModelIns)-> bool:
        return profileModelIns.profileType== 'Buyer'
    
    @staticmethod
    def isSeller(profileModelIns)-> bool:
        return profileModelIns.profileType== 'Seller'

class BuyerProfileModel(models.Model):
    buyerProfileId= models.OneToOneField(ProfileModel, on_delete=models.CASCADE, primary_key=True)
    cartId= models.IntegerField()
    purchaseListId= models.IntegerField()
    orderListId= models.IntegerField()

class SellerProfileModel(models.Model):
    sellerProfileId= models.OneToOneField(ProfileModel, on_delete=models.CASCADE, primary_key= True)
    storeName= models.CharField(max_length=50)
