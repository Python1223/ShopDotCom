from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from ItemManagement.models import ItemModel
from ItemManagement.serializers import ItemModelSerializer

class ItemManagement(APIView):
    '''
    This View Class handles HTTP requests for Item 
    '''

    def get(self, request, format= None)-> Response:
        '''
        Function returns item details when item id is provided
        '''
        data= {'message': str(), 'itemName': str(), 'itemPrice': int()}
        statusCode= HTTP_200_OK

        itemId= request.data.get('itemId',None)
        itemIns= ItemModel.objects.get(itemId= itemId)
        itemName= itemIns.itemName
        itemPrice= itemIns.itemPrice

        data['message']= "Item fetched successfully"
        data['itemName']= itemName
        data['itemPrice']= itemPrice

        return Response(data= data, status= statusCode)

    def post(self, request, format= None)-> Response:

        data= {'message': str()}
        statusCode= HTTP_200_OK

        itemName= request.data.get('itemName',None)
        itemPrice= request.data.get('itemPrice',None)

        itemModelIns= ItemModel(itemName= itemName, itemPrice= itemPrice )
        itemModelIns.save()

        data['message']= "Item added successfully"
        return Response(data= data, status= statusCode)

    def patch(self, request, format= None)-> Response:

        data= {'message':str()}
        statusCode= HTTP_200_OK

        itemId= request.data.get('itemId',None)
        newItemName= request.data.get('itemName',None)
        newItemPrice= request.data.get('itemPrice',None)

        itemIns= ItemModel.objects.get(itemId= itemId)
        if itemIns is None:

            data['message']= "No such item found"
            statusCode= HTTP_404_NOT_FOUND
            return Response(data= data, status= statusCode)

        itemName= itemIns.itemName
        itemPrice= itemIns.itemPrice

        itemName= newItemName if newItemName is not None else itemName
        if type(newItemPrice) != int: 

            data['message']= "Please provide valid price as integer"
            statusCode= HTTP_400_BAD_REQUEST
            return Response(data= data, status= statusCode)

        else: itemPrice= newItemPrice
        
        itemModelIns= ItemModel(itemName= itemName, itemPrice= itemPrice )
        itemModelIns.save()

        data['message']= "Item changed successfully"
        return Response(data= data, status= statusCode)



