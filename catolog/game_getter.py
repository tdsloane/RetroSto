from igdb.wrapper import IGDBWrapper
import json
import requests


global exp_time

def generate_token(exp_time):
    # Create global element to track token lifespan
    
    # Generate the access token if it does not exist.
    if exp_time <=1 or type(exp_time) != int:
        # Grab the OAuth binary and convert to json
        token_gen = requests.post("https://id.twitch.tv/oauth2/token?client_id=q6fao4mb1sojmg7bufkm5zjowskrq4&client_secret=ak6ruiye2hh7bgun4g12rwj3v0maul&grant_type=client_credentials")  
        token_json = token_gen.json()

        # separate the token and expiration time of the token.
        global token
        
        token = token_json['access_token']
        exp_time = token_json['expires_in']
        return token, exp_time
    else:
        pass


# Create a search
def search_query(user_input, exp_time):

    # Generate token if needed
    generate_token(exp_time)

    #establish client_id for wrapper
    client_id = "q6fao4mb1sojmg7bufkm5zjowskrq4"
    wrapper = IGDBWrapper(client_id, token)

    # Query the API based on a search term.
    query = wrapper.api_request(
                'games', # Requesting the name, storyline, genre name, and cover art url where the user input is the search tearm
                f'fields name, storyline, genres.slug, cover.url; offset 0; where name="{user_input}"*; sort first_release_date; limit: 100;',
                            # Also sorted by release date with a limit of 100 results
                )
    # Load the binary data into json
    message_json = json.loads(query)
    
    # List of all games returned
    global all_games
    all_games = dict()
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
            pass
        # Group together by game
        if game.get('cover') != None:
            result = [name,cover_url.get('url'),storyline,summary,genre_list]
            # Add the game to the collection of all games found
            all_games[key] = result
            key += 1
        else: 
            result = [name,storyline,summary,genre_list]
            # Add the game to the collection of all games found
            all_games[key] = result
            key += 1

    return str(all_games)
