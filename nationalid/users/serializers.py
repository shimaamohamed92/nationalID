from rest_framework.serializers import ModelSerializer
from .models import NationalId
from rest_framework import serializers


class NationalSerializer(ModelSerializer):
    country = serializers.CharField(read_only=True)
    gender = serializers.CharField(read_only=True)
    birth = serializers.CharField(read_only=True)

    class Meta:
        model = NationalId
        fields = ("nantional_id","birth", "country", "gender")


