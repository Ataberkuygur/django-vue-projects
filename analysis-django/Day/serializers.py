from rest_framework import serializers
from .models import Day

class DaySerializer(serializers.ModelSerializer):
    habit = serializers.StringRelatedField()
    class Meta:
        model = Day
        fields = ['id', 'day_number', 'habit', 'quantity', 'done', 'create_time', 'slug']
        read_only_fields = ['id', 'day_number', 'create_time', 'slug']