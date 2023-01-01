from django.db import models
from ProfileManagement.models import BuyerProfileModel
from random import randint

class CartModel(models.Model):
    '''
    This Model Class is used to store Cart details of a particular buyer
    '''
    cartId= models.AutoField(primary_key= True)
    buyerProfileModelIns= models.OneToOneField(to= BuyerProfileModel, on_delete=models.CASCADE)
    itemIdList= models.CharField(max_length= 500, default= str())

    @staticmethod
    def getCartDisplayString(buyerProfileModelIns, cartId)-> str:
        username= buyerProfileModelIns.buyerProfileId.userIns.username
        lowerLim= 0; upperLim= 1000000
        randomNumber= randint(lowerLim, upperLim)

        cartDisplayString= "".join([username, "-", str(cartId), "-", str(randomNumber)])
        return cartDisplayString

    def __str__(self)-> str:
        cartDisplayString= CartModel.getCartDisplayString(self.buyerProfileModelIns, self.cartId)
        return cartDisplayString
        