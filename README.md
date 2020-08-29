# chromesthesia

## Have you ever wondered what sounds look like? Chromesthesia takes your favorite songs and tells you what color it is!

## Inspiration
Chromesthesia or sound to color synesthesia is a relatively rare neurological synesthesia. The idea of watching music rather than listening to it sounded unique and made me inquisitive about it. I chose to create a website to give a normal person the experience of hearing colors rather than listening to it.

## What it does
The website Chromesthesia enables the user to search for a song and predicts the color associated with that song based on a set of audio analysis features from the Spotify API such as tempo, danceability, acoustic ness, etc. Initial data on songs and their corresponding color was gather from synesthetes from various internet communities such as Reddit, TikTok, and Discord. I then used sklearn's Decision Tree Classifier as my machine learning algorithm. If you feel the color associated with the song didn't seem connected you can take the short survey linked in the website so I can make the model more accurate.

## How I built it
I created the layout for our website on Figma and later coded the website using HTML and CSS. I used Spotify's API and linked it with our code to make it our search engine to browse songs. To import the data, I used the Google Sheets API since all my information came from a Google Form. I then used sci-kit learn and used the Decision Tree Classifier to run an algorithm based on the factors provided by Spotify's audio analysis. I then used Flask to connect my front end and back end.

## Challenges I ran into
The most challenging part was figuring out how to implement machine learning. I decided on a Decision Tree Classifier because I didn't have enough data for any of the other algorithms.

## Accomplishments that I'm proud of
I am proud I was able to get the machine learning aspect of it to all click!

## What I learned
I learned how to use some new libraries and APIs such as spotipy (Spotify API), sci-kit learn, gspread (Google Sheets API). This was also my first time deploying a dynamic page and learned how to use Heroku.

## What's next for chromesthesia
Next steps are to collect more data and disperse it to the synesthetic community to create a more accurate ML algorithm. I would also like to create a better UX/UI experience by learning JavaScript!

# click here to test it out! https://chromesthesiaa.herokuapp.com/
