from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import AppUser


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AppUser
        fields = ("email",)


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ("email",)
