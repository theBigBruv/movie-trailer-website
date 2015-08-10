import webbrowser

#Create a Movie class for storing movie related information
class Movie():
    
    #Define movie properties in the Movie class
    def __init__(self, title, release_year, rating, storyline, director, stars, poster_image_url, trailer_youtube_url):
        self.title = title
        self.release_year = release_year
        self.rating = rating
        self.storyline = storyline
        self.director = director
        self.stars = stars
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    #Define a function in the Movie class that accepts a movie trailer url as input and plays the trailer on a browser    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)