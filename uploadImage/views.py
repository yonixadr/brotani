from .models import FileUpload  # import the model
# import the serializer
from .serializers import FileUploadDisplaySerializer, FileUploadSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication


class FileUploadView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FileUploadDisplaySerializer

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():  # validate the serialized data to make sure its valid
            qs = serializer.save()
            message = {'detail': qs, 'status': True}
            return Response(message, status=status.HTTP_201_CREATED)
        else:  # if the serialzed data is not valid, return erro response
            data = {"detail": serializer.errors, 'status': False}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return FileUpload.objects.all()


@api_view(['GET'])
def detail_image(request):
    jwt_authenticator = JWTAuthentication()
    response = jwt_authenticator.authenticate(request)

    if response is None:
        return Response({"detail": "authentication credentials were not provided."}, status=401)
    _, token = response
    user_id = token.payload['user_id']
    data = FileUpload.objects.filter(user=user_id)
    serializer = FileUploadSerializer(data, many=True)
    return Response({"data": serializer.data})
