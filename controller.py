from flask import Blueprint, jsonify, request
from service import MovieService

movie_bp = Blueprint('movies', __name__)
movie_service = MovieService()

# Вивід даних (CRUD: Read) 
@movie_bp.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movie_service.get_all_movies_dto()), 200

# Вставка даних (CRUD: Create) 
@movie_bp.route('/movies', methods=['POST'])
def post_movie():
    data = request.get_json()
    result = movie_service.add_new_movie(data)
    return jsonify(result), 201

@movie_bp.route('/api/add-genre', methods=['POST'])
def add_genre():
    name = request.json.get('name')
    db.session.execute(db.text("CALL sp_add_genre(:name)"), {'name': name})
    db.session.commit()
    return {"message": "Жанр додано через процедуру"}, 201