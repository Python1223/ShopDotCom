from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
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
        data= {'message': str(), 'itemName': str(), 'itemPrice': int(), 'sellerId': int()}
        statusCode= HTTP_200_OK

        itemId= request.data.get('itemId',None)
        itemIns= ItemModel.objects.get(itemId= itemId)
        itemName= itemIns.itemName
        itemPrice= itemIns.itemPrice
        sellerId= itemIns.sellerProfileModelIns.userIns.id

        data['message']= "Item fetched successfully"
        data['itemName']= itemName
        data['itemPrice']= itemPrice
        data['sellerId']= sellerId

        return Response(data= data, status= statusCode)

    def post(self, request, format= None)-> Response:

        data= {'message': str()}
        statusCode= HTTP_200_OK

        itemName= request.data.get('itemName',None)
        itemPrice= request.data.get('itemPrice',None)
        sellerProfileModelIns= request.data.get('sellerProfileModelIns',None)

        itemModelIns= ItemModel(itemName= itemName, itemPrice= itemPrice, sellerProfileModelIns= sellerProfileModelIns)
        itemModelIns.save()

        data['message']= "Item added successfully"
        return Response(data= data, status= statusCode)
