import webbrowser

class Movie():		
	def __init__(self, movie_title,director, movie_storyline, poster_image, trailer_youtube):		
	#Instance variable to store all propiertes about the movie
		self.title = movie_title
		self.director = director		
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	#Instance method to open the trailer on youtube
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)