from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonModel
from django.conf import settings


class Experience(CommonModel):
    """
    Definition Model for Experience

    Args:
        required:
            country: str, default: "한국"
            city: str, default: "서울"
            name: str
            price: int
            address: str
            start_at: time
            end_at: time
            description: str


        relation:
            [FK] host: settings.AUTH_USER_MODEL
            [FK] category: "categories.Category"
            [MtoM] perks: "experiences.Perk"

    """

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

    # foreignkey
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiences",
    )

    price = models.PositiveIntegerField(
        _("Price"),
    )

    address = models.CharField(
        _("Address"),
        max_length=250,
    )
    start_at = models.TimeField(
        _("Start at"),
        auto_now=False,
        auto_now_add=False,
    )
    end_at = models.TimeField(
        _("End at"),
        auto_now=False,
        auto_now_add=False,
    )
    description = models.TextField(_("Description"))
    perks = models.ManyToManyField("experiences.Perk")

    category = models.ForeignKey(
        "categories.Category",
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    """
    What is included on ac Experience

    Args:
        CommonModel (_type_): _description_
    """

    name = models.CharField(
        _("Name"),
        max_length=100,
    )
    details = models.CharField(
        _("Details"),
        max_length=250,
        null=True,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        _("Explanation"),
        null=True,
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name
