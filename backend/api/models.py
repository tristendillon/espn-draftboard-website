from django.db import models

# Create your models here.

class Draft(models.Model):
    teams = models.IntegerField(null=False,)
    roster_spots = models.IntegerField(null=False,)
    name = models.CharField(null=False, max_length=200)
    minutes = models.IntegerField(),
    seconds = models.IntegerField(),
    
class Team(models.Model):
    name = models.CharField(null=False, max_length=200)
    draft_id = models.ForeignKey(to=Draft, null=False, on_delete=models.CASCADE)
    team_image = models.ImageField(null=True,)

class Pick(models.Model):
    name = models.CharField(null=False, max_length=200)
    icon = models.ImageField(null=True,)
    football_team = models.TextField(null=True, max_length=50,)
    pick_round = models.IntegerField(null=False,)
    pick_round = models.IntegerField(null=False,)
    position = models.CharField(null=False, max_length=10,)
    draft_id = models.ForeignKey(to=Draft, null=False, on_delete=models.CASCADE)