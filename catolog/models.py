from django.db import models
from .views import group_games
# Create your models here.

class Game(models.Model):
    for game in group_games:
        name = game.name
# def save(self, *args, **kwargs):
#     super(Profile, self).save(*args, **kwargs)
    # name = models.CharField(max_length=50)
    # cover = models.URLField()
    # storyline = models.TextField(max_length=500)
    # summary = models.TextField(max_length=500)
    # genre_set = models.CharField(max_length=50)
    name = group_games
    
class UserSearch():
    user_input = str