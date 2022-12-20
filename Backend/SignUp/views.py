from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from ProfileManagement.ProfileFactory import ProfileFactory
from ProfileManagement.models import ProfileModel

class SignUp(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format= None):
        requestData= request.data
        username= requestData.get('Username', None)
        email = requestData.get('Email',None)
        password = requestData.get('Password',None)
        profileString= requestData.get('ProfileString', None)

        userIns= User(username= username, email= email, password= password)

        profileModelIns= ProfileModel(userIns=userIns, profileType=profileString)
        profileIns= ProfileFactory.getProfileModelIns(profileString= profileString) #-> BuyerIns / SellerIns / None