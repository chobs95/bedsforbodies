from lib.Property import Property

class PropertyRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from properties') # Need SQL from Charlie and Tara.
        property_list = []
        for row in rows:
            pr = Property(row['id'], row['property'], row['description'], row['location'], row['cost'], row['user_id'])
            property_list.append(pr)
        print(property_list)
        return property_list
    
    def add(self, property):
        self._connection.execute('INSERT INTO properties (property, description, location, cost, user_id) VALUES (%s, %s, %s, %s, %s)', [
                                property.property, property.description, property.location, property.cost, property.user_id])
        return None
    
    def find(self, property_id):
        rows = self._connection.execute("SELECT * FROM properties WHERE id = %s", [property_id])
        row = rows[0]
        return Property(row["id"], row["property"], row["description"], row["location"], row["cost"], row["user_id"])

    def delete(self, property_id):
        self._connection.execute(
            'DELETE FROM properties WHERE id = %s', [property_id])
        return None