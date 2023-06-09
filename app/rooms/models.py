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

        Optional:
        Relation:
            [FK] owner: setting.AUTH_USER_MODEL
            [FK] category: categories.Category
            [MtoM] amenities: rooms.Amenity

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
        null=True,
        blank=True,
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
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        "categories.Category",
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return 0

        total_rating = 0
        for review in room.reviews.all().values("rating"):
            total_rating += review["rating"]
        return round(total_rating / count, 2)

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
