class Users():
    '''
    user_id: identifier of the user (unique)
    favorite_film: list that contains the favorite films of the user
    age: to control if the user has the correct age for the film recommended
    favorite_genres: to filter the films by genres
    favorite_actors: is optional to filter the films
    ''' 
    def __init__(self, user_id, favorite_film, age, favorite_genres, favorite_actors):
        self.user_id = user_id
        self.favorite_film = favorite_film
        self.age = age
        self.favorite_genres = favorite_genres
        self.favorite_actors = favorite_actors