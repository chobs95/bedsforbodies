from lib.Property import Property


""""
check class instance is instance of a class
"""

def test_check_class_is_instance():
    property = Property(1, 'property1', 'nice place', 'maldives', '999', '1')
    assert isinstance(property, Property)

"""
check that the class constructs with the correct properties

property, description, location, cost, user_id
"""

def test_checks_class_instance_is_created():
    property = Property(1, 'property1', 'nice place', 'maldives', '999', '1')
    assert property.id == 1
    assert property.property == 'property1'
    assert property.description == 'nice place'
    assert property.location == 'maldives'
    assert property.cost == '999'
    assert property.user_id == '1'
    
"""
checks to see whether the property is formated nicely
"""    
    
def test_artists_format_nicely():
    property = Property(1, "Test Property", "test description", 'test location', '999', '1')
    assert str(property) == "Property(1, Test Property, test description, test location, 999, 1)"

"""
We can compare two instances of the same properties
And have them be equal
"""

def test_instances_of_same_property_are_considered_equal():
    property1 = Property(1, "Test Property", "test description", 'test location', '999', '1')
    property2 = Property(1, "Test Property", "test description", 'test location', '999', '1')
    assert property1 == property2