from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LahanSerializer
from .models import lahan
from rest_framework.parsers import MultiPartParser, FormParser


from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


@api_view(['POST'])
def add_lahan(request, pk):
    request.data['user'] = pk
    lahan = LahanSerializer(data=request.data)
    # for i in range(5):
    #     if (request.data['imgGreenhouse'+str(i)]) is None:
    #         print("no data")
    #     else:
    #         print(request.data)

    if lahan.is_valid():
        lahan.save()
        return Response(data={"status": status.HTTP_201_CREATED, "message": "Berhasil Menambahkan Data", "data": lahan.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"status": status.HTTP_404_NOT_FOUND, "message": "Data Tidak Dapat Ditambahkan", "data": lahan.data}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_lahan(request):
    jwt_authenticator = JWTAuthentication()
    response = jwt_authenticator.authenticate(request)

    if response is None:
        return Response({"detail": "authentication credentials were not provided."}, status=401)
    _, token = response
    user_id = token.payload['user_id']
    data = lahan.objects.filter(user=user_id)
    serializer = LahanSerializer(data, many=True)
    return Response({"data": serializer.data})


@api_view(['GET'])
def detail_lahan(request, pk):
    data = lahan.objects.filter(id=pk)
    serializer = LahanSerializer(data, many=True)
    return Response({"data": serializer.data})
