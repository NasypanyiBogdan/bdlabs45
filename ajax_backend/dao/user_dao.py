import mysql.connector
from config import db_config

class UserDAO:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(**db_config)

    def get_all(self):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def get_by_id(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    def create(self, first_name, last_name, email, phone):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, email, phone))
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return new_id

    def update(self, user_id, first_name, last_name, email, phone):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s"
        cursor.execute(query, (first_name, last_name, email, phone, user_id))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

    # Вимога: Зв'язок M:1 (Для об'єкта вивести його кімнати)
    def get_rooms_by_object(self, object_id):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id, name, room_type FROM rooms WHERE object_id = %s"
        cursor.execute(query, (object_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    # Вимога: Зв'язок M:M (Для користувача вивести всі його об'єкти з ролями)
    def get_user_objects(self, user_id):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT po.id, po.name, po.address, uo.role 
            FROM protected_objects po
            JOIN user_objects uo ON po.id = uo.object_id
            WHERE uo.user_id = %s
        """
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result