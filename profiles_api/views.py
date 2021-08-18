from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self,request,format=None):
        """Return a list of APIView function"""
        an_apiview = [
            'use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk =None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def delete(self, request, pk=None):
        """handle delete an object"""
        return Response({'method':'DELETE'})
