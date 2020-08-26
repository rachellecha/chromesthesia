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
from sklearn.tree import DecisionTreeClassifier, export_graphviz, export_text
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
    
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

#import csv with the color/song data
df = pd.read_csv("chromesthesia.csv")


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
print("Accuracy:", accuracy_score(y_test, y_pred))
#r = export_text(clf, feature_names=cols)
#print(r)

#Search for song
input = input("Song Name? ")

song = spotifyObject.search(input, 1, 0, "track")

#print(json.dumps(song, sort_keys = True, indent=4))

trackURI = song["tracks"]["items"][0]["uri"]

searchResults = spotifyObject.audio_features(trackURI)

ans = clf.predict([[searchResults[0]["acousticness"],searchResults[0]["danceability"],searchResults[0]["energy"],searchResults[0]["instrumentalness"],searchResults[0]["liveness"],searchResults[0]["loudness"], searchResults[0]["speechiness"],searchResults[0]["tempo"]]])

color = ans[0]

print(color)

 