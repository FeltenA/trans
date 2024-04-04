from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User, Match, Score
from .serializers import UserSerializer, MatchSerializer, ScoreSerializer

def back(request):
    return HttpResponse("Hello world!")

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)


@api_view(['GET', 'POST'])
def score_list(request):
    if request.method == 'GET':
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def match_detail(request, pk):
    try:
        match = Match.objects.get(pk=pk)
    except Match.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MatchSerializer(match)
        return Response(serializer.data)