from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
)

from categories.serializers import CategorySerializer
from categories.models import Category

from drf_spectacular.utils import extend_schema


class CategoryView(
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Category.objects.all().filter(kind=Category.CategoryKindChoices.ROOMS)
    serializer_class = CategorySerializer

    lookup_field = "id"
    lookup_url_kwarg = "category_id"
