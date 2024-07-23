from lib.login_app import list_of_users


"""
Test that our users variable is a list of users
"""

def test_check_user_loader_returns_user(db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    result = list_of_users()
    assert result == ['charlie_roberts23@hotmail.co.uk','taconlin@hotmail.co.uk', 'joshuadosanjh@gmail.com', 'charlieroberts201@hotmail.co.uk']


