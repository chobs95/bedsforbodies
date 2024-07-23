from lib.user_repository import UserRepository

"""
test that the create a user works as intended
"""

def test_creates_a_user_and_adds_to_database(db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    user_repository = UserRepository(db_connection)
    user_repository.create('charlieroberts.editor@gmail.com','blahblahblah', 'blahblahblah')
    result = user_repository.list()
    assert result == [
        {'name': 'charlie_roberts23@hotmail.co.uk', 'password': 'Password!23',},
        {'name': 'taconlin@hotmail.co.uk', 'password': 'Password!24'},
        {'name': 'joshuadosanjh@gmail.com', 'password': 'Qwerty?09'},
        {'name': 'charlieroberts201@hotmail.co.uk', 'password': 'passWord?12'},
        {'name': 'charlieroberts.editor@gmail.com', 'password': 'blahblahblah'}
        ]
    
"""
checks that the check_password function is working correctly
"""

def test_check_password_finds_matching_credentials_on_database(db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    user_repository = UserRepository(db_connection)
    result1 = user_repository.check_password('charlie_roberts23@hotmail.co.uk', 'Password!23')
    assert result1 == True
    result2 = user_repository.check_password('charlie_roberts23@hotmail.co.uk', 'Password!43')
    assert result2 == False
    
