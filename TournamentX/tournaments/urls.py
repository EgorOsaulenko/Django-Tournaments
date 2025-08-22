from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', views.get_users, name="get_users" ),
    path('users/create/', views.create_user, name="create_user"),
    path('tournaments/create/', views.create_tournament, name="create_tournament"),
    path('teams/create/', views.create_team, name="create_team"),
    path('tournaments/', views.get_tournaments, name="get_tournaments"),
    path('teams/', views.get_teams, name="get_teams"),
    path('teams/<int:team_id>/', views.get_team, name="get_team"), 
    path('match/create/', views.create_match, name='create_match'),
    path('matches/', views.list_matches, name='list_matches'),
]