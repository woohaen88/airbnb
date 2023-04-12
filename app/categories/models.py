from django.db import models
from common.models import CommonModel
from django.utils.translation import gettext_lazy as _


class Category(CommonModel):
    """
    Category

    Args:
        required:
            name: str
            kind: choice[rooms, experiences]
    """

    class CategoryKindChoices(models.TextChoices):
        EXPERIENCES = "experiences", "Experiences"
        ROOMS = "rooms", "Rooms"

    name = models.CharField(_("Name"), max_length=50)
    kind = models.CharField(
        _("Kind"),
        max_length=15,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self):
        return f"{self.kind}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
