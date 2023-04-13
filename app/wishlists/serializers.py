from rest_framework import serializers
from wishlists.models import WishList

# serializer
from users.serializers import TinyUserSerializer
from rooms.serializers import RoomSerializer


class WishListSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    rooms = RoomSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = WishList
        fields = [
            "id",
            "name",
            "rooms",
            "user",
        ]
