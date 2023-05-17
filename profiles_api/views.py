from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test APIView"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses functions as HTTP methods',
            'Is similar to a traditional Django View',
            'Gives you the most controll over the aplicvation logic',
            'is mapped manualy to URLs'
        ]
        return Response({'message': 'Hello','an_apiview':an_apiview})
