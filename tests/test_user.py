from lib.user import User
from lib.BookingRequest import BookingRequest
from lib.BookingRequestRepository import *

def test_setup(db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    newuser = User(db_connection, 'Jane@Janemail.com', 'Jan£Do£123')
    assert isinstance(newuser, User)
    k = db_connection.execute("SELECT name FROM USERS WHERE id = 5")
    assert k == [{'name': 'Jane@Janemail.com'}]
    assert newuser.id == 5

def test_request_view(db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    newuser = User(db_connection, 'Jane@Janemail.com', 'Jan£Do£123')
    assert newuser.id == 5
    assert len(newuser.view_requests_to_approve()) == 0
    db_connection.execute("INSERT INTO properties (property, description, location, cost, user_id) VALUES ('test_property7', 'This place is slightly above average', 'test7', '111', '5')")
    assert len(newuser.view_requests_to_approve()) == 0
    db_connection.execute("INSERT INTO bookings (property_id, user_id, start_date, end_date) VALUES (7,2,'2025-01-01', '2025-01-08')")
    assert len(newuser.view_requests_to_approve()) == 1