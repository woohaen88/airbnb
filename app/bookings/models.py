from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from common.models import CommonModel


class Booking(CommonModel):
    """Booking

    Args:
        required:
            kind: ["room", "experience"]
            guests: int
        optional:
            check_in: date
            check_out: date
            experience_time: datetime

        relation:
            [FK] user: settings.AUTH_USER_MODEL
            [FK] room: "room.Room"
            [FK] experience: "experiences.Experience"
    """

    class BookingKindChoices(models.TextChoices):
        ROOM = "room", _("ROOM")
        EXPERIENCE = "experience", _("Experience")

    kind = models.CharField(
        _("Kind"),
        max_length=15,
        choices=BookingKindChoices.choices,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    room = models.ForeignKey(
        "rooms.Room",
        verbose_name=_("Room"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        verbose_name=_("Experience"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    check_in = models.DateField(
        _("Check In"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        _("Check Out"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
    )

    experience_time = models.DateTimeField(
        _("Experience Time"),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True,
    )

    guests = models.PositiveIntegerField(_("Guests"))

    def __str__(self) -> str:
        return f"{self.kind.title()} / {self.user}"
