from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import AktuatorSerializer
from .models import aktuator
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['PUT'])
def add_aktuator(request, pk):
    request.data['user'] = pk
    aktuator = AktuatorSerializer(data=request.data)

    if aktuator.is_valid():
        aktuator.save()
        return Response(data={"status": status.HTTP_201_CREATED, "message": "Berhasil Menambahkan Data", "data": aktuator.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"status": status.HTTP_404_NOT_FOUND, "message": "Data Tidak Dapat Ditambahkan", "data": aktuator.data}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_aktuator(request):
    jwt_authenticator = JWTAuthentication()
    response = jwt_authenticator.authenticate(request)

    if response is None:
        return Response({"detail": "authentication credentials were not provided."}, status=401)
    _, token = response
    user_id = token.payload['user_id']
    data = aktuator.objects.filter(user=user_id)[:1]
    serializer = AktuatorSerializer(data, many=True)
    return Response({"data": serializer.data})
