from rest_framework import serializers
from .models import *


class MyDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'


class DriverleaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driverleave
        fields='__all__'