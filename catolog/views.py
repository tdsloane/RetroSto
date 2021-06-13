from igdb.wrapper import IGDBWrapper
from catolog.models import Game
from django.shortcuts import render
from django.views.generic import ListView
import json
import requests

exp_time = False

# Create your views here.
def collection(request):
    context = {
        'games': Game.objects.all()
    }
    return render(request, 'catolog/collection.html', context)



def search(request):
    er = {
        'error': "The Search Did not function.",
        'error2': "Passed by First Section"
        }

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # user_input = SearchView(request.GET)
        # Generate token if needed
        if exp_time <=1 or exp_time == False:
            def generate_token(exp_time):

                # Grab the OAuth binary and convert to json
                token_gen = requests.post("https://id.twitch.tv/oauth2/token?client_id=q6fao4mb1sojmg7bufkm5zjowskrq4&client_secret=ak6ruiye2hh7bgun4g12rwj3v0maul&grant_type=client_credentials")  
                token_json = token_gen.json()

                # separate the token and expiration time of the token.
                global token
                
                token = token_json['access_token']
                exp_time = token_json['expires_in']
                return token, exp_time
            generate_token(exp_time)
        else:
            print("Failed Check 1")
            return render(request,"catolog/search_page.html", er)

        #establish client_id for wrapper
        client_id = "q6fao4mb1sojmg7bufkm5zjowskrq4"
        wrapper = IGDBWrapper(client_id, token)

        # Query the API based on a search term.
        query = wrapper.api_request(
                    'games', # Requesting the name, storyline, genre name, and cover art url where the user input is the search tearm
                    f'fields name, storyline, genres.slug, cover.url; offset 0; where name=*"{user_input}"*; sort first_release_date; limit: 100;',
                                # Also sorted by release date with a limit of 100 results
                    )
        # Load the binary data into json
        message_json = json.loads(query)
        print("json get!")
        # List of all games returned
        global group_games
        group_games = dict()
        key = 0

        # Grab each value by key and separate per game
        for game in message_json:
            name = game.get('name')
            cover_url = game.get('cover')
            storyline = game.get('storyline')
            summary = game.get('summary')
            genre_set = game.get('genres')
            # Genre posses none to many tags which needs to be sorted.
            genre_list = []
            if genre_set:
                for type in genre_set:
                    for i in type:
                        genre_list.append(type[i])
                        for i in genre_list:
                            genre_list = [x for x in genre_list if not isinstance(x, int)]
            else:
                print("Failed Genre Check")
                pass
            # Group together by game
            if game.get('cover') != None:
                result = {
                    'name': name,
                    'cover_url': cover_url.get('url'),
                    'storyline': storyline,
                    'summary': summary,
                    'genres': genre_list
                    }
                # Add the game to the collection of all games found
                group_games[key] = result
                key += 1
            else: 
                result = {
                    'name': name,
                    'storyline': storyline,
                    'summary': summary,
                    'genres': genre_list
                    }
                # Add the game to the collection of all games found
                group_games[key] = result
                key += 1

        
        return render(request, "catolog/search_page.html", {'group_games': group_games}) 
    else:
        print("Failed Check Two")
        er = {'error': "The Search Did not function."}
        return render(request,"catolog/search_page.html", er) 

    

class GameListView(ListView):
    model = Game
    template_name = 'catolog/collection.html'
    context_object_name = 'games'

class SearchView(ListView):
    model = Game
    template_name = 'catolog/search_page.html'
    context_object_name = 'user_input'
    
    
# class ImageViewer(group_games):
#     for i in group_games:
#         img = group_games[i].cover_url
