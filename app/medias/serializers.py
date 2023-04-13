from medias.models import (
    Photo,
    Video,
)

from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "file",
            "description",
            "room",
            "experience",
        ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            "file",
            "experience",
        ]
