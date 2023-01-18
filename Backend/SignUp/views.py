from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from ProfileManagement.Profiles import ProfileFactory
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.db.models import Q

def checkEmailExistance(email: str)-> bool:
    '''
    checkEmailExistance checks whether the inputted email is already registered 
    or not
    '''
    querySet= User.objects.filter(Q(email= email))

    if len(list(querySet))== 0: return False
    else: return True


def checkNameExistance(username: str)-> bool:
    '''
    checkNameExistance checks whether the inputted name is already registered 
    or not
    '''
    querySet= User.objects.filter(Q(username= username))

    if len(list(querySet))== 0: return False
    else: return True

class SignUp(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format= None)-> Response:
        data= {'message': str()}; statusCode= None

        requestData= request.data
        username= requestData.get('Username', None)
        email = requestData.get('Email',None)
        password = requestData.get('Password',None)
        profileString= requestData.get('ProfileString', None)
        storeName= requestData.get('StoreName', None)

        if profileString not in ('Buyer', 'Seller'):
            data['message']= 'Please provide correct profile type'
            statusCode= HTTP_200_OK

            return Response(data= data, status= statusCode)

        duplicateNameFlag= checkNameExistance(username)

        if duplicateNameFlag:
            data['message']= {'Please try with different Name'}
            statusCode= HTTP_200_OK

            return Response(data= data, status= statusCode)

        duplicateEmailFlag= checkEmailExistance(email)

        if duplicateEmailFlag:
            data['message']= {'Please try with different Email'}
            statusCode= HTTP_200_OK

            return Response(data= data, status= statusCode)

        userIns= User(username= username, email= email, password= password)
        userIns.set_password(password); userIns.save()

        profileIns= ProfileFactory.getProfileIns(profileString= profileString, userIns= userIns, storeName= storeName)
        op= profileIns.setProfileResources()

        print("op-> {}".format(op))
        data['message']= 'Profile Created Successfully'
        statusCode= HTTP_201_CREATED

        return Response(data= data, status= statusCode)
