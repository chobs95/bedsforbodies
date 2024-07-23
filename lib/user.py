from lib.BookingRequest import BookingRequest

class User:
    #What does the user need to store? Their Reservations, their locations, password, username
    #What methods do we need for the user? View Requests - Reject or Approve
    def __init__(self,connection,username,password):
        self.connection = connection
        connection.execute('INSERT INTO USERS (name, password) VALUES (%s, %s)',
                        [username,password])
        self.id = connection.execute('SELECT id FROM USERS WHERE name = %s',[username])[0]['id']
    
    def view_requests_to_approve(self):
        myproperties = self.connection.execute('SELECT id FROM properties WHERE user_id = %s',[self.id])
        ToReview = []
        for property in myproperties:
            ToReview += self.connection.execute('SELECT id FROM bookings WHERE property_id = %s',[property['id']]) #Will also include a clause that the status is pending when implemented into the database
        return ToReview
