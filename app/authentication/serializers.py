from rest_framework import serializers


class UsersSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
        

class DeleteUserSerializers(serializers.Serializer):
    password = serializers.CharField()


class CredentialSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


