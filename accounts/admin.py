from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AppUserChangeForm, AppUserCreationForm
from .models import AppUser


class AppUserAdmin(UserAdmin):
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
        "first_name",
        "last_name",
        "phone_number",
    )
    #  The fields below are available when a new user is being edited.
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "password",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    #  The fields below are available when a new user is being created.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "first_name", "last_name", "phone_number")
    ordering = ("email", "first_name", "last_name")


admin.site.register(AppUser, AppUserAdmin)
