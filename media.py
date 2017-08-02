# class for Movies

class Movie():
""" The Movie class creates object of type Movie
Three string arguments must be passed: title, poster image url and youtube trailer url
"""  
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

