import fresh_tomatoes
import media

# Create several instances of Movie class

dark_knight = media.Movie(
    "The Dark Knight", 
    "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", 
    "https://www.youtube.com/watch?v=EXeTwQWrcwY", 
    9.0
)

kingsman = media.Movie(
    "Kingsman", 
    "http://upload.wikimedia.org/wikipedia/en/8/8b/Kingsman_The_Secret_Service_poster.jpg", 
    "https://www.youtube.com/watch?v=kl8F-8tR8to", 
    8.1
)

toy_story = media.Movie(
    "Toy Story",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc", 
    8.3
)

avatar = media.Movie(
   "Avatar",
   "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
   "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 
   7.9
)

school_of_rock = media.Movie(
    "School of Rock",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc", 
    7.1
)

saving_christmas = media.Movie(
    "Saving Christmas", 
    "http://upload.wikimedia.org/wikipedia/en/9/92/Saving_Christmas_poster.jpg", 
    "https://www.youtube.com/watch?v=z5-yA66kaVc", 
    1.6
)

movies = [dark_knight, kingsman, toy_story, avatar, school_of_rock, saving_christmas]
# fresh_tomatoes.py first dynamically generates a webpage based on information in movies, then it will open that webpage in browser
fresh_tomatoes.open_movies_page(movies)
