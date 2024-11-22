from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from producer.serializers import MessageSerializer


class ProducerView(APIView):
    def post(self, request: Request) -> Response:
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_message()
        return Response(status=status.HTTP_200_OK)