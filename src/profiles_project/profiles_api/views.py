from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView featurs"""

        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Djnago view',
            'Gives you the most control over your logic',
            'Is mappped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
