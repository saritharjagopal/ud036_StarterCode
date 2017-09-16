from media import Movie

def get_movie_list():

    movies = []
    toy_story = Movie("Toy Story",
                      "A Story of a boy and his toys that come to life",
                      "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    movies.append(toy_story)

    avatar = Movie("Avatar",
                   "A marine on an alien planet",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8")
    movies.append(avatar)
    
    frozen = Movie("Frozen",
                   "A Story on act of true love",
                   "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=TbQm5doF_Uc")
    movies.append(frozen)

    pulimurugan = Movie("Pulimurugan",
                        "The daring Tiger man",
                        "https://upload.wikimedia.org/wikipedia/en/e/e1/Pulimurugan_film_poster.jpg",
                        "https://www.youtube.com/watch?v=blQUlD8g4Pk")
    movies.append(pulimurugan)

    bahubali = Movie("Bahubali ",
                     "The Beginning",
                     "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                     "https://www.youtube.com/watch?v=sOEg_YZQsTI")
    movies.append(bahubali)

    boss_baby = Movie("Boss Baby ",
                      "Baby Boss",
                      "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Boss_Baby_poster.jpg",
                      "https://www.youtube.com/watch?v=h24gEn3y82Q")
    movies.append(boss_baby)

    turbo = Movie("Turbo ",
                  "Fast and Furious Turbo Snail",
                  "https://upload.wikimedia.org/wikipedia/en/b/b9/Turbo_%28film%29_poster.jpg",
                  "https://www.youtube.com/watch?v=QULzGYRThH8")
    movies.append(turbo)

    
    return movies
