from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import NotifikasiSerializer
from .models import notifikasi

from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication


# @api_view(['POST'])
# def add_notifikasi(request, pk):
#     request.data['user'] = pk
#     # request.data['lahan'] = pk
#     notifikasi = NotifikasiSerializer(data=request.data)

#     if notifikasi.is_valid():
#         notifikasi.save()
#         return Response(data={"status": status.HTTP_201_CREATED, "message": "Berhasil Menambahkan Data", "data": notifikasi.data}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(data={"status": status.HTTP_404_NOT_FOUND, "message": "Data Tidak Dapat Ditambahkan", "data": notifikasi.data}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def list_notifikasi(request, pk):
#     print(pk)
#     data = notifikasi.objects.filter(id=pk)
#     serializer = NotifikasiSerializer(data, many=True)
#     return Response({"data": serializer.data})


@api_view(['GET'])
def list_notifikasi(request):
    jwt_authenticator = JWTAuthentication()
    response = jwt_authenticator.authenticate(request)

    if response is None:
        return Response({"detail": "authentication credentials were not provided."}, status=401)
    _, token = response
    user_id = token.payload['user_id']
    data = notifikasi.objects.filter(user=user_id)
    serializer = NotifikasiSerializer(data, many=True)
    return Response({"data": serializer.data})
