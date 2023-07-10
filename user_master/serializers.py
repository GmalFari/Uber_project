from rest_framework import serializers
from .models import *


class MyCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class MyStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class MyCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
