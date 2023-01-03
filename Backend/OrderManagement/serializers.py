from rest_framework.serializers import ModelSerializer
from OrderManagement.models import OrderModel

class OrderModelSerializer(ModelSerializer):
    '''
    This Serializer Class is used as a serializer for OrderModel
    '''
    class Meta:
        model= OrderModel
        fields= '__all__'
        