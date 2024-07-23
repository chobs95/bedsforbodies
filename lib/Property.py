class Property:
    def __init__(self, id, property, description, location, cost, user_id):
        self.id = id
        self.property = property
        self.description = description
        self.location = location
        self.cost = cost
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Property({self.id}, {self.property}, {self.description}, {self.location}, {self.cost}, {self.user_id})"
    
    def is_valid(self):
        return bool(self.property and self.description and self.location and self.cost and self.user_id)

    def generate_errors(self):
        errors = []
        if not self.property:
            errors.append("Property name is required.")
        if not self.description:
            errors.append("Description is required.")
        if not self.location:
            errors.append("Location is required.")
        if not self.cost:
            errors.append("Cost is required.")
        if not self.user_id:
            errors.append("User ID is required.")
        return errors