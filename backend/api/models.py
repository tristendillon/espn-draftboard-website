from django.db import models

DEFAULT_PICK_ICON = 'https://a.espncdn.com/combiner/i?img=/games/lm-static/ffl/images/nomug.png&w=96&h=70&cb=1'
DEFAULT_TEAM_ICON = 'https://g.espncdn.com/lm-static/ffl/images/default_logos/20.svg'

class Draft(models.Model):
    id = models.CharField(primary_key=True, null=False, max_length=50)
    name = models.CharField(null=False, max_length=200)
    teams = models.IntegerField(null=False,)
    roster_spots = models.IntegerField(null=False,)

class Timer(models.Model):
    minutes = models.IntegerField(null=False, default=0)
    seconds = models.IntegerField(null=False, default=0)
    draft_id = models.OneToOneField(to=Draft, null=False, on_delete=models.CASCADE)


class Team(models.Model):
    name = models.CharField(null=False, max_length=200)
    draft_id = models.ForeignKey(to=Draft, null=False, on_delete=models.CASCADE)
    team_image = models.CharField(null=False, max_length=400, default=DEFAULT_TEAM_ICON)

class Pick(models.Model):
    name = models.CharField(null=False, max_length=200)
    icon = models.CharField(null=True, max_length=400, default=DEFAULT_PICK_ICON)
    football_team = models.TextField(null=True, max_length=50,)
    pick_round = models.IntegerField(null=False,)
    pick_number = models.IntegerField(null=False,)
    position = models.CharField(null=False, max_length=10,)
    draft_id = models.ForeignKey(to=Draft, null=False, on_delete=models.CASCADE)
