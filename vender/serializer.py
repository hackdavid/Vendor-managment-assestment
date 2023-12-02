from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers

from vender.models import (
    VenderProfile,
)

class VenderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderProfile
        fields = ['id', 'name', 'contact', 'details', 'address', 'vender_code']