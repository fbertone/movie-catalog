# imports of helper functions
import media
import fresh_tomatoes

# add or create new entries following the examples
# each Movie object must be initialized with 3 strings: the title, the poster and the link to the trailer on youtube
machete = media.Movie("Machete",  
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZWUxODc2NmItNThkNS00Mzc4LThlYTQtOTYwZjVhYjRiNmMwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg", 
    "https://www.youtube.com/watch?v=I16020r--oM")

machete_kills = media.Movie("Machete Kills",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA2MzUxMTM3M15BMl5BanBnXkFtZTgwMzA2NzkxMDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=DwbG64YC-vQ")

# add all the Movies in this array
movies = [machete, machete_kills]

# this call create the actual catalog in html
fresh_tomatoes.open_movies_page(movies)
