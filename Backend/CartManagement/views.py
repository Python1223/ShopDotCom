from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from ProfileManagement.models import ProfileModel, BuyerProfileModel
from CartManagement.models import CartModel
from CartManagement.CartOperations import CartOperation, CartOperationFactory
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
        statusCode= None

        userIns= request.user
        profileModelIns= ProfileModel.objects.filter(userIns= userIns)

        if profileModelIns is None:
            data['message']= 'Profile not found for requested user'
            statusCode= HTTP_200_OK

        elif ProfileModel.isBuyer(profileModelIns= profileModelIns):
            buyerProfileModeIns= BuyerProfileModel.objects.get(profileId= profileModelIns.profileId)
            cartId= buyerProfileModeIns.cartId
            cartModelIns= CartModel.objects.get(cartId= cartId)
            
            data['message']= 'Cart details fetched successfully'
            data['itemIdList']= cartModelIns.itemIdList
            statusCode= HTTP_200_OK

        elif profileModelIns.isSeller(profileModelIns= profileModelIns):
            data['message']= 'User is a seller and has no cart'
            statusCode= HTTP_200_OK

        else:
            data['message']= 'User is neither a buyer nor a seller'
            statusCode= HTTP_200_OK

        return Response(data= data, status= statusCode)

    def patch(self, request, operation, format= None)-> Response:
        '''
        This method handles post operations in cart of a buyer profile
        '''
        userIns= request.user
        itemId= request.data.get('itemId',None)
        
        profileModelIns= ProfileModel.objects.filter(userIns= userIns)
        buyerProfileModelIns= BuyerProfileModel.objects.get(profileModelIns= profileModelIns)
        cartId= buyerProfileModelIns.cartId
        cartModelIns= CartModel.objects.get(cartId= cartId)
        itemIdList= cartModelIns.itemIdList
        
        cartOperationIns= CartOperationFactory(operation, itemIdList, itemId)
        editItemIdList= cartOperationIns.editItemIdList()

        data= {
            'itemIdList': editItemIdList
        }
        cartModelIns= CartModelSerializer(cartModelIns, data= data ,partial= True)
        if cartModelIns.is_valid(): 
            cartModelIns.save()
            return Response({'msg': 'Data Updated'}, status= HTTP_200_OK)

        return Response(cartModelIns.errors, status= HTTP_200_OK)


        







        






        



