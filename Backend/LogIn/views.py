from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
class LogIn(APIView):
    authentication_classes= [BasicAuthentication]
    permission_classes= [AllowAny]

    def post(self, request, format= None)-> Response:
        data= {'message': str()}; statusCode= None

        print("request-> ", request.data, request.headers)
        requestData= request.data
        username= requestData.get('Username', None)
        password = requestData.get('Password',None)

        userExistanceFlag= authenticate(username= username, password= password)

        if userExistanceFlag is not None:
            login(request, userExistanceFlag)
            data['message']= 'Successfully Logged In'
            statusCode= HTTP_200_OK
            return Response(data= data, status= statusCode)
        else:
            data['message']= 'Please LogIn with correct credentials'
            statusCode= HTTP_400_BAD_REQUEST
            return Response(data= data, status= statusCode)
            