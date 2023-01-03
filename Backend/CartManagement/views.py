from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from ProfileManagement.models import BuyerProfileModel
from CartManagement.models import CartModel
from CartManagement.CartOperations import CartOperationFactory
from CartManagement.serializers import CartModelSerializer

class CartManagement(APIView):
    '''
    This View Class handles HTTP requests for Cart 
    '''

    def get(self, request, format= None)-> Response:
        '''
        This method returns cart details if a user profile is of a buyer
        '''
        data= {'message': str(), 'itemIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        buyerprofileModelIns= BuyerProfileModel.objects.get(userIns= userIns)
        cartModelIns= CartModel.objects.filter(buyerprofileModelIns= buyerprofileModelIns)
        itemIdList= cartModelIns.itemIdList

        data['message']= 'Cart details fetched successfully'
        data['itemIdList']= itemIdList

        return Response(data= data, status= statusCode)
        
    def patch(self, request, operation, format= None)-> Response:
        '''
        This method handles post operations in cart of a buyer profile
        '''
        data = {'message': str(), 'itemIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        itemId= request.data.get('itemId',None)

        buyerprofileModelIns= BuyerProfileModel.objects.get(userIns= userIns)
        cartModelIns= CartModel.objects.filter(buyerprofileModelIns= buyerprofileModelIns)
        itemIdList= cartModelIns.itemIdList
        
        cartOperationIns= CartOperationFactory(operation, itemIdList, itemId)
        editItemIdList= cartOperationIns.editItemIdList()

        cartModelIns.itemIdList= editItemIdList
        cartModelIns.save()
        
        data['message']= 'Cart operation done successfully'
        return Response(data= data, status= statusCode)
        