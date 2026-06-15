class UserDTO:
    @staticmethod
    def to_json(user_dict):
        if not user_dict:
            return None
        return {
            "userId": user_dict['id'],
            "fullName": f"{user_dict['first_name']} {user_dict['last_name']}",
            "email": user_dict['email'],
            "phoneNumber": user_dict['phone']
        }