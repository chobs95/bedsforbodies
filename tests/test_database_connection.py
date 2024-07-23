# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/bedsforbodies_seed.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO users (name, password) VALUES (%s, %s)", ["charlieroberts.editor@gmail.com","apassword123!"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM users")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "name": "charlie_roberts23@hotmail.co.uk", "password": "Password!23"},
        {"id": 2, "name": "taconlin@hotmail.co.uk", "password": "Password!24"},
        {"id": 3, "name": "joshuadosanjh@gmail.com", "password": "Qwerty?09"},
        {"id": 4, "name": "charlieroberts201@hotmail.co.uk", "password": "passWord?12"},
        {"id": 5, "name": "charlieroberts.editor@gmail.com", "password": "apassword123!"},
    ]

