import requests

from django.conf import settings

from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model,
)

from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from users.serializers import (
    AuthSerializer,
    AuthChangePasswordSerializer,
    UserCreationSerializer,
    UserMeSerializer,
    GithubLoginSerializer,
)


class AuthView(ModelViewSet):
    serializer_class = AuthSerializer

    def get_serializer_class(self):
        if self.action == "update":
            return AuthChangePasswordSerializer
        # if self.action == "delete":
        #     return None
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create()

        headers = self.get_success_headers(serializer.data)

        msg = {"message": "로그인 성공!"}
        return Response(msg, status=status.HTTP_200_OK, headers=headers)

    def perform_create(self):
        email = self.request.data.get("email")
        user = get_user_model().objects.get(email=email)

        login(
            self.request,
            user,
        )

    @permission_classes([IsAuthenticated])
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        serializer = self.get_serializer(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update()

        msg = {"message": "password change ok!"}
        return Response(msg, status=status.HTTP_200_OK)

    def perform_update(self):
        user = self.request.user
        old_password = self.request.data.get("password", None)
        new_password = self.request.data.get("new_password", None)

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        logout(request)
        msg = {"message": "logout"}
        return Response(msg, status=status.HTTP_200_OK)


class UserCreationView(ModelViewSet):
    serializer_class = UserCreationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        email = self.request.data.get("email")
        password1 = self.request.data.get("password1")
        get_user_model().objects.create_user(email=email, password=password1)


class UserMeView(ModelViewSet):
    serializer_class = UserMeSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        instance = get_user_model().objects.get(id=user.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


#########################################################################################################
##                                     Social Login                                                    ##
#########################################################################################################


class GithubLogIn(ModelViewSet):
    serializer_class = GithubLoginSerializer

    def create(self, request, *args, **kwargs):
        code = request.data.get("code")
        client_id = "e41e6d6c2f43e39f3a7c"
        GH_SECRET = settings.GH_SECRET
        access_token_set = requests.post(
            f"https://github.com/login/oauth/access_token?code={code}&client_id={client_id}&client_secret={GH_SECRET}",
            headers={"Accept": "application/json"},
        )
        access_token = access_token_set.json().get("access_token")
        user_data_set = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        )

        user_data = user_data_set.json()

        user_email_set = requests.get(
            "https://api.github.com/user/emails",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        )

        user_emails = user_email_set.json()

        try:
            user = get_user_model().objects.get(email=user_emails[0]["email"])
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        except get_user_model().DoesNotExist:  # Github로 계정을 만듬
            user = get_user_model().objects.create(
                email=user_emails[0]["email"],
                username=user_data.get("login"),
                avatar=user_data.get("avatar_url"),
            )
            user.set_unusable_password()  # 이유저는 password로 로그인 할수 없음
            user.save()
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        # except Exception:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)


class KakaoLogIn(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                "https://kauth.kakao.com/oauth/token",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                data={
                    "grant_type": "authorization_code",
                    "client_id": "c65ba131d4497c8389e078cfbe59469e",
                    "redirect_uri": "http://localhost:3000/social/kakao",
                    "code": code,
                },
            )
            print("access_token/: ", access_token.json())

            access_token = access_token.json().get("access_token")
            user_data = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
                },
            )
            user_data = user_data.json()
            print("user_data: ", user_data)
            kakao_account = user_data.get("kakao_account")
            profile = kakao_account.get("profile")
            nickname = profile.get("nickname")
            thumbnail_image_url = profile.get("thumbnail_image_url")

            try:
                user = get_user_model().objects.get(email=kakao_account["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except get_user_model().DoesNotExist:
                user = get_user_model().objects.create(
                    email=kakao_account["email"],
                    avatar=thumbnail_image_url,
                    username=nickname,
                )
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
