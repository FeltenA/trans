from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<slug:pk>/', views.user_detail, name='user_detail'),
    path('matchs/', views.match_list, name='match_list'),
    path('matchs/<int:pk>/', views.match_detail, name='match_detail'),
    path('tournaments/', views.tournament_list, name='tournament_list'),
    path('tournaments/<int:pk>/', views.tournament_detail, name='tournament_detail'),
]
