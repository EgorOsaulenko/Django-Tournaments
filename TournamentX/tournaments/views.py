from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import UserForm, TournamentForm, TeamForm
from .models import User, Tournament, Team

# Create your views here.

def get_users(request):
    users = User.objects.all()
    return render(request=request, template_name='users.html',context=dict(users=users))

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            email=form.cleaned_data.get('email'),
            bio=form.cleaned_data.get('bio')
            team=form.cleaned_data.get('team')
   
            user = User(
                name=name,
                first_name=first_name,
                last_name=last_name,
                email=email,
                bio=bio
            )
            user.team.set(team)
            user.save()
            return redirect('get_users')
        
def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name'),
            date=form.cleaned_data.get('date'),
            playground=form.cleaned_data.get('playground'),
            bio=form.cleaned_data.get('bio')
            
            tournament = Tournament(
                name=name,
                date=date,
                playground=playground,
                bio=bio
            )
            tournament.save()
            return redirect('get_tournaments')
    
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name'),
            members=form.cleaned_data.get('members')
            
            team = Team(
                name=name
            )
            team.save()
            team.members.set(members)
            return redirect('get_teams')
    
def get_tournaments(request):
    tournaments = Tournament.objects.all()
    return render(request=request, template_name='tournaments.html', context=dict(tournaments=tournaments))

def get_teams(request):
    teams = Team.objects.all()
    return render(request=request, template_name='teams.html', context=dict(teams=teams))

def get_team_members(request, team_id):
    team = Team.objects.get(id=team_id)
    members = team.members.all()
    return render(request=request, template_name='team_members.html', context=dict(team=team, members=members))

def get_tournament_participants(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    participants = tournament.participants.all()
    return render(request=request, template_name='tournament_participants.html', context=dict(tournament=tournament, participants=participants))

def get_team(request, team_id):
    team = Team.objects.get(id=team_id)
    members = team.members.all()
    return render(request=request, template_name='team.html', context=dict(team=team, members=members))

def get_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    participants = tournament.participants.all()
    return render(request=request, template_name='tournament.html', context=dict(tournament=tournament, participants=participants))
