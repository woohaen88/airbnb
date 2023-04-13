from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from wishlists.models import WishList
from wishlists.serializers import WishListSerializer

from rooms.models import Room


class WishlistsViewSet(ModelViewSet):
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "wishlist_id"
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class WishListToggle(ModelViewSet):
    serializer_class = None
    queryset = None
    permission_classes = [IsAuthenticated]

    def get_object(self, wishlist_id, user):
        try:
            return WishList.objects.get(id=wishlist_id, user=user)
        except WishList.DoesNotExist:
            raise NotFound

    def get_room(self, room_id):
        try:
            return Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise NotFound

    def update(self, request, *args, **kwargs):
        wishlist_id = kwargs["wishlist_id"]
        room_id = kwargs["room_id"]

        wishlist = self.get_object(wishlist_id, request.user)
        room = self.get_room(room_id)

        if wishlist.rooms.filter(id=room.id).exists():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)

        return Response(status=status.HTTP_200_OK)

    #     if wishlist.rooms.filter(pk=room.pk).exists():
    #         wishlist.rooms.remove(room)
    #     else:
    #         wishlist.rooms.add(room)
    #     # check
    #     # 이 room이 wishlist에 있는지 확인
    #     # wishlist는 MtoM인 rooms -> list를 가지고 있음

    #     return super().update(request, *args, **kwargs)
