from rest_framework.serializers import ModelSerializer
from CartManagement.models import CartModel

class CartModelSerializer(ModelSerializer):
    '''
    This Serializer Class is used as a serializer for CartModel
    '''
    class Meta:
        model= CartModel
        fields= '__all__'
        