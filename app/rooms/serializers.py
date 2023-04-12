from django.db import transaction
from rest_framework import serializers
from rooms.models import (
    Amenity,
    Room,
)

from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer

from django.http import QueryDict
from typing import Any, Dict

from ast import literal_eval


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = [
            "id",
            "name",
            "description",
        ]
        read_only_fields = ["description"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "country",
            "city",
            "price",
        ]


class RoomDetailSerializer(RoomSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        many=True,
        required=False,
    )
    category = CategorySerializer(required=False)

    class Meta(RoomSerializer.Meta):
        fields = RoomSerializer.Meta.fields + [
            "amenities",
            "rooms",
            "toilets",
            "description",
            "address",
            "pet_friendly",
            "kind",
            "owner",
            "category",
        ]

    def create(self, validated_data):
        amenities = self.context["request"].data.get("amenities")
        if isinstance(amenities, str):
            validated_data["amenities"] = literal_eval(amenities)

        amenities = validated_data.pop("amenities", [])

        try:
            with transaction.atomic():
                room = Room.objects.create(**validated_data)

                for amenity in amenities:
                    amenity_obj = Amenity.objects.get(**amenity)
                    room.amenities.add(amenity_obj)
                return room
        except Exception:
            raise serializers.ValidationError("Amenity not found")
