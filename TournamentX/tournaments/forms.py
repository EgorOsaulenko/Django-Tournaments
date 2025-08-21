from django import forms
from .models import User, Tournament, Team

class UserForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    bio = forms.CharField(
        label='Bio',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )


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
