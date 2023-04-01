from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_302_FOUND, HTTP_404_NOT_FOUND
from ProfileManagement.models import BuyerProfileModel
from CartManagement.models import CartModel
from CartManagement.CartOperations import CartOperationFactory
from CartManagement.serializers import CartModelSerializer
from ItemManagement.models import ItemModel


class CartManagement(APIView):

    """ This View Class handles HTTP requests for Cart """
    # Operation is required only for patch request
    # Operation -> Cart Operations : AddItem and DeleteItem

    def get(self, request, operation = None, format = None)-> Response:

        """ This method returns cart details if a user profile is of a buyer """
        data= {'message': str(), 'itemIdList': str()}; statusCode= HTTP_200_OK

        userIns = request.user
        buyerprofileIns = BuyerProfileModel.objects.get(userIns= userIns)
        if buyerprofileIns is None:
            data['message']= 'This is not a Buyer Profile'; statusCode= HTTP_404_NOT_FOUND
            return Response(data= data, status= statusCode)

        cartModelIns= CartModel.objects.filter(buyerprofileIns= buyerprofileIns)
        itemIdList= cartModelIns.itemIdList

        data['message']= 'Cart details fetched successfully'
        data['itemIdList']= itemIdList

        return Response(data= data, status= statusCode)

    def post(self, request, operation= None, format= None)-> Response:
        '''
        Creates Cart Instance for Buyer Profile
        '''
        data= {'message':str(),'cartId': None}; statusCode= HTTP_201_CREATED

        userIns= request.user
        buyerProfileIns= BuyerProfileModel.objects.get(userIns= userIns)

        if buyerProfileIns is None:
            data['message']= 'This is not a Buyer Profile'; statusCode= HTTP_404_NOT_FOUND
        else:
            cartIns= CartModel(buyerProfileIns= buyerProfileIns); cartIns.save()
            data['message']= 'Cart created successfully'; data['cartId']= cartIns.cartId

        return Response(data= data, status= statusCode)

    def patch(self, request, operation, format= None)-> Response:
        '''
        This method handles patch operations in cart of a buyer profile
        '''
        data = {'message': str(), 'itemIdList': str()}
        statusCode= HTTP_200_OK

        userIns= request.user
        itemId= request.data.get('itemId',None)

        buyerprofileIns= BuyerProfileModel.objects.get(userIns= userIns)
        cartModelIns= CartModel.objects.filter(buyerprofileIns= buyerprofileIns)
        itemIdList= cartModelIns.itemIdList

        cartOperationIns= CartOperationFactory(operation, itemIdList, itemId)
        editItemIdList= cartOperationIns.editItemIdList()

        cartModelIns.itemIdList= editItemIdList
        cartModelIns.save()

        data['message']= 'Cart operation done successfully'
        return Response(data= data, status= statusCode)

class ItemInCart(APIView):
    ''' This view handles requests to check whether an item is in Cart or not '''

    def get(self, request, itemId, format= None)-> Response:
        ''' This method returns whether a specific item is in Buyer's Cart '''

        data= {'message': str(), 'itemInCart': None}; status= None

        try: itemId= int(itemId); itemIns= ItemModel.objects.get(itemId= itemId)
        except:
            data['message']= 'No item with Item Id-> {} is found'.format(itemId); status= HTTP_404_NOT_FOUND
            return Response(data= data, status= status)

        buyerProfileIns= BuyerProfileModel.objects.get(userIns= request.user)
        cartIns= list(CartModel.objects.filter(buyerProfileIns= buyerProfileIns))[0]
        itemIdList= [int(itemId_) for itemId_ in cartIns.itemIdList.split(',')]

        itemInCart= True if itemId in itemIdList else False
        data['message'], data['itemInCart'], status = ('Item In Cart', True, HTTP_302_FOUND) if itemInCart else \
            ('Item Not in Cart', False, HTTP_404_NOT_FOUND)

        return Response(data= data, status= status)
