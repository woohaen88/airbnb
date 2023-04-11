from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from common.models import CommonModel


class WishList(CommonModel):
    """WisthList

    Args:
        required:
            name: str
        relation:
            [MtoM] rooms : "rooms.Room"
            [MtoM] experiences : "experiences.Experience"
            [FK] user : settings.AUTH_USER_MODEL
    """

    name = models.CharField(
        _("Name"),
        max_length=150,
    )
    rooms = models.ManyToManyField(
        "rooms.Room",
        verbose_name=_("Rooms"),
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        verbose_name=_("Experience"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("USER"),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.name
