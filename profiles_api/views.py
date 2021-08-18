from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Return a list of APIView function"""
        an_apiview = [
            'use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
