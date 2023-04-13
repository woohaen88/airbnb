from django.db import transaction
from rest_framework import serializers
from rooms.models import (
    Amenity,
    Room,
)
from wishlists.models import WishList

from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


from django.http import QueryDict
from typing import Any, Dict

from ast import literal_eval


# type
from django.db.models.query import QuerySet


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
    rating = serializers.SerializerMethodField()

    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    def get_rating(self, room: Room):
        """평점 계산"""
        return room.rating()

    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "photos",
        ]


class RoomDetailSerializer(RoomSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        many=True,
        required=False,
    )
    category = CategorySerializer(required=False)

    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_is_owner(self, room: Room):
        return room.owner == self.context["request"].user

    def get_is_liked(self, room: Room) -> bool:
        request = self.context["request"]
        return WishList.objects.filter(user=request.user, rooms__id=room.id).exists()

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
            "is_owner",
            "is_liked",
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
