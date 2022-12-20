from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#  Profile model class 
class ProfileModel(models.Model):
    profileId= models.AutoField(primary_key=True)
    userIns= models.OneToOneField(User,on_delete=models.CASCADE)
    profileType= models.CharField(max_length=20)


# class BuyerProfileModel(models.Model):
    

# class SellerProfileModel():
