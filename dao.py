from domain import db, Movie

class MovieDAO:
    def get_all(self):
        return Movie.query.all()

    def get_by_id(self, movie_id):
        return Movie.query.get(movie_id)

    def create(self, movie):
        db.session.add(movie)
        db.session.commit()
        return movie

    def delete(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()