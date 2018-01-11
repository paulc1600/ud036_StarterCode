import webbrowser


class Movie():
    """ This class provides a way to store movie related information. """
    # Only if directly below class statement does get picked up by "__doc__"

    # Class variable because outside all functions
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_sline, poster_image, trail_youtube):
        self.title = movie_title
        self.storyline = movie_sline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trail_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

