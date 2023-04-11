from django.contrib import admin
from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # :
    #     required:
    #         kind: ["room", "experience"]
    #         guests: int
    #     optional:
    #         check_in: date
    #         check_out: date
    #         experience_time: datetime

    #     relation:
    #         [FK] user: settings.AUTH_USER_MODEL
    #         [FK] room: "room.Room"
    #         [FK] experience: "experiences.Experience"
    list_display = [
        "kind",
        "guests",
        "user",
        "room",
        "experience",
    ]

    list_filter = [
        "kind",
        "user",
        "room",
        "experience",
    ]
