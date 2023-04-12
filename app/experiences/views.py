from rest_framework.viewsets import ModelViewSet
from experiences.models import Perk
from experiences.serializers import PerksSerializer
from rest_framework.permissions import IsAuthenticated


class PerksViewset(ModelViewSet):
    queryset = Perk.objects.all()
    serializer_class = PerksSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "perk_id"
