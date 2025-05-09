from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import *
from .models import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

#READ
@api_view(['GET'])
def contact_read(request):
    contact_obj=ContactModel.objects.all()
    serializer=Contactserializers(contact_obj,many=True)
    return Response({'status':200,'payload':serializer.data})

#CREATE
@api_view(['POST'])
def contact_create(request):
    contact_obj=ContactModel.objects.all()
    serializer=Contactserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200,'payload':serializer.data})

     

#UPDATE
@api_view(['POST'])
def contact_update(request,id):
    contact_obj=ContactModel.objects.get(id=id)
    serializer=Contactserializers(instance=contact_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200,'payload':serializer.data})


#DELETE
@api_view(['DELETE'])
def contact_delete(request,id):
    contact_obj=ContactModel.objects.get(id=id)
    contact_obj.delete()
    return Response("This Contact Is Deleted")

#VIEW
@api_view(['GET'])
def contact_view(request,id):
    contact_obj=ContactModel.objects.get(id=id)
    serializer=Contactserializers(contact_obj)
    return Response({'status':200,'payload':serializer.data})


    
