from django.db import transaction
from rest_framework.permissions import IsAuthenticated
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


from rooms.models import (
    Amenity,
    Room,
)

from categories.models import Category
from rooms.serializers import AmenitySerializer, RoomSerializer, RoomDetailSerializer

from ast import literal_eval

# type
from django.http import QueryDict
from typing import Any, Dict


# GET POST /amenity
# GET PUT DELETE /amenity/1


#     ListModelMixin,
#     CreateModelMixin,
#     RetrieveModelMixin,
#     DestroyModelMixin,
#     UpdateModelMixin,
#     GenericViewSet
class AmenityView(ModelViewSet):
    serializer_class = AmenitySerializer
    queryset = Amenity.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "amenity_id"


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
