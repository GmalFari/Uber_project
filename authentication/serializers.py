from rest_framework import serializers
from .models import Newuser

class NewuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newuser
        fields = "__all__"