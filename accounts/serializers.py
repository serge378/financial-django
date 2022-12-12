from rest_framework import serializers

from .models import AppUser


class RegisterRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("id", "email", "first_name", "last_name", "phone_number")
