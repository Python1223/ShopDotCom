from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from ProfileManagement.models import SellerProfileModel
from StoreManagement.models import Store
from StoreManagement.serializers import StoreSerializer
from ItemManagement.models import ItemModel
from StoreManagement.StoreOperations import StoreOperationFactory

class StoreManagement(APIView):
  '''View for Store Management'''

  def get(self, request, format= None)-> Response:
    '''Returns Store Instance for a given user (Seller)'''
    data= {'message': str(), 'storeDetails': None}; statusCode= HTTP_200_OK
    
    userIns= request.user
    sellerProfileIns= SellerProfileModel.objects.get(userIns= userIns)

    if sellerProfileIns is None:
      data['message']= 'This is not a Seller Profile'
      statusCode= HTTP_400_BAD_REQUEST

    else:
      storeIns= Store.objects.filter(sellerProfileIns= sellerProfileIns)
      storeDetails= StoreSerializer(storeIns).data
      data['message']= 'Store Details fetched successfully'
      data['storeDetails']= storeDetails

    return Response(data= data, status= statusCode)

  def patch(self, request, operation, format= None)-> Response:

    data= {'message':str()}; statusCode= HTTP_200_OK
    storeId= request.data.get('storeId, None'); itemId= request.data.get('itemId',None)
    itemIns= ItemModel.data.get(itemId= itemId)
    
    storeIns= Store.objects.get(storeId= storeId)
    itemIdList= storeIns.itemIdList

    storeOperationIns= StoreOperationFactory(operation, itemIdList, itemIns)
    editItemIdList= storeOperationIns.editItemIdList()

    storeIns.itemIdList= editItemIdList
    storeIns.save()

    data['message']= 'Store operation done successfully'
    return Response(data= data, status= statusCode)
    