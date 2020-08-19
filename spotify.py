import os
import sys
import spotipy 
import webbrowser
import json
import spotipy.util as util
from json.decoder import JSONDecodeError
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# get username from terminal
username = "12171678313"

#12171678313

#Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    #os.remove(".cache-{}".format(username))
    token = token = util.prompt_for_user_token(username, client_id='f572cf52d72b4e44ac55d6c14ba6f74a', client_secret='18f76a14e1554ad69b2d51070a9a67eb', redirect_uri='https://google.com/')

#create spotify object
spotifyObject = spotipy.Spotify(auth=token)

#user = spotifyObject.current_user()
#displayName = user["display_name"]

#connect google sheets

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

c = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

gc = gspread.authorize(c)

sh = gc.open("Chromesthesia").sheet1

songsCol = sh.col_values(2)
colorsCol = sh.col_values(15)

print(colorsCol)

#print(sh.get_all_records())

#Search for song
input = input("Song Name? ")

song = spotifyObject.search(input, 1, 0, "track")

#print(json.dumps(song, sort_keys = True, indent=4))

trackURI = song["tracks"]["items"][0]["uri"]

searchResults = spotifyObject.audio_features(trackURI)

#genre = searchResults["artists"]["items"][0]["genres"]

#print(type(genre))

#print(genre)

print(json.dumps(searchResults, sort_keys = True, indent=4))

#if any("indie" in genre for genre in genre):
    #print("yellow")

#if "pop" in genre:
    #print("pink")
        
#if "folk" in genre:
    #print("yellow")

#if "rap" in genre:
    #print("black")

#if "alternative r&b" in genre:
    #print("pink")
        
#if "pop punk" in genre:
    #print("blue")



# print(json.dumps(VARIABLE, sort_keys = True, indent=4))


