from flask import Flask, redirect, url_for, render_template, request, flash
import os
import sys
import spotipy 
import webbrowser
import json
import spotipy.util as util
from json.decoder import JSONDecodeError

app = Flask(__name__)

#main home page

@app.route("/")
def home():
    return render_template("index.html")

#result page

@app.route("/result")
def result():

    # my Spotify username
    username = "12171678313"

    #get user permissions from Spotify 
    try:
        token = util.prompt_for_user_token(username)
    except:
        #os.remove(".cache-{}".format(username))
        token = token = util.prompt_for_user_token(username, client_id='f572cf52d72b4e44ac55d6c14ba6f74a', client_secret='18f76a14e1554ad69b2d51070a9a67eb', redirect_uri='https://google.com/')

    #create spotify object
    spotifyObject = spotipy.Spotify(auth=token)


    #Search for song

    #user input song into search bar
    input = request.args["song"]

    #uses Spotify API search function to get information about the track (song)
    song = spotifyObject.search(input, 1, 0, "track")

    #use this to get artist
    artist = song["tracks"]["items"][0]["artists"][0]["name"]

    searchResults = spotifyObject.search(artist, 1, 0, "artist")

    #I chose genre as the differentiator for songs to represent different colors.
    #then get genre from this because Spotify doesn't classify each song to have a specific genre
    genre = searchResults["artists"]["items"][0]["genres"]

    #takes the genre of the song and returns the color that song is. This will become more nuanced over time
    if any("indie" in genre for genre in genre):
        color = "yellow"

    if "pop" in genre:
        color = "pink"
        
    if any("folk" in genre for genre in genre):
        color = "yellow"

    if any("rap" in genre for genre in genre):
        color = "black"

    if any("r&b" in genre for genre in genre):
        color = "pink"
        
    if any("punk" in genre for genre in genre):
        color = "blue"
    
    #returns the result in a new page
    return render_template("result.html", color=color)


if __name__ == "__main__":
    app.run()

