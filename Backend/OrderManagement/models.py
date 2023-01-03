from django.db import models
from ProfileManagement.models import BuyerProfileModel
from ItemManagement.models import ItemModel
from random import randint

class OrderModel(models.Model):
    '''
    This Model Class is used to store Order details of a particular buyer
    '''
    orderId= models.AutoField(primary_key= True)
    buyerProfileModelIns= models.ForeignKey(to= BuyerProfileModel, on_delete=models.CASCADE)
    itemIns= models.ForeignKey(to= ItemModel, on_delete=models.CASCADE)
    paymentStatus= models.BooleanField(default= False)
    deliveryStatus= models.BooleanField(default= False)


class OrderListModel(models.Model):
    orderListId= models.AutoField(primary_key= True)
    buyerProfileModelIns= models.OneToOneField(to= BuyerProfileModel, on_delete=models.CASCADE)
    orderIdList= models.CharField(max_length= 500)