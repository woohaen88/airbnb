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
from reviews.models import Review


from rooms.models import (
    Amenity,
    Room,
)

# serializer
from categories.models import Category
from rooms.serializers import AmenitySerializer, RoomSerializer, RoomDetailSerializer
from reviews.serializers import ReviewSerializer

from ast import literal_eval

# type
from django.http import QueryDict
from typing import Any, Dict

# pagenation
from rest_framework.pagination import PageNumberPagination

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
