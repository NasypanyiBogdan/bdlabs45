from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Стикувальна таблиця для M:M
movies_has_genres = db.Table('movies_has_genres',
    db.Column('movies_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True),
    db.Column('genres_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    duration = db.Column(db.Integer)
    # Зв'язок M:M
    genres = db.relationship('Genre', secondary=movies_has_genres, backref='movies')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration,
            "genres": [g.name for g in self.genres]
        }

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)