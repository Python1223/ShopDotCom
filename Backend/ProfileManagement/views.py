from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
class Profile(APIView):
  authentication_classes= [JWTAuthentication]
  permission_classes= [IsAuthenticated]
  
  def get(self, request, format= None):
    print('request-> ', request.user, request.data, request.headers)
    return Response(data= {}, status= HTTP_200_OK)

