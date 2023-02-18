from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel
from ProfileManagement.serializers import BuyerSerializer, SellerSerializer
from django.contrib.auth.models import User

class Profile(APIView):
  authentication_classes= [JWTAuthentication]
  permission_classes= [IsAuthenticated]
  
  def get(self, request, format= None)-> Response:
    ''' This method returns Profile details given a userId '''

    data= {'message': str(), 'profile': None}; status= HTTP_200_OK
    userIns= User.objects.get(userIns= request.user)
    
    try: 
      profileIns= BuyerProfileModel.objects.get(userIns= userIns)
      seraializedProfileIns= BuyerSerializer(profileIns)
    except: 
      try: 
        profileIns= SellerProfileModel.objects.get(userIns= userIns)
        seraializedProfileIns= SellerSerializer(profileIns)
      except: 
        data['message']= 'No profile is found'; status= HTTP_404_NOT_FOUND
        return Response(data= data, status= status)

    data['message']= 'Profile instance fetched successfully'; data['profile']= seraializedProfileIns.data
    status= HTTP_200_OK
    return Response(data= data, status= status)
    