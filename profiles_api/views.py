from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        an_apiview = [

            'Uses HTTP Methods as a function (get, put, patch, post, delete)',
            'It is Similar to a Tradisional Django View',
            'Gives You the Most control over your application logic',
            'Is mapped manually to Urls',

        ]

        return Response({'message':'Hello!!','an_apiview':an_apiview})


    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a Partial update of an Object"""
        return Response({'method':'PATACH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})
