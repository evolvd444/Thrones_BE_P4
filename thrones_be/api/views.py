from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import BathroomSerializer
from .serializers import ProfileSerializer
from .serializers import ReviewSerializer, ThroneSerializer
from thrones_be.models import Bathroom, Review
from users.models import Profile
from rest_framework import viewsets


class ThroneList(viewsets.ModelViewSet):
    queryset = Bathroom.objects.all()
    serializer_class = BathroomSerializer

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getRoutes(request):

#     routes = [
#         {'GET':'/api/throne'},
#         {'GET':'/api/thrones'},
#         {'GET':'/api/thrones/id'},
#         {'GET':'/api/thrones/id/vote'},
#         {'POST': '/api/thrones/create-throne'},
#         {'PUT': '/api/thrones/edit-throne'},
#         {'DELETE': '/api/thrones/delete-throne'},
#         {'POST': '/api/profiles/'},
#         {'POST': '/api/profiles/id'},

#     ]
#     return Response(routes)



# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getBathrooms(request):
#     bathrooms = Bathroom.objects.all()
#     serializer = ThroneSerializer(bathrooms, many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getThrone(request):
#     bathrooms = Bathroom.objects.all()
#     serializer = BathroomSerializer(bathrooms, many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getUsers(request):
#     profile = Profile.objects.all()
#     serializer = ProfileSerializer(profile, many = True)
#     return Response(serializer.data)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getUser(request,pk):
#     profile = Profile.objects.get(id=pk)
#     serializer = ProfileSerializer(profile, many = False)
#     return Response(serializer.data)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getBathroom(request, pk):
#     bathroom = Bathroom.objects.get(id=pk)
#     serializer = BathroomSerializer(bathroom, many=False)
#     return Response(serializer.data)

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def getReviews(request):
#     reviews = Review.objects.all()
#     serializer = ReviewSerializer(reviews, many = True)
#     return Response(serializer.data)


