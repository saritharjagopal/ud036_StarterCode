import webbrowser


class Movie():

    # Movie Class Constructor
    def __init__(self, title, storyline, poster_image,
                 trailer_link):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link

    # Opens the webbrowser to show the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
