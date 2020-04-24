from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test API View"""
    def get(self, request, format=None):
        """returns a lsit of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, pathc, put, delete)',
            'Is similar to a tradiational Django view',
            'Gives u the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
