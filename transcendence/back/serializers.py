from rest_framework import serializers
from .models import User, Score, Match

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    player = serializers.CharField(max_length=30)
    score = serializers.IntegerField()
    match = serializers.IntegerField()

    class Meta:
        model = Score
        fields = ['player', 'score', 'match']

class MatchSerializer(serializers.ModelSerializer):
    winner = serializers.CharField(max_length=30)
    tournament = serializers.IntegerField(required=False, allow_null=True)
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Match
        fields = ['winner', 'tournament', 'scores']