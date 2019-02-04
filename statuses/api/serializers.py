from rest_framework import serializers
from statuses.models import Status

from rest_framework import serializers
class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
         
        fields = [
            'user',
            'content',
            'image'
        ]

    def validate_content(self, value):
        if len(value)>200:
            raise serializers.ValiationError("this is too long")
        return value


    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)

        if content is None and image is None:
            raise serializers.ValiationError("content or image is missing")

        return data
