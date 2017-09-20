import movies
import fresh_tomatoes


# Get the list of movies to be displayed
movies = movies.get_movie_list()

# Pass the movies List to be viewed on the browser
fresh_tomatoes.open_movies_page(movies)
