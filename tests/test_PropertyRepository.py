from lib.PropertyRepository import PropertyRepository
from lib.Property import *

"""
When I call on the PropertyRepository
I get all the properties back in a list
"""

def test_lists_all_properties(db_connection):
    db_connection.seed('seeds/bedsforbodies_seed.sql')
    property_repository = PropertyRepository(db_connection)
    result = property_repository.all()
    print(result)
    assert result ==[
        Property(1, 'test_property1', 'This place is nice', 'test1', 999, 1),
        Property(2, 'test_property2', 'This place is okay', 'test2', 888, 1), 
        Property(3, 'test_property3', 'This place is amazing', 'test3', 777, 2), 
        Property(4, 'test_property4', 'This place is cool', 'test4', 666, 2), 
        Property(5, 'test_property5', 'This place is wicked', 'test5', 555, 3), 
        Property(6, 'test_property6', 'This place is rubbish', 'test6', 444, 3),
]
    
"""
check that when we create a new property
it is properly reflected within the database
"""

def test_creates_a_property(db_connection):
    db_connection.seed('seeds/bedsforbodies_seed.sql')
    property_repository = PropertyRepository(db_connection)
    property_repository.add(Property(None, "test_property7", "This place is grand", "test7", 333, 3))
    result = property_repository.all()

    assert result ==[
        Property(1, 'test_property1', 'This place is nice', 'test1', 999, 1),
        Property(2, 'test_property2', 'This place is okay', 'test2', 888, 1), 
        Property(3, 'test_property3', 'This place is amazing', 'test3', 777, 2), 
        Property(4, 'test_property4', 'This place is cool', 'test4', 666, 2), 
        Property(5, 'test_property5', 'This place is wicked', 'test5', 555, 3), 
        Property(6, 'test_property6', 'This place is rubbish', 'test6', 444, 3),
        Property(7, 'test_property7', 'This place is grand', 'test7', 333, 3),
]


"""
check that deleting a property 
removes it from the database
"""

def test_delete_a_property(db_connection):
    db_connection.seed('seeds/bedsforbodies_seed.sql')
    property_repository = PropertyRepository(db_connection)
    property_repository.delete(2)
    result = property_repository.all()

    assert result == [
        Property(1, 'test_property1', 'This place is nice', 'test1', 999, 1),
        Property(3, 'test_property3', 'This place is amazing', 'test3', 777, 2), 
        Property(4, 'test_property4', 'This place is cool', 'test4', 666, 2), 
        Property(5, 'test_property5', 'This place is wicked', 'test5', 555, 3), 
        Property(6, 'test_property6', 'This place is rubbish', 'test6', 444, 3),
    ]
    