from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from ProfileManagement.models import BuyerProfileModel
from OrderManagement.models import OrderListModel
from OrderManagement.OrderOperations import OrderOperationFactory
from OrderManagement.serializers import OrderModelSerializer

class OrderManagement(APIView):
    '''
    This View Class handles HTTP requests for Order
    '''

    def get(self, request, format= None)-> Response:
        '''
        This method returns order list if a user profile is of a buyer
        '''
        data= {'message': str(), 'itemIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        buyerprofileModelIns= BuyerProfileModel.objects.get(userIns= userIns)
        OrderListModelIns= OrderListModel.objects.filter(buyerprofileModelIns= buyerprofileModelIns)
        orderIdList= OrderListModelIns.orderIdList

        data['message']= 'Order details fetched successfully'
        data['itemIdList']= orderIdList

        return Response(data= data, status= statusCode)
        
    def patch(self, request, operation, format= None)-> Response:
        '''
        This method handles post operations in order of a buyer profile
        '''
        data = {'message': str(), 'itemIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        itemId= request.data.get('itemId',None)

        buyerprofileModelIns= BuyerProfileModel.objects.get(userIns= userIns)
        orderListModelIns= OrderListModel.objects.filter(buyerprofileModelIns= buyerprofileModelIns)
        orderIdList= orderListModelIns.orderIdList
        
        orderOperationIns= OrderOperationFactory(operation, orderIdList, itemId)
        editItemIdList= orderOperationIns.editItemIdList()

        orderListModelIns.orderIdList= editItemIdList
        
        data['message']= 'Order operation done successfully'
        return Response(data= data, status= statusCode)
        