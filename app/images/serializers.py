from rest_framework import serializers


class ImageSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    user_id = serializers.IntegerField()

    