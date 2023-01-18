from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
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
        buyerProfileIns= BuyerProfileModel.objects.get(user= userIns)

        itemId= request.data.get('itemId', None)    
        itemIns= ItemModel.objects.get(itemId= itemId)

        orderModelIns= OrderModel(buyerProfileIns= buyerProfileIns, itemIns= itemIns)
        orderModelIns.save()

        data['message']= 'Order placed successfully'
        orderId= orderModelIns.orderId
        data['orderId']= orderId

        orderListIns= OrderListModel.objects.filter(buyerprofileIns= buyerProfileIns)
        orderIdList= orderListIns.orderIdList
        
        operation= 'AddItem'
        orderOperationIns= OrderOperationFactory(operation, orderIdList, orderId)
        editItemIdList= orderOperationIns.editItemIdList()

        orderListIns.orderIdList= editItemIdList
        orderListIns.save()
        
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
        buyerprofileIns= BuyerProfileModel.objects.get(userIns= userIns)
        OrderListIns= OrderListModel.objects.filter(buyerprofileIns= buyerprofileIns)
        orderIdList= OrderListIns.orderIdList

        data['message']= 'Order details fetched successfully'; data['orderIdList']= orderIdList
        return Response(data= data, status= statusCode)
        
    def post(self, request, format= None)-> Response:
        '''
        Creates Order list for a Buyer Profile
        '''
        data= {'message': str(), 'orderListId': None}; statusCode= HTTP_201_CREATED

        userIns= request.user; buyerProfileIns= BuyerProfileModel.objects.get(user= userIns)
        if buyerProfileIns is None:
            data['message']= 'This is not a Buyer Profile'; statusCode= HTTP_404_NOT_FOUND
        else:
            orderListIns= OrderListModel(buyerProfileIns= buyerProfileIns); orderListId= orderListIns.orderListId
            data['message']= 'Order List created successfully'; data['orderListId']= orderListId
            statusCode= HTTP_201_CREATED

        return Response(data= data, status= statusCode)

    def patch(self, request, operation, format= None)-> Response:
        '''
        This method handles patch operations in order of a buyer profile
        '''
        data = {'message': str(), 'orderIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        orderId= request.data.get('orderId',None)

        buyerProfileIns= BuyerProfileModel.objects.get(userIns= userIns)
        orderListIns= OrderListModel.objects.filter(buyerprofileIns= buyerProfileIns)
        orderIdList= orderListIns.orderIdList
        
        orderOperationIns= OrderOperationFactory(operation, orderIdList, orderId)
        editItemIdList= orderOperationIns.editItemIdList()

        orderListIns.orderIdList= editItemIdList
        orderListIns.save()
        
        data['message']= 'Order operation done successfully'
        return Response(data= data, status= statusCode)
        