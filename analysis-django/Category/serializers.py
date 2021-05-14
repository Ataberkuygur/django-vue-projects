from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'daily_goal_type', 'user', 'create_date', 'update_date', 'slug']
        read_only_fields = ['id', 'user', 'create_date', 'update_date', 'slug']