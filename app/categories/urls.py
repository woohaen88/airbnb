from django.urls import path
from categories import views

urlpatterns = [
    path(
        "",
        views.CategoryView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:category_id>/",
        views.CategoryView.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
