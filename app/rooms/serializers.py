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


# class AmenityCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Amenity
#         fields = [
#             "id",
#             "name",
#             "description",
#         ]
#         # read_only_fields = ["description"]

#     def validate(self, attrs):
#         print("amenities: 본체:")


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = [
            "id",
            "name",
            "description",
        ]
        # read_only_fields = [
        #     "description",
        #     "name",
        # ]

    def validate(self, attrs):
        print("here")
        print("attrs: ", attrs)


class RoomSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    def get_rating(self, room: Room):
        """평점 계산"""
        return room.rating()

    def get_is_owner(self, room: Room) -> bool:
        request = self.context["request"]
        if request:
            return room.owner == request.user
        return False

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
            "is_owner",
        ]


class RoomDetailSerializer(RoomSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        many=True,
        required=False,
        read_only=True,
    )
    category = CategorySerializer(
        required=False,
        read_only=True,
    )

    is_owner = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_is_owner(self, room: Room):
        request = self.context.get("request")
        if request:
            return room.owner == self.context["request"].user
        return False

    def get_is_liked(self, room: Room) -> bool:
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return WishList.objects.filter(
                    user=request.user, rooms__id=room.id
                ).exists()

        return False

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
            "is_liked",
        ]

    def create(self, validated_data):
        amenities = self.context["request"].data.get("amenities", [])

        if isinstance(amenities, str):
            validated_data["amenities"] = literal_eval(amenities)

        try:
            with transaction.atomic():
                room = Room.objects.create(**validated_data)

                for amenity in amenities:
                    amenity_obj = Amenity.objects.get(id=amenity)
                    room.amenities.add(amenity_obj)
                    room.save()

                return room
        except Exception:
            raise serializers.ValidationError("Amenity not found")
