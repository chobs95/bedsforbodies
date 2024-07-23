from lib.BookingRequest import BookingRequest
from datetime import date
"""
Simple property constructs with an id etc.
"""
def test_property_request_constructs():
    propReq = BookingRequest(date(2024,7,8), date(2024,7,9),1,1,1, 'PENDING')
    assert propReq.property_id == 1
    assert propReq.user_id == 1
    assert propReq.status == 'PENDING'
    
"""
Call the state change methods.
"""
# TODO: Need to review these unit tests.