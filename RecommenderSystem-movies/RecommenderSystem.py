import csv, os, inspect
from Users import Users
from Movie import Movie
import nltk
import spacy
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class RecommenderSystem():

    def __init__(self):
        self.csv_users = "users.csv"
        self.users = []
        self.csv_movies = "movies_with_genres.csv"
        self.movies = []
        #self.read_users()
        self.read_movies()
        self.contFilms = 1
        self.columnNames = []


        # Cargar el analizador de sentimientos VADER
        self.sid = SentimentIntensityAnalyzer()
        self.positiveGenres = ['Action', 'Adventure', 'Comedy']
        self.negativeGenres = ['Drama', 'Thriller', 'Horror']
        self.recommendations = []
        self.process_finished = False


    def read_users(self):
        try:
            with open(self.csv_users, 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    # Ampliacion: 
                    # fila['genresFavNegative'] -> generos para cuando el estado es negativo
                    # fila['genresFavPositive'] -> generos para cuando el estado es positivo
                    # fila['lastRecomendation'] -> ultima recomendacion para que puntue y el código aprenda si lo ha hecho bien ¿RNN?
                    user = Users(fila['user'], fila['favoriteFilm'], int(fila['age']), fila['genresFavs'], fila['actorFavs'])
                    self.users.append(user)
        except FileNotFoundError:
            print(f"El archivo '{self.csv_users}' no se encontró.")

    def read_movies(self):
        try:
            with open(self.csv_movies, 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    movie = Movie(fila['title'], fila['genres_associated'], fila['languages_availables'],
                                 fila['runtime'], fila['overview'], fila['adult'], fila['release_date'],
                                   fila['tagline'], fila['vote_average'], fila['keywords'], fila['cast'])
                    self.movies.append(movie)
        except FileNotFoundError:
            print(f"El archivo '{self.csv_movies}' no se encontró.")

    '''
    Extract the sentiment of the text passed
    text: contains the answer of how do you feel today
    '''
    def get_sentiment(self, text):
        sentiment_scores = self.sid.polarity_scores(text)
        if sentiment_scores['compound'] >= 0.05:
            return 'positive'
        elif sentiment_scores['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    '''
    Searchs on dataset what films are more fit for the user
    - user_preferences: genres selected to the user obtained throws sentiment
    '''
    def get_recommendations(self, user_preferences):
        sorted_movies = sorted(self.movies, key=lambda movie: 
                                   sum(1 for genre in movie.genres_associated if genre in user_preferences), reverse=True)
        return sorted_movies
    
    '''
    Analyze the text to extract the name of the film in the text
    '''
    def get_data_by_text(self, user_text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(user_text)
        movie_titles = [movie.title for movie in self.movies]
        #matching_movies = [title for title in movie_titles if title.lower() in user_text.lower()]
        relevant_info = []
        print(self.columnNames)

        column_name = None
        movie_title = None

        # Obtener los atributos de la clase Movie
        movie_attributes = inspect.getmembers(Movie)
        print("movie attributes: ", movie_attributes)

        # Buscar nombres de atributos de la clase Movie en el texto procesado
        for token in doc:
            for attr_name, attr_value in movie_attributes:
                if token.text.lower() == attr_name.lower():
                    if attr_name == "genres_associated":
                        column_name = "genres_associated"
                    else:
                        movie_title = getattr(Movie, attr_name).title
        print("Column: ", column_name)
        print("Film: ", movie_title)

    # ----------------------------------------------------------------------------------------------------------------------
        
    '''
    The first text to send to the user
    '''
    def welcome_feeling(self):
        opcion = input("Welcome to MovIA, how do you feel today? ")
        sentiment = self.get_sentiment(opcion)

        print(f"You have {sentiment} feelings...")
        opcion2 = input("Do you want any particular genre?")
        if opcion2 == "No" or opcion2 == "":
            if sentiment == "positive":
                genres = self.positiveGenres
            elif sentiment == "negative":
                genres = self.negativeGenres
            else:
                genres = ['Adventure', 'Fantasy', 'Family'] # cambiar a todos los generos
        elif opcion2 == "Yes": 
            opcion2 = input("\n What genres do you prefer?", sentiment)
        else:
            text_normalized = opcion2.replace(" o ", ",").replace(" y ", ",").replace(",", "")
            genres = text_normalized.split(",")
        print("\nGenres selected: ", genres)
        return genres
    
    def process_recommendation(self):
        while not self.process_finished:
            answer = input("Do you like the selection? ")
            self.handle_selection(answer)
        print(f"We hope you enjoy watching '{self.recommendations[self.contFilms-1].title}'!")


    def handle_selection(self, answer):
        if answer.lower() in ["yes", "ok"]:
            self.ask_about_film()
        elif answer.lower() == "no":
            self.show_other_options()
        else:
            print("Invalid response. Please answer yes or no")

    def ask_about_film(self):
        answer = input("Do you want to know something about any film? ")
        if answer.lower() in ["yes", "ok"]:
            self.ask_more_about_film()

    def ask_more_about_film(self):
        while True:
            answer = input("Do you want to know something else? ")
            if answer.lower() == "no":
                break
            elif answer.lower() in ["yes", "ok"]:
                text = input("Tell me what do you want to know...")
                self.get_data_by_text(text)
                text2 = input("Is everything all right?")
                if text2.lower() in ["yes", "ok"]:
                    continue
                else:
                    print("Invalid response. Please answer yes or no")
            else:
                print("Invalid response. Please answer yes or no")


    def show_other_options(self):
        print("Understood, I can show you some other options that fit your profile...")
        if self.contFilms < len(self.recommendations):
            print("\nThe new film selected is: ", self.recommendations[self.contFilms].title)
            self.contFilms += 1
            self.process_recommendation()
        else:
            print("Sorry, there are no more recommendations.")
            self.process_finished = True


    '''
    Gestor of the proyect 
    '''
    def menu(self):
        genres = self.welcome_feeling()
        self.recommendations = self.get_recommendations(genres)
        print("\n Your recommendation is: ", self.recommendations[0].title)
        self.process_recommendation()
  
    
    '''
    Process the response of the user 
    
    def process_recommendation(self):
        process_finished = False
        answer = input("Do you like the selection? ")
        while process_finished != True:
            if answer == "yes" or answer == "Yes" or answer == "ok":
                answer = input("Do you want to know something about any film? ")
                # tell me the overview of xxx 
                self.get_data_by_text(answer)
                answer = input("Do you want to know something else? ")
                while process_finished != True or answer == "" or answer == "no" or answer == "No":
                    text = input("Tell me what do you want to know...")
                    self.get_data_by_text(text)
                    text2 = input("Is everything allright?")
                    if text2 == "yes" or text2 == "Yes" or text2 == "ok":
                        process_finished = True
            else:
                print("Understood, I can show you some other options that fit your profile...")
                print("\n The new film selected is: ", self.recommendations[self.contFilms].title)
                self.contFilms = self.contFilms + 1
        return process_finished
'''
          
if __name__ == "__main__":
    manager = RecommenderSystem()
    manager.menu()