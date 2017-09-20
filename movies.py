from media import Movie  # importing Movie class from media module


def get_movie_list():

    # initialize an empty movies array
    movies = []

    # Define Movie 1 (Toystory) and add to the movies list
    toy_story = Movie("Toy Story",
                      "A Story of a boy and his toys that come to life",
                      "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    movies.append(toy_story)

    # Define Movie 2 (Avatar) and add to the movies list
    avatar = Movie("Avatar",
                   "A marine on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8")
    movies.append(avatar)

    # Define Movie 3 (Frozen) and add to the movies list
    frozen = Movie("Frozen",
                   "A Story on act of true love",
                   "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=TbQm5doF_Uc")
    movies.append(frozen)

    # Define Movie 4 (Pulimurugan) and add to the movies list
    pulimurugan = Movie("Pulimurugan",
                        "The daring Tiger man",
                        "https://upload.wikimedia.org/wikipedia/en/e/e1/Pulimurugan_film_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=blQUlD8g4Pk")
    movies.append(pulimurugan)

    # Define Movie 5 (Bahubali) and add to the movies list
    bahubali = Movie("Bahubali ",
                     "The Beginning",
                     "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=sOEg_YZQsTI")
    movies.append(bahubali)

    # Define Movie 6 (Boss Baby) and add to the movies list
    boss_baby = Movie("Boss Baby ",
                      "Baby Boss",
                      "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=h24gEn3y82Q")
    movies.append(boss_baby)

    # Define Movie 7 (Turbo) and add to the movies list
    turbo = Movie("Turbo ",
                  "Fast and Furious Turbo Snail",
                  "https://upload.wikimedia.org/wikipedia/en/b/b9/Turbo_%28film%29_poster.jpg",  # NOQA
                  "https://www.youtube.com/watch?v=QULzGYRThH8")
    movies.append(turbo)

    return movies
