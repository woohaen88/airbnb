from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from common.models import CommonModel


class Room(CommonModel):
    """
    Model Definition for Room

    Args:
        Required:
            country: str, default: 한국
            city: str, default: 서울
            name: str,
            price: int,
            rooms: int,
            toilets: int,
            description: str, default:""
            address: str, default: ""
            pet_friendly: bool, default: true
            kind: choice, [entire_place, private_room, shared_room]
            [FK] owner: request.user
            [MtoM] amenities: rooms.Amenity
        Optional:

    """

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = "entire_place", _("Entire Place")
        PRIVATE_ROOM = "private_room", _("Private Room")
        SHARED_ROOM = "shared_room", _("Shared Room")

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        _("Name"),
        max_length=150,
    )
    price = models.PositiveIntegerField(
        _("Price"),
    )
    rooms = models.PositiveIntegerField(
        _("Room"),
    )
    toilets = models.PositiveIntegerField(
        _("Toilet"),
    )
    description = models.TextField(
        _("Description"),
        default="",
    )
    address = models.CharField(
        _("Address"),
        max_length=250,
        default="",
    )
    pet_friendly = models.BooleanField(
        _("Pet Friendly"),
        default=True,
    )

    kind = models.CharField(
        _("Kind"),
        max_length=20,
        choices=RoomKindChoices.choices,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("OWNER"),
        on_delete=models.CASCADE,
        related_name="rooms",
    )

    amenities = models.ManyToManyField(
        "rooms.Amenity",
        verbose_name=_("Amenity"),
    )

    def __str__(self) -> str:
        return self.name


class Amenity(models.Model):
    """Amenity Definition

    Args:
        required:
            name: str
        optional:
            description: str
    """

    name = models.CharField(
        _("Amenity Name"),
        max_length=150,
    )
    description = models.CharField(
        _("Description"),
        max_length=150,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Amenities"

    def __str__(self) -> str:
        return self.name
