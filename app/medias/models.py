from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    """
    Photo

    Args:
        required:
            file: url
        optional:
            description: str
        relation:
            room: "rooms.Room"
            experience: "experiences.Experience"

    """

    file = models.URLField(_("File"), max_length=255)
    description = models.CharField(
        _("Description"),
        max_length=150,
        blank=True,
        null=True,
    )
    room = models.ForeignKey(
        "rooms.Room",
        verbose_name=_("Room"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name=_("Experience"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )


class Video(CommonModel):
    """
    Video

    Args:
        required:
            file: url
        relation:
           experience: "experiences.Experience"
    """

    file = models.URLField(_("File"), max_length=255)
    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name=_("Experience"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
