from flask import Flask, redirect, url_for, render_template, request, flash
import os
import sys
import spotipy 
import webbrowser
import json
import spotipy.util as util
from json.decoder import JSONDecodeError
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

app = Flask(__name__)

#main home page

@app.route("/")
def home():
    return render_template("index.html")


#result page

@app.route("/hi")
def hi():

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


    #connect google sheets and add the spotify data to it

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    c = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    gc = gspread.authorize(c)

    sh = gc.open("Chromesthesia").sheet1

    songsCol = sh.col_values(2)
    colorsCol = sh.col_values(15)

    df = pd.DataFrame(sh.get_all_records())

    df = df[["Song", "Color"]]

    cols = ["acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "tempo"]

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []

    for index, row in df.iterrows():
        song = spotifyObject.search(row["Song"], 1, 0, "track")
        trackURI = song["tracks"]["items"][0]["uri"]
        searchResults = spotifyObject.audio_features(trackURI)
        l1.append(searchResults[0]["acousticness"])
        l2.append(searchResults[0]["danceability"])
        l3.append(searchResults[0]["energy"])
        l4.append(searchResults[0]["instrumentalness"])
        l5.append(searchResults[0]["liveness"])
        l6.append(searchResults[0]["loudness"])
        l7.append(searchResults[0]["speechiness"])
        l8.append(searchResults[0]["tempo"])

    df = df.assign(acousticness = l1 , danceability = l2, energy = l3, instrumentalness = l4, liveness = l5, loudness = l6, speechiness = l7, tempo = l8)


    #create the Decision Tree Classifier
    cols = ["acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "tempo"]

    X = df[cols] #features

    y = df["Color"] #target/outcome

    #90/10 split because I have very little data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    clf = DecisionTreeClassifier()

    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    #check accuracy and print out decision tree
    #print("Accuracy:", accuracy_score(y_test, y_pred))
    #r = export_text(clf, feature_names=cols)
    #print(r)

    #Search for song
    input = request.args["color"]

    song = spotifyObject.search(input, 1, 0, "track")

    #print(json.dumps(song, sort_keys = True, indent=4))

    trackURI = song["tracks"]["items"][0]["uri"]

    searchResults = spotifyObject.audio_features(trackURI)

    ans = clf.predict([[searchResults[0]["acousticness"],searchResults[0]["danceability"],searchResults[0]["energy"],searchResults[0]["instrumentalness"],searchResults[0]["liveness"],searchResults[0]["loudness"], searchResults[0]["speechiness"],searchResults[0]["tempo"]]])

    color = ans[0]
    
    #returns the result in a new page or sends them to error page
    try:    
        return render_template("hi.html", color=color)
    except Exception as e:
        return render_template("error.html", error = str(e))

if __name__ == "__main__":
    app.run(debug = True)

