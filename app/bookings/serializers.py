from datetime import date
from django.utils import timezone

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

class CreateBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    def get_now_date(self) -> date:
        return timezone.localtime(timezone.now()).date() 

    class Meta:
        model = Booking
        fields = [            
            "guests",
            "check_in",
            "check_out",            
        ]    

    def validate_check_in(self, check_in):
        now = self.get_now_date()
        if now > check_in:
            raise serializers.ValidationError("Can't book in the past!")

        return check_in
    
    def validate_check_out(self, check_out):
        now = self.get_now_date()
        if now > check_out:
            raise serializers.ValidationError("Can't book in the past!")

        return check_out
    
    def validate(self, attrs):
        # checkin < checkout
        if attrs["check_in"] > attrs["check_out"]:
            raise serializers.ValidationError("체크아웃 날짜가 체크인 날짜보다 큽니다.")
        
        if Booking.objects.filter(check_in__lte=attrs["check_out"], check_out__gte=attrs["check_in"]):
            raise serializers.ValidationError("이미 예약된 방이 존재합니다.")
        return attrs