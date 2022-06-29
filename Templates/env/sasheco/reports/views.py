from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse 
from .models import Guest,Moive,Reservation
from rest_framework.decorators import api_view
from .serializers import Guestserializer,Movieserializer,Reservationserializer   
from rest_framework.response import Response
from rest_framework import status , filters



# Create your views here.


def index(request):

    return render(request, 'pages/index.html')


# 1 without Rest and no model query
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            'Name': 'madkour',
            'mobile': 1004582452,
        },
        {
            'id': 2,
            'name': 'drenn',
            'mobile': 774552,
        }
    ]
    return JsonResponse(guests, safe=False)
#2 model data default django without rest
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests':list(data.values('name','mobile'))
    }
    return JsonResponse(response)


# List == Get
# create == post
# pk query == Get     item from list
# update == put
# Delete or destory == delete


#3 Function based Views
#3.1 Get Post
@api_view(['GET','POST'])            #Name this decorator
def FBV_List(request):
    #Get
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializers = Guestserializer(guests, many =True )
        return Response(serializers.data)
    #post    
    elif request.method == 'POST':
        serializers = Guestserializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
# #3.2 GUT put Delete
# @api_view()
# def FBV_pk(request , pk):
#     #GET
#         if request.method == 'Get':
#         guests = Guest.objects.all()
#         serializers = Guestserializer(guests, many =True )
#         return response(serializers.data)
#     #put    
#     elif request.method == 'PUT':
#         serializers = Guestserializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#     #DELETE    
#     elif request.method == 'DELETE':
#         serializers = Guestserializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)





