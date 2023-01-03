from rest_framework.serializers import ModelSerializer
from ItemManagement.models import ItemModel

class ItemModelSerializer(ModelSerializer):
    '''
    This Serializer Class is used as a serializer for ItemModel
    '''
    class Meta:
        model= ItemModel
        fields= '__all__'
        