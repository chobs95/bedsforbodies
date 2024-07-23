"""
What do we need the class to do?


The information we need to store is whether a user is logged in or not. This needs to be cached in an instance of the applicaiton. 

We need to call on the database to see whether the entered credentials match a log in the user table. 

If there's no match we get an error

If there is a match we are logged into the users account.


"""

"""
What we need to work out?

How to store a session locally when a user logs in.



====
"""

from lib.database_connection import DatabaseConnection
from lib.user import User
import psycopg
import flask
import flask_login


app = flask.Flask(__name__)
# app.secret_key = ''  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


database_connection = DatabaseConnection()
database_connection.connect()
user_list = database_connection.execute('SELECT name FROM users',[])
users = [user['name'] for user in user_list]

def list_of_users():
    database_connection = DatabaseConnection()
    database_connection.connect()
    user_list = database_connection.execute('SELECT name FROM users',[])
    users = [user['name'] for user in user_list]
    return users


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return "account not found"

    user = User()
    user.name = email 
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    
    user = User()
    user.name = email
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
                <form action='login' method='POST'>
                    <input type='text' name='email' id='email' placeholder='email'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                </form>
                '''
    
    email = flask.request.form['email']
    password = flask.request.form['password']
    user = DatabaseConnection.execute('SELECT name, password FROM users WHERE name = %s', [email])


    if user != []:
        if password == user[0]['password']:
            current_user = email
            flask_login.login_user(current_user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


