from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from ProfileManagement.ProfileFactory import ProfileFactory
from ProfileManagement.models import ProfileModel
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.db.models import Q

def checkExistanceUsername(username):
    querySet= User.objects.filter(
        Q(username= username)
    )
    if len(list(querySet))== 0:
        return False

    else: return True

def checkExistanceEmail(email):
    querySet= User.objects.filter(
        Q(email= email)
    )
    if len(list(querySet))== 0:
        return False

    else: return True


class SignUp(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format= None):
        requestData= request.data
        username= requestData.get('Username', None)
        email = requestData.get('Email',None)
        password = requestData.get('Password',None)
        profileString= requestData.get('ProfileString', None)

        duplicateUsernameFlag= checkExistanceUsername(username)
        duplicateEmailFlag= checkExistanceEmail(email)

        if duplicateUsernameFlag:
            data={
                'msg': 'Please try with different Username',
            }
            return Response(data= data, status= HTTP_200_OK)

        if duplicateEmailFlag:
            data={
                'msg': 'Please try with different Email',
            }
            return Response(data= data, status= HTTP_200_OK)

        profileTypeModelIns= ProfileFactory.getProfileModelIns(profileString= profileString) #-> BuyerIns / SellerIns / None
        if profileTypeModelIns is None:
            data= {
                'msg': 'Please provide correct profile type. User not created'
            }
            return Response(data= data, status= HTTP_200_OK)

        userIns= User(username= username, email= email, password= password)
        userIns.set_password(password); userIns.save()
        
        ProfileModel(userIns=userIns, profileType=profileString).save()
        profileTypeModelIns.save()

        return Response(data= {'msg': 'User created'}, status= HTTP_201_CREATED)