from rest_framework import serializers
from bookings.models import Booking


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "id",
            # "kind",
            "guests",
            "check_in",
            "check_out",
            "experience_time",
            # "user",
            # "room",
            # "experience",
        ]
