from django.db import models
# from .views import group_games
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    pass
    # for game in group_games.values():
    #     collector = models.ForeignKey(User, on_delete=models.CASCADE)
    #     for i in game.values():
    #         name = models.CharField(max_length=50)
    #         cover = models.URLField()
    #         storyline = models.TextField(max_length=500)
    #         summary = models.TextField(max_length=500)
    #         genre_set = models.CharField(max_length=50)

        
    
# def save(self, *args, **kwargs):
#     super(Profile, self).save(*args, **kwargs)    
class UserSearch():
    pass