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