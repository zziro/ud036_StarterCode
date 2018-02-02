import fresh_tomatoes
import media

# List of my favourites movies

titanic = media.Movie(
    "Titanic",
    "James Cameron",
    "Titanic is a 1997 American epic romance-disaster film directed, written,"
    "co-produced and co-edited by James Cameron.",
    "http://thesource.com/wp-content/uploads/2017/11/Titanic-to-Return-to-Theaters-for-20th-Anniversary.jpg",  # NOQA
    "https://www.youtube.com/watch?v=IVqpcSqokkw")

gladiator = media.Movie(
    "Glatiator",
    "Ridley Scott",
    "Crowe portrays Hispano-Roman general Maximus Decimus Meridius, who is"
    "betrayed when Commodus, the ambitious son of Emperor Marcus Aurelius, "
    "murders his father and seizes the throne.",
    "https://static0.srcdn.com/wp-content/uploads/2016/09/Russell-Crowe-is-Maximus-in-Gladiator.jpg",  # NOQA
    "https://www.youtube.com/watch?v=JENO6uClY2E")

the_notebook = media.Movie(
    "The Notebook",
    "Nick Cassavetes",
    "The Notebook is a 2004 American romantic drama film directed by Nick "
    "Cassavetes and based on the 1996 novel of the same name by Nicholas "
    "Sparks.",
    "http://www.movieroomreviews.com/sites/movieroomreviews.com/files/imagecache/full_size_image/photos/the-notebook-movie-picture-59.jpg",  # NOQA
    "https://www.youtube.com/watch?v=yDJIcYE32NU")

king_kong = media.Movie(
    "King Kong",
    "Peter Jackson",
    "King Kong is a 2005 epic monster adventure film co-written, produced, and"
    "directed by Peter Jackson. A remake of the 1933 film of the same name, "
    "the film stars Naomi Watts, Jack Black, Adrien Brody, and, through motion"
    "capture, Andy Serkis as the title character.",
    "https://vignette.wikia.nocookie.net/skull-island/images/8/89/King-Kong-Movie-Poster-1-.jpeg",  # NOQA
    "https://www.youtube.com/watch?v=44LdLqgOpjo")

casino_royale = media.Movie(
    "Casino Royale",
    "Martin Campbell",
    "Casino Royale (2006) is the twenty-first spy film in the Eon Productions "
    "James Bond film series, and is the third screen adaptation of Ian "
    "Fleming's 1953 novel of the same name.",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Casino_Royale_2_-_UK_cinema_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xK7PbujRUOk")

braveheart = media.Movie(
    "Braveheart",
    "Mel Gibson",
    "Braveheart is a 1995 American epic war film directed by Mel "
    "Gibson, who stars as William Wallace, a late 13th-century "
    "Scottish warrior who led the Scots in the First War of "
    "Scottish Independence against King Edward I of England. ",
    "http://static.tvgcdn.net/rovi/showcards/movie/130677/thumbs/16930914_1242x1656.jpg",  # NOQA
    "https://www.youtube.com/watch?v=nMft5QDOHek")

# Storing all movie in an array
movies = [titanic, gladiator, the_notebook, king_kong, casino_royale,
          braveheart]

# Sending an array to list
fresh_tomatoes.open_movies_page(movies)
