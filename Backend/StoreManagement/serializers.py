from rest_framework.serializers import ModelSerializer
from StoreManagement.models import Store

class StoreSerializer(ModelSerializer):
    '''
    This Serializer Class is used as a serializer for OrderModel
    '''
    class Meta:
        model= Store
        fields= '__all__'
        