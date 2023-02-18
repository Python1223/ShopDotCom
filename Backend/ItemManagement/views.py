from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_304_NOT_MODIFIED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from ItemManagement.models import ItemModel
from ItemManagement.serializers import ItemSerializer

class ItemManagement(APIView):
    ''' This View Class handles HTTP requests for Item '''

    # authentication_classes= [JWTAuthentication]
    # permission_classes= [IsAuthenticated]
    #parser_classes = [MultiPartParser , FormParser]

    def get(self, request, itemId= None, format= None)-> Response:
        ''' This method returns item details when item id is provided'''

        if itemId is None: return Response(data= {}, status= HTTP_204_NO_CONTENT)

        data= {'message': str(), 'item': None}; status= HTTP_200_OK
        itemId= int(itemId)
        try: itemIns= ItemModel.objects.get(itemId= itemId)
        except: 
            data['message']= 'No item with Item Id -> {} is found'.format(itemId); status= HTTP_404_NOT_FOUND
            return Response(data= data, status= status)
            
        serializedItemIns= ItemSerializer(itemIns)
        data['message']= 'Item fetched successfully'; data['item']= serializedItemIns.data
            
        return Response(data= data, status= status)

    def post(self, request, format= None)-> Response:
        ''' This method creates a new item '''
        
        data= {'message': str(), 'item': None, 'error': None}; status= HTTP_201_CREATED
        itemAttributes= request.data.get('itemAttributes', None)
        if itemAttributes is None:
            data['message']= 'No Item Attributes were sent'; status= HTTP_204_NO_CONTENT 
            return Response(data= data, status= status)

        deserializedItemIns= ItemSerializer(data= itemAttributes)
        if deserializedItemIns.is_valid(): 
            itemIns= deserializedItemIns.save()
            data['message']= 'Item created'; data['item']= ItemSerializer(itemIns).data
        else: data['message']= 'Error while creating Item'; data['error']= deserializedItemIns.errors

        return Response(data= data, status= status)

    def patch(self, request, itemId= None, format= None)-> Response:
        '''This method patches an item'''

        data= {'message': str(), 'item': None, 'error': None}; status= HTTP_200_OK
        if itemId is None:
            data['message']= 'Please provide itemId'; status= HTTP_400_BAD_REQUEST
            return Response(data= data, status= status)

        itemId= int(itemId)
        try: itemIns= ItemModel.objects.get(itemId= itemId)
        except: 
            data['message']= 'No item with Item Id -> {} is found'.format(itemId); status= HTTP_404_NOT_FOUND
            return Response(data= data, status= status)

        newItemAttributes= request.data.get(newItemAttributes)
        deserializedItemIns= ItemSerializer(instance= itemIns, data= newItemAttributes, partial= True)

        if deserializedItemIns.is_valid(): 
            newItemIns= deserializedItemIns.save()
            data['message']= 'Item with Item Id-> {} patched successfully'.format(itemId)
            data['item']= newItemIns.data
        else:
            data['error']= deserializedItemIns.errors; status= HTTP_304_NOT_MODIFIED
        
        return Response(data= data, status= status)
