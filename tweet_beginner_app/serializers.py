from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = [
            'id', 
            'user', 
            'text', 
            'photo', 
            'created_at', 
            'updated_at',
            'temperature',
            'weather_description',
            'city',
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data) 