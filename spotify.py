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
print(json.dumps(user, sort_keys = True, indent=4))

dispayName = user["display_name"]



# print(json.dumps(VARIABLE, sort_keys = True, indent=4))

