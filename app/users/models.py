from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if email is None:
            raise ValueError("email은 반드시 입력되어야 합니다.")

        username = email.split("@")[0]
        extra_fields["username"] = username

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User Model

    Required:
        email (emailType) : your email(ex. user@example.com)
        password (str) : your password

    Optional:
        username: (str)
        first_name: (str?)
        last_name: str?
        is_staff: bool, default: false
        is_staff: bool, default: true
        date_joined: datetime
        avatar: str(startswith__http://)
        is_host: bool, default: false
        gender: TextChoice?, "M", "F"
        language: TextChoice? "KR", "EN"
        currency: TextChoice? "WON", "USD



    """

    username = models.CharField(
        _("username"),
        max_length=150,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        _("last name"),
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    avatar = models.URLField(
        _("avatar"),
        blank=True,
        null=True,
    )

    class GenderChoice(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "FEMALE"

    gender = models.CharField(
        max_length=6,
        choices=GenderChoice.choices,
        blank=True,
        null=True,
    )

    class LanguageChoice(models.TextChoices):
        KR = "kr", _("Korean")
        EN = "en", _("English")

    language = models.CharField(
        max_length=2,
        choices=LanguageChoice.choices,
        blank=True,
        null=True,
    )

    class CurrencyChoice(models.TextChoices):
        WON = "won", _("Korean Won")
        USD = "usd", _("Dollar")

    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoice.choices,
        blank=True,
        null=True,
    )

    is_host = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
