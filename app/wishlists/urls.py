from django.urls import path
from wishlists import views

# /api/v1/wishlist

wishList = views.WishlistsViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

wishListDetail = views.WishlistsViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

wishListToggle = views.WishListToggle.as_view(
    {
        "put": "update",
    }
)

urlpatterns = [
    path("", wishList),
    path("<int:wishlist_id>/", wishListDetail),
    path("<int:wishlist_id>/room/<int:room_id>/", wishListToggle),
]
