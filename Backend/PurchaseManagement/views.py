from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from ProfileManagement.models import BuyerProfileModel
from PurchaseManagement.models import PurchaseListModel

class PurchaseListManagement(APIView):
  '''
  This View Class handles Http request for Purchases
  '''
  def get(self, request, format= None)-> Response:
    pass

  def post(self, request, format= None)-> Response:
    '''
    Creates Purchase list for a Buyer Profile
    '''
    data= {'message': str(), 'purchaseListId': None}; statusCode= HTTP_201_CREATED

    userIns= request.user; buyerProfileIns= BuyerProfileModel.objects.get(userIns= userIns)
    if buyerProfileIns is None:
      data['message']= 'This is not a Buyer Profile'; statusCode= HTTP_404_NOT_FOUND
    else:
      purchaseListIns= PurchaseListModel(buyerProfileIns= buyerProfileIns); purchaseListId= purchaseListIns.purchaseListId
      data['message']= 'Purchase list created successfully'; data['purchaseListId']= purchaseListId

    return Response(data= data, status= statusCode)

  def patch(self, request, format= None)-> Response: pass
  