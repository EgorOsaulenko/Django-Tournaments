from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tournament, Team

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'password1', 'password2']


class TournamentForm(forms.Form):
    name = forms.CharField(
        label='Tournament Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    playground = forms.CharField(
        label='Playground',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    bio = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    
class TeamForm(forms.Form):
    name = forms.CharField(
        label='Team Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Members'
    )
    tournament = forms.ModelChoiceField(
        queryset=Tournament.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tournament'
    )

class MatchForm(forms.Form):
    tournament = forms.ModelChoiceField(
        queryset=Tournament.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tournament'
    )
    team1 = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Team 1'
    )
    team2 = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Team 2'
    )
    score1 = forms.IntegerField(
        label='Score Team 1',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0})
    )
    score2 = forms.IntegerField(
        label='Score Team 2',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0})
    )
    match_date = forms.DateTimeField(
        label='Match Date and Time',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )