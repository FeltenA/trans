from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['nickname', 'name', 'password']