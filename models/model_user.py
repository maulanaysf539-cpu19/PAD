from database import get_connection


class UserModel:

    @staticmethod
    def login(username, password):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE username=? AND password=?
        """, (username, password))

        user = cursor.fetchone()

        conn.close()

        return user