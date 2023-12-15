from django.db import models
from django.contrib.auth import get_user_model
from core.models import DateModel

User = get_user_model()


class Team(DateModel):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='teams/logo/', blank=True, null=True)

    def __str__(self):
        return self.name


class Player(DateModel):
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name} ({self.team.name})"


class FantasyTeam(DateModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, related_name='fantasyteam', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    players = models.ManyToManyField(Player, blank=True)

    def __self__(self):
        return f"{self.name} - {self.user.full_name}"

class Match(DateModel):
    home_team = models.ForeignKey(Team, related_name='home_team', on_delete=models.DO_NOTHING)
    away_team = models.ForeignKey(Team, related_name='away_team', on_delete=models.DO_NOTHING)
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)
    scorers = models.ManyToManyField(Player, related_name='scorers')
    assists = models.ManyToManyField(Player, related_name='assists')


    def __str__(self):
        return f"{self.home_team} {self.home_team_score} - {self.away_team_score} {self.away_team}"


class MatchScore(DateModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


    def __str__(self):
        return f"Match: {self.match.pk} Player: {self.player} Score: {self.score}"
