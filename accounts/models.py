import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from .user_manager import AppUserManager


class AppUser(AbstractUser):
    username = None
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(4)])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    objects = AppUserManager()

    def __str__(self):
        return f"{self.email}"
