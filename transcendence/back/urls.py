from django.urls import path
from . import views

urlpatterns = [
    path('back/', views.back, name='back'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('matchs/<int:pk>/', views.match_detail, name='match_detail'),
    path('scores/', views.score_list, name='score_list'),
]
