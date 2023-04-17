from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
    login,
    authenticate,
)

from users.models import User


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
        ]


class AuthSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "password",
        ]

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)

        user = authenticate(
            self.context["request"],
            username=email,
            password=password,
        )

        if user is None:
            raise serializers.ValidationError("Invalid Credentials!")

        return attrs


class AuthChangePasswordSerializer(AuthSerializer):
    new_password = serializers.CharField()

    class Meta(AuthSerializer.Meta):
        fields = [
            "email",
            "password",
            "new_password",
        ]

    def validate_new_password(self, new_password):
        if new_password is None:
            raise serializers.ValidationError("new password가 입력되지 않았습니다.")
        return new_password


class UserCreationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "password1",
            "password2",
        ]

    def validate(self, attrs):
        password1 = attrs.get("password1", None)
        password2 = attrs.get("password2", None)
        if password1 is None or password2 is None:
            raise serializers.ValidationError("password1 혹은 password2가 입력되지 않았음")

        if password1 != password2:
            raise serializers.ValidationError("password1과 password2가 다름")

        return attrs
