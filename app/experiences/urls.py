from django.urls import path
from experiences import views


perks = views.PerksViewset.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

perk_detail = views.PerksViewset.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("perk/", perks),
    path("perk/<int:perk_id>/", perk_detail),
]
