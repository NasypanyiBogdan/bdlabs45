from dao.user_dao import UserDAO
from dto.user_dto import UserDTO

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def get_all_users(self):
        users = self.user_dao.get_all()
        return [UserDTO.to_json(u) for u in users]

    def get_user_by_id(self, user_id):
        user = self.user_dao.get_by_id(user_id)
        return UserDTO.to_json(user)

    def create_user(self, data):
        return self.user_dao.create(data['firstName'], data['lastName'], data['email'], data['phone'])

    def update_user(self, user_id, data):
        self.user_dao.update(user_id, data['firstName'], data['lastName'], data['email'], data['phone'])

    def delete_user(self, user_id):
        self.user_dao.delete(user_id)

    def get_rooms_for_object(self, object_id):
        return self.user_dao.get_rooms_by_object(object_id)

    def get_objects_for_user(self, user_id):
        return self.user_dao.get_objects_for_user(user_id)