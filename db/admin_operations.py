# db/admin_operations.py

from .mysql_connector import MySQLConnector

class AdminOperations:
    @staticmethod
    def create_admin(name, username, email, password):
        with MySQLConnector() as cursor:
            cursor.execute("INSERT INTO admin (name, username, email, password) VALUES (%s, %s, %s, %s)",
                           (name, username, email, password))

    @staticmethod
    def read_admin_by_id(admin_id):
        with MySQLConnector() as cursor:
            cursor.execute("SELECT * FROM admin WHERE id = %s", (admin_id,))
            return cursor.fetchone()

    # Implement update and delete operations similarly
