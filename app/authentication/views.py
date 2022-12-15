from .models import  User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UsersSerializers, CredentialSerializer, DeleteUserSerializers
from app.core import Check_User_Token, Delete_User_Token, Find_User


class UserAuthenticatedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):

        if not Find_User(user_id):
            return Response( status=status.HTTP_404_NOT_FOUND)

        if Check_User_Token(request, user_id):
            user = User.objects.get(id=user_id)  
        
            serializers = UsersSerializers(user)

            return Response(serializers.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    
    def delete(self, request, user_id):
            
        serializers = DeleteUserSerializers(data=request.data)

        if not serializers.is_valid() or not Find_User(user_id):
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(id=user_id)
        
        if  Check_User_Token(request, user_id) and user.check_password(request.data['password']):
            
            User.objects.filter(id=user_id).delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
     
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UsersRegisterView(APIView):
    def post(self, request):

        serializer = UsersSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        find_user_by_email = User.objects.filter(email=request.data['email']).exists()

        if find_user_by_email:
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        
        user = User.objects.create_user(username=request.data['email'],**request.data)

        token = Token.objects.get_or_create(user=user)[0]
      
        serializer = UsersSerializers(user)
        
        return Response({"data": serializer.data, "token":token.key}, status=status.HTTP_201_CREATED)




class LoginView(APIView):
    def post(self, request):

        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        find_user_by_email = User.objects.filter(email=request.data['email']).exists()

        if not find_user_by_email:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        user = authenticate(username=request.data['email'], password=request.data['password'])

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key, "userId": user.id})

  
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)

        if user:
            delete_token = Delete_User_Token(user_id)
            
            if delete_token:
                return Response(status=status.HTTP_200_OK)
     
                
        return Response(status=status.HTTP_404_NOT_FOUND)