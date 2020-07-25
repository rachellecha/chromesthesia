import os
import sys
import spotipy 
import webbrowser
import json
import spotipy.util as util
from json.decoder import JSONDecodeError

# get username from terminal
username = sys.argv[1]

#12171678313

#Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(".cache-{}".format(username))
    token = util.prompt_for_user_token(username)

#create spotify object
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
displayName = user["display_name"]

while True:

    print()
    print("Welcome to Chromesthesia " + displayName)
    print()
    print("0 - Search for Song")
    print("1 - exit")
    print()
    choice = input("Your choice ")

#Search for song
    if choice == "0":
        print()
        searchQuery = input("What's the song: ")
        print()

        song = spotifyObject.search(searchQuery, 1, 0, "track")

        artist = song["tracks"]["items"][0]["artists"][0]["name"]

        searchResults = spotifyObject.search(artist, 1, 0, "artist")

        genre = searchResults["artists"]["items"][0]["genres"]

        #print(type(genre))

        print(genre)

        #print(json.dumps(searchResults, sort_keys = True, indent=4))
        
        if "indie pop" in genre:
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



#end program
    if choice == "1":
        break

# print(json.dumps(VARIABLE, sort_keys = True, indent=4))

