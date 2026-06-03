from dao import MovieDAO

class MovieService:
    def __init__(self):
        self.movie_dao = MovieDAO()

    def get_all_movies_dto(self):
        movies = self.movie_dao.get_all()
        # Повертаємо дані у вигляді DTO (dict у Python) 
        return [m.to_dict() for m in movies]

    def add_new_movie(self, data):
        from domain import Movie
        new_movie = Movie(title=data.get('title'), duration=data.get('duration'))
        return self.movie_dao.create(new_movie).to_dict()