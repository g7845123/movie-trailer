class Movie():
    """ 
    This class provides a way to store movie related information
    
    Attributes:
        title: String. The title of the movie
        poster_image_url: String. Url of the poster image
        trailer_youtube_url: String. Url of the movie trailer
        imdb_rating: Number. Movie rating on IMDb.com
    """

    def __init__(self, movie_title, poster_image, trailer_youtube, imdb_rating):
        """ Inits Movie with basic information """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_rating = imdb_rating

    def show_tailer(self):
        """ Open movie trailer webpage (fresh_tomatoes.html) with web brower """ 
        webbrowser.open(self.trailer_youtube)

