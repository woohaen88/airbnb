from django.urls import path
from users import views

userLogin = views.AuthView.as_view(
    {
        "post": "create",
    }
)

userChangePassword = views.AuthView.as_view(
    {
        "put": "update",
    }
)

userLogout = views.AuthView.as_view(
    {
        "delete": "destroy",
    }
)

userCreate = views.UserCreationView.as_view(
    {
        "post": "create",
    }
)

urlpatterns = [
    path("user-login/", userLogin),
    path("user-changepw/", userChangePassword),
    path("logout/", userLogout),
    path("user-create/", userCreate),
]
