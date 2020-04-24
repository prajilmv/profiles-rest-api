from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """test API View"""
    serializer_class = serializers.HelloSerilizers

    def get(self, request, format=None):
        """returns a lsit of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, pathc, put, delete)',
            'Is similar to a tradiational Django view',
            'Gives u the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, reqesut, pk=None):
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
