
class Movie:
    def __init__(self, title, genres_associated, languages_availables, runtime, overview, adult, release_date, tagline, vote_average, keywords, cast):
        self.title = title
        self.genres_associated = eval(genres_associated)
        self.languages_availables = eval(languages_availables)
        self.runtime = runtime
        self.overview = overview
        self.adult = adult
        self.release_date = release_date
        self.tagline = tagline
        self.vote_average = vote_average
        self.keywords = eval(keywords)
        self.cast = eval(cast)