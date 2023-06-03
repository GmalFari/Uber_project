from rest_framework import serializers
from .models import AddDriver


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'
