from rest_framework import serializers
from experiences.models import Perk


class PerksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = [
            "id",
            "name",
            "details",
            "explanation",
            "updated_at",
            "created_at",
        ]
