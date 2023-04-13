from django.urls import path
from medias import views


photos = views.PhotoViewset.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

urlpatterns = [
    path("", photos),
]
