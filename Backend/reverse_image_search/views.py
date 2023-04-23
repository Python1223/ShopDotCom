from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from typing import Any, Optional


class ReverseImageSearch(APIView):

    authentication_classes: list = [JWTAuthentication]
    parser_classes: list = [MultiPartParser, FormParser]
    permission_classes: list = [IsAuthenticated]

    def post(self, request: Request, format: Optional[Any] = None) -> Response:
        data: dict = {'message': str(),
                      'item_ids': list()}
        status: int = 0
        image_url: str = request.data.get('Image', None)

        if image_url is None:
            data['message'] = "No input image found"
            status = HTTP_400_BAD_REQUEST
            return Response(data=data, status=status)

        item_ids: list[int] = [1, 2, 3, 4]
        data['message'] = "Similar Item Ids fetched successfully"
        data['item_ids'].extend(item_ids)
        status = HTTP_200_OK

        return Response(data=data, status=status)
