from rest_framework import serializers

from . import models


class CategorieFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategorieFormation
        fields = "__all__"


class VideoFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoFormation
        fields = "__all__"
        # depth = 1
