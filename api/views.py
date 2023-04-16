from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions, status
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication


# Register API


@api_view(['POST'])
def RegisterAPI(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(data={"status": status.HTTP_201_CREATED, "message": "Berhasil Menambahkan Data", "data": user.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(data={"status": status.HTTP_404_NOT_FOUND, "message": "Data Tidak Dapat Ditambahkan", "data": user.data}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def LoginAPI(request):
    user = authenticate(
        email=request.data['email'], password=request.data['password'])
    if user is None:
        return Response({
            "status": False,
            "Message": "Data yang anda masukan tidak sesuai"
        }, status=401)

    return Response({
        "status": True,
        "Message": "Berhasil Login"
    }, status=200)


class UserAPiView(RetrieveAPIView):
    permissions_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# class LogoutView(UserAPiView):
#     permission_classes = (IsAuthenticated,)

#     @requires_csrf_token
#     @csrf_exempt
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"status": True,
                         "Message": "Berhasil LogOut"
                         }, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer


@api_view(['GET'])
def getAlluser(request):
    data = User.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response({"data": serializer.data})


@api_view(['GET'])
def getDetailuser(request):
    jwt_authenticator = JWTAuthentication()
    response = jwt_authenticator.authenticate(request)

    if response is None:
        return Response({"detail": "authentication credentials were not provided."}, status=401)
    _, token = response
    user_id = token.payload['user_id']
    data = User.objects.filter(id=user_id)
    serializer = UserSerializer(data, many=True)
    return Response({"data": serializer.data})
