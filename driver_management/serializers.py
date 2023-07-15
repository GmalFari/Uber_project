from rest_framework import serializers
from .models import *


class MyDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'



    
class DriverleaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driverleave
        fields=('drivername', 'reason', 'leave_from_date', 'leave_to_date', 'total_days_of_leave')
    
    def create(self, validated_data):
        start_date = validated_data.get('leave_from_date')
        end_date = validated_data.get('leave_to_date')
        total_days_of_leave = (end_date - start_date).days

        instance =Driverleave.objects.create(
            start_date=start_date,
            end_date=end_date,
            total_days_of_leave= total_days_of_leave
        )
        return instance





