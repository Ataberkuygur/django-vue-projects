from rest_framework import serializers
from Category.serializers import CategorySerializer
from Day.serializers import DaySerializer
from Auth.serializers import UserSerializer
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)
    class Meta:
        model = Habit
        fields = ['id', 'title', 'description', 'category', 'success_rate', 'daily_goal', 'days', 'user', 'start_date', 'end_date', 'slug']
        read_only_fields = ['id', 'success_rate', 'days', 'user', 'start_date', 'slug']