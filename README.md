# Movie Trailer
This is a small movie trailer project with seven movies.

Source Code: https://github.com/saritharjagopal/ud036_StarterCode



		
To Run the project.

1. Download the code the given github link.
2. Open the local folder where the code is copied.
3. Open command prompt for this folder path.
4. run entertainment_center.py file 
5. A web browser would be opened with a list of movies displayed.
6. Select any movie for which you wish to see the trailer.
7. Your trailer would be displayed. Enjoy!!


Library - fresh_tomatoes
	This library was taken from the starter kit for this project
	This library expects the Movie list to be passed on to the method open_movies_page()
	The Movie list Should be a list of Object that has the following parameters
		1.	title 				- Name of the Movie
		2. poster_image_url 	- Link to Movie Poster
		3. trailer_youtube_url 	- Link to the youtube trailer
		

Modules - Media.py
		This module has the class Movie.
		The constructor of this class expects - title, storyline, poster_image, 
							and trailer link in the corresonding order
		This class could be used to create as many instance of Movie that you would wish to create.
	
	
	-	movies.py
		This is a utility module
		This has a function get_movie_list()
		This list would give you the list of 7 movies added for this demo
		
	- entertainment_center.py 
		This is the main module
		This creates the movie list and pass it on to the 
			fresh_tomatoes open_movies_page() method which,
			intern creates the HTML page and opens the same in browser
			
