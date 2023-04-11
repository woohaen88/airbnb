from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import CommonModel


class Review(CommonModel):
    """
    Review

    Args:
        required:
            payload: str
            rating: int
        relation:
            [FK] user: setting.AUTH_USER_MODEL
            [FK] room = "rooms.Room"
            [FK] experience = "experiences.Experience",
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    room = models.ForeignKey(
        "rooms.Room",
        verbose_name=_("room"),
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name=_("Experience"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    payload = models.TextField(_("Review"))
    rating = models.PositiveIntegerField(_("Rating"))

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"
