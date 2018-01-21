import fresh_tomatoes
import media

#List of my favourites movies

titanic = media.Movie("Titanic",
						"James Cameron",
						"Titanic is a 1997 American epic romance-disaster film directed, written, co-produced and co-edited by James Cameron.",
						"https://en.wikipedia.org/wiki/Titanic_(1997_film)#/media/File:Titanic_poster.jpg",
						"https://www.youtube.com/watch?v=zCy5WQ9S4c0&t=3s")

gladiator = media.Movie("Glatiator",
						"Ridley Scott",
						"Crowe portrays Hispano-Roman general Maximus Decimus Meridius, who is betrayed when Commodus, the ambitious son of Emperor Marcus Aurelius, murders his father and seizes the throne.",
						"https://en.wikipedia.org/wiki/Gladiator_(2000_film)#/media/File:Gladiator_ver1.jpg",
						"https://www.youtube.com/watch?v=owK1qxDselE")

the_notebook = media.Movie("The Notebook",
						"Nick Cassavetes",
						"The Notebook is a 2004 American romantic drama film directed by Nick Cassavetes and based on the 1996 novel of the same name by Nicholas Sparks.",
						"https://en.wikipedia.org/wiki/The_Notebook#/media/File:Posternotebook.jpg",
						"https://www.youtube.com/watch?v=FC6biTjEyZw")

king_kong = media.Movie("King Kong",
						"Peter Jackson",
						"King Kong is a 2005 epic monster adventure film co-written, produced, and directed by Peter Jackson. A remake of the 1933 film of the same name, the film stars Naomi Watts, Jack Black, Adrien Brody, and, through motion capture, Andy Serkis as the title character.",
						"https://en.wikipedia.org/wiki/King_Kong_(2005_film)#/media/File:Kingkong_bigfinal1.jpg",
						"https://www.youtube.com/watch?v=AYaTCPbYGdk")

casino_royale = media.Movie("Casino Royale",
						"Martin Campbell",
						"Casino Royale (2006) is the twenty-first spy film in the Eon Productions James Bond film series, and is the third screen adaptation of Ian Fleming's 1953 novel of the same name.",
						"https://en.wikipedia.org/wiki/Casino_Royale_(2006_film)#/media/File:Casino_Royale_2_-_UK_cinema_poster.jpg",
						"https://www.youtube.com/watch?v=36mnx8dBbGE")


braveheart = media.Movie("Braveheart",
						"Mel Gibson",
						"Braveheart is a 1995 American epic war film directed by Mel Gibson, who stars as William Wallace, a late 13th-century Scottish warrior who led the Scots in the First War of Scottish Independence against King Edward I of England. ",
						"https://en.wikipedia.org/wiki/Braveheart#/media/File:Braveheart_imp.jpg",
						"https://www.youtube.com/watch?v=1cnoM8EiGGU")

#Storing all movie in an array
movies = [titanic, gladiator, the_notebook, king_kong, casino_royale, braveheart]

#Sending an array to list
fresh_tomatoes.open_movies_page(movies)
