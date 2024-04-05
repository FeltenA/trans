from rest_framework import serializers
from .models import User, Score, Match, Tournament

class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['nickname', 'name', 'password']

class ScoreSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()
    player = serializers.PrimaryKeyRelatedField(
        many=False, 
        read_only=False,
        queryset=User.objects.all()
    )

    class Meta:
        model = Score
        fields = ['player', 'score']

class MatchSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)
    player_nbr = serializers.IntegerField(default=2, required=False)
    winner = serializers.PrimaryKeyRelatedField(
        many=False, 
        read_only=False,
        queryset=User.objects.all()
    )
    tournament = serializers.PrimaryKeyRelatedField(
        many=False, 
        read_only=False,
        queryset=Tournament.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Match
        fields = ['winner', 'tournament', 'player_nbr', 'scores']
    
    def validate_player_nbr(self, data):
        if (data < 2):
            raise serializers.ValidationError({"player_nbr": "player number must be higher than 2"})
        return (data)
    
    def validate(self, data):
        scores = data['scores']
        if (len(scores) != data['player_nbr']):
            raise serializers.ValidationError({"scores": "there must be as much scores as players"})
        return (data)
    
    def create(self, validated_data):
        scores = validated_data.pop('scores')
        match_instance = Match.objects.create(**validated_data)
        for score in scores:
            Score.objects.create(match=match_instance,**score)
        return match_instance


class TournamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    players = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=False,
        queryset=User.objects.all()
    )

    class Meta:
        model = Tournament
        fields = ['name', 'players']