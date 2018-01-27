import webbrowser


class Movie():
    """Class describing attributes an behavior of a Movie.

    Args:
        title           (str): Movie's title.
        director        (str): Movie's director.
        movie_storyline (str): Movie's storyline.
        poster_image    (str): Movie's film poster.
        trailer_youtube (str): Movie's trailer on youtube.

    Atributes:
        title           (str): Movie's title.
        director        (str): Movie's director.
        movie_storyline (str): Movie's storyline.
        poster_image    (str): Movie's film poster.
        trailer_youtube (str): Movie's trailer on youtube.

    Methods:
        show_trailer (self): Open default web browser 
    """
    def __init__(self, title, director, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = title
        self.director = director
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):        
        webbrowser.open(self.trailer_youtube_url)