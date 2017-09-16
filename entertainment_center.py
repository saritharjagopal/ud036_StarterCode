import movies
import fresh_tomatoes
from media import Movie
								
movies = movies.get_movie_list()    
print(movies)
fresh_tomatoes.open_movies_page(movies)

print("The class "+Movie.__name__+" is present in the module "+Movie.__module__)



