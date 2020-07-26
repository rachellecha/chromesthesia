import os
import sys
import spotipy 
import webbrowser
import json
import spotipy.util as util
from json.decoder import JSONDecodeError

# get username from terminal
username = "12171678313"

#12171678313

#Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(".cache-{}".format(username))
    token = util.prompt_for_user_token(username)

#create spotify object
spotifyObject = spotipy.Spotify(auth=token)

#user = spotifyObject.current_user()
#displayName = user["display_name"]

#Search for song
def colorPicker(input):

    song = spotifyObject.search(input, 1, 0, "track")

    artist = song["tracks"]["items"][0]["artists"][0]["name"]

    searchResults = spotifyObject.search(artist, 1, 0, "artist")

    genre = searchResults["artists"]["items"][0]["genres"]

        #print(type(genre))

        #print(genre)

        #print(json.dumps(searchResults, sort_keys = True, indent=4))

    if any("indie" in genre for genre in genre):
        print("yellow")

    if "pop" in genre:
        print("pink")
        
    if "folk" in genre:
        print("yellow")

    if "rap" in genre:
        print("black")

    if "alternative r&b" in genre:
        print("pink")
        
    if "pop punk" in genre:
        print("blue")

input = input("Song Name? ")

colorPicker(input)

# print(json.dumps(VARIABLE, sort_keys = True, indent=4))


