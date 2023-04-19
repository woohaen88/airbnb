import time
from django.db import transaction
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import (
    ParseError,
    NotFound,
)
from rest_framework.response import Response
from rest_framework import status
from reviews.models import Review


from rooms.models import (
    Amenity,
    Room,
)
from bookings.models import Booking

# serializer
from categories.models import Category
from rooms.serializers import (
    AmenitySerializer,
    RoomSerializer,
    RoomDetailSerializer,
    AmenityCreateSerializer,
)
from reviews.serializers import ReviewSerializer
from bookings.serializers import (
    PublicBookingSerializer,
    CreateBookingSerializer,
)

from ast import literal_eval

# type
from django.http import QueryDict
from typing import Any, Dict

# pagenation
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone


# GET POST /amenity
# GET PUT DELETE /amenity/1


#     ListModelMixin,
#     CreateModelMixin,
#     RetrieveModelMixin,
#     DestroyModelMixin,
#     UpdateModelMixin,
#     GenericViewSet
class AmenityView(ModelViewSet):
    serializer_class = AmenityCreateSerializer
    queryset = Amenity.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "amenity_id"

    def perform_create(self, serializer):
        name = self.request.data.get("name")
        if Amenity.objects.filter(name=name).exists():
            raise ParseError("Amenity이름이 중복됩니다.")
        serializer.save()


class RoomView(ModelViewSet):
    serializer_class = RoomDetailSerializer
    queryset = Room.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "room_id"

    def get_serializer_class(self):
        if self.action == "list":
            return RoomSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        category_dict = self.request.data.get("category")
        if isinstance(category_dict, str):
            category_dict = literal_eval(category_dict)
        try:
            category = Category.objects.get(name=category_dict.get("name"))
            if category.kind != Category.CategoryKindChoices.ROOMS:
                raise ParseError("Category Kind should be rooms")
        except Category.DoesNotExist:
            raise ParseError("Category Name Not Found")

        with transaction.atomic():
            serializer.save(owner=self.request.user, category=category)

    def retrieve(self, request, *args, **kwargs):
        time.sleep(2)
        return super().retrieve(request, *args, **kwargs)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class RoomReviewsView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"
    lookup_url_kwarg = "room_id"
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_object().reviews.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RoomBookingViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Room.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "room_id"
    serializer_class = PublicBookingSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookingSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        room = self.get_object()

        now = timezone.localtime(timezone.now()).date()

        # 미래의 예약만
        bookings = Booking.objects.filter(
            room=room,
            kind=Booking.BookingKindChoices.ROOM,
            check_in__gt=now,
        )

        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        room_id = self.kwargs.get("room_id")
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise NotFound

        # room,
        serializer.save(
            room=room,
            user=self.request.user,
            kind=Booking.BookingKindChoices.ROOM,
        )
