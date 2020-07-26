from flask import Flask, redirect, url_for, render_template, request, flash
import os
import sys
import spotipy 
import webbrowser
import json
import spotipy.util as util
from json.decoder import JSONDecodeError

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hi")
def hi():
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
    #def colorPicker(input):

    input = request.args["color"]

    song = spotifyObject.search(input, 1, 0, "track")

    artist = song["tracks"]["items"][0]["artists"][0]["name"]

    searchResults = spotifyObject.search(artist, 1, 0, "artist")

    genre = searchResults["artists"]["items"][0]["genres"]

    #print(type(genre))

    #print(genre)

    #print(json.dumps(searchResults, sort_keys = True, indent=4))

    if any("indie" in genre for genre in genre):
        color = "yellow"

    if "pop" in genre:
        color = "pink"
        
    if "folk" in genre:
        color = "yellow"

    if "rap" in genre:
        color = "black"

    if "alternative r&b" in genre:
        color = "pink"
        
    if "pop punk" in genre:
        color = "blue"

    #input = input("Song Name? ")

    #colorPicker(input)

    # print(json.dumps(VARIABLE, sort_keys = True, indent=4))

    return render_template("hi.html", color=color)


if __name__ == "__main__":
    app.run()

