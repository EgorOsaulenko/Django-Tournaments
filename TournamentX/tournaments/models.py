from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.email})"


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    bio = models.TextField()
    playground = models.CharField(max_length=100)
    participants = models.ManyToManyField("User", related_name="tournaments")

    def __str__(self):
        return f"Турнір: {self.name} ({self.date})"


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField("User", related_name="teams")
    tournament = models.ForeignKey(
        "Tournament", on_delete=models.CASCADE, related_name="teams"
    )

    def __str__(self):
        return f"Команда: {self.name}"

class Match(models.Model):
    tournament = models.ForeignKey(
        "Tournament", on_delete=models.CASCADE, related_name="Tournament"
    )
    team1 = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="team1"
    )
    team2 = models.ForeignKey(
        "Team", on_delete=models.CASCADE, related_name="team2"
    )
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    match_date = models.DateTimeField()

    def __str__(self):
        return f"Матч: {self.team1.name} vs {self.team2.name} ({self.match_date})"
    
