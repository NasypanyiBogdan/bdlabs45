from flask import Blueprint, request, jsonify
from service.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)
user_service = UserService()

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_service.get_all_users()), 200

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_blueprint.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_id = user_service.create_user(data)
    return jsonify({"message": "User created", "id": new_id}), 201

@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.get_json()
    user_service.update_user(user_id, data)
    return jsonify({"message": "User updated"}), 200

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 200

# Роут для зв'язку M:1 (Всі кімнати для об'єкта)
@user_blueprint.route('/objects/<int:object_id>/rooms', methods=['GET'])
def get_object_rooms(object_id):
    rooms = user_service.get_rooms_for_object(object_id)
    return jsonify(rooms), 200

# Роут для стикувальної таблиці M:M (Всі об'єкти користувача)
@user_blueprint.route('/users/<int:user_id>/objects', methods=['GET'])
def get_user_objects(user_id):
    objects = user_service.get_objects_for_user(user_id)
    return jsonify(objects), 200