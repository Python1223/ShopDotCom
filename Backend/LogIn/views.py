from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


# Create your views here.

class LogIn(APIView):

    authentication_classes= [BasicAuthentication]
    permission_classes= [AllowAny]

    def post(self ,request ,format= None):
        requestData= request.data

        username= requestData.get('Username', None)
        password = requestData.get('Password',None)

        userExistanceFlag= authenticate(username= username, password= password)

        if userExistanceFlag is not None:
            login(
                request,
                userExistanceFlag
            )
            data={
                'msg' : 'Logged In'
            }
            return Response(data= data, status= HTTP_200_OK)

        else:
            data={
                'msg' : 'Please LogIn with correct credentials'
            }
            return Response(data= data, status= HTTP_200_OK)