from rest_framework import serializers
from .models import AddDriver


class MyDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'
