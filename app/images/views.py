from app.core import Find_User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from images.models import Images
from images.serializers import ImageSerializers
from authentication.models import User


class ImagesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    

    def post(self, request):

        serializer = ImageSerializers(data=request.data)
        
        if not serializer.is_valid:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        user_id = request.data['user_id']

        if not Find_User(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(id=user_id)

        Images.objects.create(user=user, image=request.data['image'])

        return Response( status=status.HTTP_201_CREATED)


    def get(self, request, user_id):
        
        found_image = Images.objects.filter(user_id=user_id)

        if not found_image or not Find_User(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializers = ImageSerializers(found_image, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)


    def put(self, request):
        found_image = Images.objects.filter(id=request.data['image_id'], user_id=request.data['user_id'])

        if not found_image or not Find_User(user_id=request.data['user_id']):
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(id=request.data['user_id'])
        
        new_image = Images.objects.get(id=request.data['image_id'], user=user)
        new_image.image = request.data['image']
        new_image.save()

        serializers = ImageSerializers(new_image)

        return Response(serializers.data, status=status.HTTP_200_OK)

     
