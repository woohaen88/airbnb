from django.contrib import admin
from rooms.models import Room, Amenity


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "kind",
        "owner",
    ]

    list_filter = [
        "country",
        "city",
        "pet_friendly",
        "kind",
        "amenities",
    ]
