from django.urls import path
from rooms import views


amenities = views.AmenityView.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
amenity_detail = views.AmenityView.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

rooms = views.RoomView.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

room_detail = views.RoomView.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("", rooms),
    path("<int:room_id>/", room_detail),
    path("amenity/", amenities),
    path("amenity/<int:amenity_id>/", amenity_detail),
]
