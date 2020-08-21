# chromesthesia

## Have you ever wondered what sounds look like? Chromesthesia takes your favorite songs and tells you what color it is!

## Inspiration
Chromesthesia or sound to color synesthesia is a relatively rare neurological synesthesia. The idea of watching music rather than listening to it sounded unique and made me (Rachelle) inquisitive about it. When I shared the idea with my teammate (Treasa) we instantly got on the same page and chose to create a website to give a normal person the experience of watching music rather than listening to it.

## What it does
The website Chromesthesia enables the user to search for a song and predicts the color associated with that song based on its genre just like how people with chromesthesia would see it. If you feel the color associated with the song didn’t seem connected you can take the short survey linked in the website so the changes can be made to the simulator.

## How I built it
We created the layout for our website on Figma and later hardcoded the website using HTML and CSS styles. We used Spotify’s API to link it with our code to make it our search engine to browse songs using Python. I then used sklearn and used the Decision Tree Classifier to run an algorithm based on the factors provided from Spotify's audio analysis. Later we flasked the Python code with the HTML/CSS website to make the website up and running.

## Challenges I ran into
Trying to get Spotify’s API as our search engine to browse songs was the most challenging part of our project. Once that was complete we were not sure on how compatible Python and HTML/CSS were and later came up with the idea of using Flask to combine the frontend and backend.

Right now, our website doesn't take into account all genres listed in Spotify so some songs will run into error messages.

## Accomplishments that I'm proud of
We are proud we were able to get this website up and running. We are happy we made this website with the future in mind so we can have a detailed idea of this synthesia.

## What I learned
I learned how to use the new library Spotipy to use the Spotify API in python. I also learned Flask to connect the HTML/CSS frontend to the Python backend.

## What's next for chromesthesia
Next steps are to create a form to collect more data and disperse it to the synesthetic community and create a more accurate ML algorithm.

# click here to test it out! https://chromesthesiaa.herokuapp.com/
