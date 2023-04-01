from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from ItemManagement.models import ItemModel
from ProductDashboardManagement.utils import getFilter

COUNT_POSITIVES: int= 100

class ProductDashboardManagement(APIView):
    global COUNT_POSITIVES

    def get(self, request, format= None)-> Response:
        '''This method returns a list of item ids for Product Dashboard frontend'''

        itemList= list(ItemModel.objects.all()); totalElements= len(itemList)
        filter_= getFilter(totalElements= totalElements, countPositives= COUNT_POSITIVES)

        filteredItemList= list()
        for index_, toBeIncludedFlag in enumerate(filter_): 
           if toBeIncludedFlag: filteredItemList.append(itemList[index_].itemId)

        data= {'message': 'Item List fetched successfuly',
               'itemList': filteredItemList
               }
        status= HTTP_200_OK
        return Response(data= data, status= status)