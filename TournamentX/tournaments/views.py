from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import UserForm, TournamentForm, TeamForm, MatchForm
from .models import User, Tournament, Team, Match


# Create your views here.

def get_users(request):
    users = User.objects.all()
    return render(request=request, template_name='users.html',context=dict(users=users))

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('get_users')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

        
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

def add_team_member(request, team_id, user_id):
    team = Team.objects.get(id=team_id)
    user = User.objects.get(id=user_id)
    team.members.add(user)
    return redirect('get_team', team_id=team_id)

def add_tournament_participant(request, tournament_id, team_id):
    tournament = Tournament.objects.get(id=tournament_id)
    team = Team.objects.get(id=team_id)
    tournament.participants.add(team)
    return redirect('get_tournament', tournament_id=tournament_id)

def get_tournaments(request):
    tournaments = Tournament.objects.all()
    return render(request=request, template_name='tournaments.html', context=dict(tournaments=tournaments))

def get_teams(request):
    teams = Team.objects.all()
    return render(request=request, template_name='teams.html', context=dict(teams=teams))

def get_team_members(request, team_id):
    team = Team.objects.get(id=team_id)
    members = team.members.all()
    return render(request=request, template_name='teams.html', context=dict(team=team, members=members))

def get_tournament_participants(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    participants = tournament.participants.all()
    return render(request=request, template_name='tournament_participants.html', context=dict(tournament=tournament, participants=participants))

def get_team(request, team_id):
    team = Team.objects.get(id=team_id)
    return render(request=request, template_name='team.html', context=dict(team=team))

def get_tournament(request, tournament_id): 
    tournament = Tournament.objects.get(id=tournament_id)
    return render(request=request, template_name='tournament.html', context=dict(tournament=tournament))

def home(request):
    return HttpResponse("""<h1>Вітаємо на головній сторінці TournamentX!</h1>                
                        <p><a href="/users/">Користувачі</a></p>
                        <p><a href="/users/create/">Створити користувача</a></p>
                        <p><a href="/tournaments/">Турніри</a></p>
                        <p><a href="/teams/">Команди</a></p>
                        <p><a href="/match/create/">Створити матч</a></p>
                        <p><a href="/matches/">Переглянути матчі</a></p>
                        <p><a href="/admin/">Адмін-панель</a></p>
                        <p><a href="/tournaments/create/">Створити турнір</a></p>
                        <p><a href="/teams/create/">Створити команду</a></p
                        """)

def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = Match.objects.create(
                tournament=form.cleaned_data['tournament'],
                team1=form.cleaned_data['team1'],
                team2=form.cleaned_data['team2'],
                score1=form.cleaned_data['score1'],
                score2=form.cleaned_data['score2'],
                match_date=form.cleaned_data['match_date']
            )
            return redirect('create_match')
    else:
        form = MatchForm()
    
    return render(request, 'match.html', {'form': form})
        
def list_matches(request):
    matches = Match.objects.all()
    return render(request, 'matches.html', {'matches': matches}) 

def get_matches(request):
    matches = Match.objects.all()
    return render(request=request, template_name='matches.html', context=dict(matches=matches))

