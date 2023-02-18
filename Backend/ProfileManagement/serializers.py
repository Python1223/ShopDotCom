from rest_framework.serializers import ModelSerializer
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel

class BuyerSerializer(ModelSerializer):
  ''' Serializer Class for BuyerProfileModel '''
  class Meta: 
    model= BuyerProfileModel; fields= '__all__'

class SellerSerializer(ModelSerializer):
  ''' Serializer Class for SellerProfileModel'''
  class Meta:
    model= SellerProfileModel; fields= '__all__'
    