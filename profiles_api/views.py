from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""


    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        an_apiview = [

            'Uses HTTP Methods as a function (get, put, patch, post, delete)',
            'It is Similar to a Tradisional Django View',
            'Gives You the Most control over your application logic',
            'Is mapped manually to Urls',

        ]

        return Response({'message':'Hello!!','an_apiview':an_apiview})
