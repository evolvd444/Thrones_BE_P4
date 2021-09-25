from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import BathroomSerializer
from thrones_be.models import Bathroom

@api_view(['GET'])
def getRoutes(request):

    routes = [

        {'GET':'/api/bathroom'},
        {'GET':'/api/bathroom/id'},
        {'GET':'/api/bathroom/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]
    return Response(routes)

@api_view(['GET'])
def getBathrooms(request):
    bathrooms = Bathroom.objects.all()
    serializer = BathroomSerializer(bathrooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBathroom(request, pk):
    bathrooms = Bathroom.objects.get(id=pk)
    serializer = BathroomSerializer(bathrooms, many=False)
    return Response(serializer.data)