from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.contrib.auth.models import User
from vender.models import (
    VenderProfile,
    PurchaseOrder,
    HistoricalPerformance
)

class VenderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenderProfile
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']