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

from users.serializers import (
    AuthSerializer,
    AuthChangePasswordSerializer,
    UserCreationSerializer,
    UserMeSerializer,
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
