from django.db import models
from catolog import game_getter
# Create your models here.

class Game(models.Model):
    url_clue = ["//images.igdb.com"]
    for game in game_getter.all_games:
        title = game_getter.all_games[game][0]
        if url_clue in game_getter.all_games[game][1]:
            cover_art = game_getter.all_games[game]
        else:
            pass
        if game_getter.all_games[game][2] == None:
            pass
        else:
            storyline = game_getter.all_games[game][2]
        if game_getter.all_games[game][3] == None:
            pass
        else:
            storyline = game_getter.all_games[game][3]
        genre_pac = game_getter.all_games[game][4]
        
    def __str__(self):
        return self.title

class UserSearch():
    user_input = str