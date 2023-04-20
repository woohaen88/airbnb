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

userLogout = views.LogoutView.as_view(
    {
        "post": "create",
    }
)

userCreate = views.UserCreationView.as_view(
    {
        "post": "create",
    }
)

userMe = views.UserMeView.as_view(
    {
        "get": "retrieve",
    }
)

githubLogin = views.GithubLogIn.as_view(
    {
        "post": "create",
    }
)

urlpatterns = [
    path("user-login/", userLogin),
    path("user-changepw/", userChangePassword),
    path("logout/", userLogout),
    path("user-create/", userCreate),
    path("me/", userMe),
    path("github/", githubLogin),
]
