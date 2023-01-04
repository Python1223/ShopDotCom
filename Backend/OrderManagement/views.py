from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from ProfileManagement.models import BuyerProfileModel
from ItemManagement.models import ItemModel
from OrderManagement.models import OrderModel, OrderListModel
from OrderManagement.OrderOperations import OrderOperationFactory
from OrderManagement.serializers import OrderModelSerializer

class OrderManagement(APIView):
    '''
    This View Class handles Http request for Order
    '''

    def get(self, request, format= None)-> Response:
        '''
        This method returns order details of a order given an orderId
        '''
        data= {'message': str(), 'order': dict()}
        statusCode= HTTP_200_OK

        orderId= request.data.get('orderId', None)
        orderModelIns= OrderModel.objects.get(orderId= orderId)

        orderDictIns= OrderModelSerializer(orderModelIns).data
        data['message']= 'Order details fetched successfully'
        data['order']= orderDictIns
        return Response(data= data, status= statusCode)

    def post(self, request, format= None)-> Response:
        '''
        This method creates an order given an itemId
        '''
        data= {'message': str(), 'orderId': int()}
        statusCode= HTTP_200_OK

        userIns= request.user
        buyerProfileModelIns= BuyerProfileModel.objects.get(user= userIns)

        itemId= request.data.get('itemId', None)    
        itemIns= ItemModel.objects.get(itemId= itemId)

        orderModelIns= OrderModel(buyerProfileModelIns= buyerProfileModelIns, itemIns= itemIns)
        orderModelIns.save()

        data['message']= 'Order placed successfully'
        orderId= orderModelIns.orderId
        data['orderId']= orderId

        orderListModelIns= OrderListModel.objects.filter(buyerprofileModelIns= buyerProfileModelIns)
        orderIdList= orderListModelIns.orderIdList
        
        operation= 'AddItem'
        orderOperationIns= OrderOperationFactory(operation, orderIdList, orderId)
        editItemIdList= orderOperationIns.editItemIdList()

        orderListModelIns.orderIdList= editItemIdList
        orderListModelIns.save()
        
        return Response(data= data, status= statusCode)


class OrderListManagement(APIView):
    '''
    This View Class handles HTTP requests for OrderList
    '''

    def get(self, request, format= None)-> Response:
        '''
        This method returns order list if a user profile is of a buyer
        '''
        data= {'message': str(), 'orderIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        buyerprofileModelIns= BuyerProfileModel.objects.get(userIns= userIns)
        OrderListModelIns= OrderListModel.objects.filter(buyerprofileModelIns= buyerprofileModelIns)
        orderIdList= OrderListModelIns.orderIdList

        data['message']= 'Order details fetched successfully'
        data['orderIdList']= orderIdList

        return Response(data= data, status= statusCode)
        
    def patch(self, request, operation, format= None)-> Response:
        '''
        This method handles patch operations in order of a buyer profile
        '''
        data = {'message': str(), 'orderIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        orderId= request.data.get('orderId',None)

        buyerProfileModelIns= BuyerProfileModel.objects.get(userIns= userIns)
        orderListModelIns= OrderListModel.objects.filter(buyerprofileModelIns= buyerProfileModelIns)
        orderIdList= orderListModelIns.orderIdList
        
        orderOperationIns= OrderOperationFactory(operation, orderIdList, orderId)
        editItemIdList= orderOperationIns.editItemIdList()

        orderListModelIns.orderIdList= editItemIdList
        orderListModelIns.save()
        
        data['message']= 'Order operation done successfully'
        return Response(data= data, status= statusCode)
        