from django.db import models
from common.models import CommonModel

from django.conf import settings


class House(CommonModel):
    """Model definition for House"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="houses",
    )

    def __str__(self) -> str:
        return self.name
