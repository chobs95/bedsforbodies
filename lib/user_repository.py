# File: lib/user_repository.py

from lib.database_connection import DatabaseConnection
import hashlib

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def list(self):
        user_lists = self._connection.execute('SELECT name, password FROM users')
        print('===> LIST')
        print(user_lists)
        return user_lists

    def create(self, email, password, password_authenticator):
        # Hash the password
        # binary_password = password.encode("utf-8")
        # hashed_password = hashlib.sha256(binary_password).hexdigest()
        email_list = []
        rows = self._connection.execute('SELECT name FROM users')
        for row in rows:
            email_list.append(row['name'])
        if email in email_list:
            return 2
        if password != password_authenticator:
            return 1
        # Store the email and hashed password in the database
        self._connection.execute(
            'INSERT INTO users (name, password) VALUES (%s, %s)',
            [email, password])
        return 0
        
        

    def check_password(self, email, password_attempt):
        # binary_password_attempt = password_attempt.encode("utf-8")
        # hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT id FROM users WHERE name = %s AND password = %s',
            [email, password_attempt])

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0 

    # ...
    def get_user_id_from_email(self, email):
        rows = self._connection.execute(
            'SELECT id FROM users WHERE name = %s',
            [email])
        row = rows[0]
        id = row['id']
        return id
    
